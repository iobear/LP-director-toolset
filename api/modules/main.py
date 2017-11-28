#!/usr/bin/env python
#

import json
import time
from apiconnect import Connect
from devicegroups import DeviceGroups
from devices import Devices
from repos import Repos
from printer import Format
from config import ApiConfig
from orders import Orders
from processingpolicy import ProcessingPolicy
from normalizationpolicy import NormalizationPolicy
from normalizationpackage import NormalizationPackage
from opendoor import OpenDoor
from systemsettingsntp import SystemSettingsNTP
from syslogcollector import SyslogCollector
from routingpolicy import RoutingPolicy

class API:
	data = {}
	devicegroup = DeviceGroups()
	config = ApiConfig()
	device = Devices()
	repo = Repos()
	orders = Orders()
	processingpolicy = ProcessingPolicy()
	normalizationpolicy = NormalizationPolicy()
	normalizationpackage = NormalizationPackage()
	opendoor = OpenDoor()
	systemsettingsntp = SystemSettingsNTP()
	syslogcollector	= SyslogCollector()
	routingpolicy = RoutingPolicy()


	def __init__(self, args):
		self.connect = Connect(args.lphost)
		self.show = Format(args.output, self.config.debug)
		self.task = args.task
		self.data['task'] = args.task
		self.data['userinput'] = args.parameter
		self.file = args.file
		self.lphost = args.lphost


	def syslogcollectors(self):
		self.data['option'] = 'SyslogCollector'
		self.data['default'] = self.config.default_collector_parameters
		self.data['ppapi'] = self.connect.getOption('ProcessingPolicy')
		self.data['processingpolicy'] = self.processingpolicy.getNamesOnly(self.data['ppapi'])
		self.data['deviceapi'] = self.connect.getOption('Devices')
		self.data['devices'] = self.namesOnly(self.data['deviceapi'], 'name')


		if self.task in ['edit', 'delete', 'create']:
			if self.file:
				tasks = self.readJsonFile()
				for taskdata in tasks:
					self.data['data'] = taskdata
					enriched = self.syslogcollector.update(self.data)
					result = self.connect.update(enriched)
					self.show.printOrders(result)

			else:
				self.data = self.syslogcollector.update(self.data)
				result = self.connect.update(self.data)
				self.show.printOrders(result)


	def repos(self):
		self.data['default'] = self.config.default_repo_parameters

		if self.task == 'get':
			self.data['repoapi'] = self.connect.getOption('Repos')
			self.data['repos'] = self.repo.getAll(self.data['repoapi'])
			self.show.printformat(self.data['repos'])

		if self.task == 'edit':
			self.data = self.repo.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)

		if self.task == 'create':
			self.data = self.repo.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)

		if self.task == 'delete' or self.task == 'trash':
			self.data = self.repo.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def devices(self):
		self.data['option'] = 'Devices'
		self.data['default'] = self.config.default_device_parameters
		self.data['groupapi'] = self.connect.getOption('DeviceGroups')
		self.data['devicegroups'] = self.devicegroup.getNamesOnly(self.data['groupapi'])
		self.data['ppapi'] = self.connect.getOption('ProcessingPolicy')
		self.data['processingpolicy'] = self.processingpolicy.getNamesOnly(self.data['ppapi'])

		if not self.task == 'create':
			self.data['deviceapi'] = self.connect.getOption('Devices')
			self.data['devices'] = self.namesOnly(self.data['deviceapi'], 'name')

		if self.task == 'get':
			self.data = self.device.listall(self.data)
			self.show.printformat(self.data['devicelist'])

		if self.task in ['edit', 'delete', 'create']:
			if self.file:
				tasks = self.readJsonFile()
				for taskdata in tasks:
					self.data['data'] = taskdata
					enriched = self.device.update(self.data)
					result = self.connect.update(enriched)
					self.show.printOrders(result)

			else:
				self.data = self.device.update(self.data)
				result = self.connect.update(self.data)
				self.show.printOrders(result)


	def distributedLogpoints(self):
		if self.task == 'get':
			self.data['dlp'] = self.connect.getOption('DistributedLogpoints')
			self.show.printformat(self.data['dlp'])

		if self.task == 'create':
			self.data['option'] = 'DistributedLogpoints'
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def distributedCollectors(self):
		option = 'DistributedCollectors'

		if self.task == 'get':
			self.data['dcol'] = self.connect.getOption(option)
			self.show.printformat(self.data['dcol'])

		if self.task == 'create' or self.task == 'activate':
			self.data['option'] = option
			result = self.connect.update(self.data)
			self.show.printOrders(result)

		if self.task == 'refresh':
			self.refresh(option)


	def openDoor(self):
		if self.task == 'get':
			self.data['opendoorapi'] = self.connect.getOption('OpenDoor')
			self.data['opendoor'] = self.opendoor.getAll(self.data['opendoorapi'])
			self.show.printformat(self.data['opendoor'])

		if self.task == 'create':
			self.data['option'] = 'OpenDoor'
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def systemSettingsNTP(self):
		if self.task == 'get':
			self.data['systemsettingsntpapi'] = self.connect.getOption('SystemSettingsNTP')
			self.data['systemsettingsntp'] = self.systemsettingsntp.getAll(self.data['systemsettingsntpapi'])
			self.show.printformat(self.data['systemsettingsntp'])

		if self.task == 'restart':
			self.data['option'] = 'SystemSettingsNTP/ntprestart'
			result = self.connect.update(self.data)
			self.show.printOrders(result)

		if self.task == 'create':
			self.data['option'] = 'SystemSettingsNTP'
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def systemSettings(self):
		if self.task == 'get':
			self.data['systemsettingsapi'] = self.connect.getOption('SystemSettingsGeneral')

			self.show.rotatePrint(self.data['systemsettingsapi'])

		if self.task == 'create' or self.task == 'update':
			self.data['option'] = 'SystemSettingsGeneral'
			result = self.connect.update(self.data)
			self.show.printOrders(result)		


	def deviceGroups(self):
		self.data['option'] = 'DeviceGroups'

		if self.task == 'get':
			self.data['groupapi'] = self.connect.getOption('DeviceGroups')

			self.data['devicegroups'] = self.devicegroup.getAll(self.data['groupapi'])

			self.show.printformat(self.data['devicegroups'])

		if self.task == 'create':
			result = self.connect.update(self.data)

			self.show.printOrders(result)


	def processingPolicy(self):
		self.data['option'] = 'ProcessingPolicy'
		apiresponse = self.connect.getOption('RoutingPolicies')
		self.data['routing_policy'] = self.namesOnly(apiresponse, 'policy_name')
		apiresponse = self.connect.getOption('EnrichmentPolicy')
		self.data['enrich_policy'] = self.namesOnly(apiresponse, 'name')
		self.data['ppapi'] = self.connect.getOption('ProcessingPolicy')

		if self.task == 'get':
			self.data = self.processingpolicy.listAll(self.data)
			self.show.printformat(self.data)

		if self.task in ['edit', 'delete', 'create']:
			self.data = self.processingpolicy.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def normalizationPolicy(self):
		self.data['option'] = 'NormalizationPolicy'
		self.data['normpolapi'] = self.connect.getOption('NormalizationPolicy')

		if self.task == 'get':
			self.data['normpackapi'] = self.connect.getOption('NormalizationPackage') #get packege names, for translation
			self.data['normalizationpackage'] = self.normalizationpackage.getNames(self.data['normpackapi'])

			self.data['normalizationpolicy'] = self.normalizationpolicy.getAll(self.data)
			self.show.printformat(self.data['normalizationpolicy'])

		if self.task in ['edit', 'delete', 'create']:
			self.data = self.normalizationpolicy.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def normalizationPackage(self):
		option = 'NormalizationPackage'

		if self.task == 'get':
			self.data['normpackapi'] = self.connect.getOption(option)

			self.show.printformat(self.data['normpackapi'])

		if self.task == 'refresh':
			self.refresh(option)


	def routingPolicy(self):
		self.data['option'] = 'RoutingPolicies'
		self.data['rpapi'] = self.connect.getOption('RoutingPolicies')

		if self.task == 'get':
			self.show.printformat(self.data['rpapi'])

		if self.task in ['edit', 'delete', 'create']:
			self.data = self.routingpolicy.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def supportConnection(self):
		option = 'SystemSettingsSupportConnection'

		if self.task == 'get':
			self.data['supcon'] = self.connect.getOption(option)
			self.show.printformat(self.data['supcon'])

		if self.task == 'refresh':
			self.refresh(option)

		if self.task == 'create' or self.task == 'save':
			self.data['option'] = option
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def systemSettingsSSH(self):
		if self.task == 'get':
			self.data['SSSSH'] = self.connect.getOption('SystemSettingsSSH')
			self.show.printformat(self.data['SSSSH'])

		if self.task == 'create' or self.task == 'save':
			self.data['option'] = 'SystemSettingsSSH'
			result = self.connect.update(self.data)
			self.show.printOrders(result)


	def plugins(self):
		if self.task == 'get':
			self.data['plugins'] = self.connect.getOption('Plugins')
			self.show.printformat(self.data['plugins'])


	def enrichmentPolicy(self):
		if self.task == 'get':
			self.data['enrichmentpolicy'] = self.connect.getOption('EnrichmentPolicy')

			self.show.rotatePrint(self.data['enrichmentpolicy'])


	def refresh(self, item):
		self.data['option'] = item + '/refreshlist'
		self.data['userinput'] = ['data=true']
		result = self.connect.update(self.data)
		self.show.printOrders(result)


	def namesOnly(self, data, item):
		returndict = {}

		for stuff in data:
			returndict[stuff['id']] = stuff[item]

		return returndict


	def readJsonFile(self):
		with open(self.file) as json_data:
			return json.load(json_data)

