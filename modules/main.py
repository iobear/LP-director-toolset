#!/usr/bin/env python
#

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

class API:
	data = {}
	devicegroup = DeviceGroups()
	config = ApiConfig()
	device = Devices()
	repo = Repos()
	connect = Connect()
	orders = Orders()
	processingpolicy = ProcessingPolicy()
	normalizationpolicy = NormalizationPolicy()
	normalizationpackage = NormalizationPackage()
	opendoor = OpenDoor()
	systemsettingsntp = SystemSettingsNTP()

	def __init__(self, out, task, debug, parameter = ''):
		self.show = Format(out, debug)
		self.task = task
		self.data['task'] = task
		self.data['userinput'] = parameter


	def repos(self):
		self.data['default'] = self.config.default_repo_parameters

		if self.task == 'get':
			self.data['repoapi'] = self.connect.getOption('Repos')
			self.data['repos'] = self.repo.getAll(self.data['repoapi'])
			self.show.printformat(self.data['repos'])

		if self.task == 'edit':
			self.data = self.repo.update(self.data)
			self.data['http'] = 'PUT'
			result = self.connect.update(self.data)
			self.show.printOrders(result)

		if self.task == 'create':
			self.data = self.repo.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)

		if self.task == 'delete' or self.task == 'trash':
			pass


	def devices(self):
		self.data['option'] = 'Devices'
		self.data['groupapi'] = self.connect.getOption('DeviceGroups')
		self.data['devicegroups'] = self.devicegroup.getNamesOnly(self.data['groupapi'])
		self.data['ppapi'] = self.connect.getOption('ProcessingPolicy')
		self.data['processingpolicy'] = self.processingpolicy.getNamesOnly(self.data['ppapi'])

		if self.task == 'get':
			self.data['deviceapi'] = self.connect.getOption('Devices')
			self.data = self.device.listall(self.data)
			self.show.printformat(self.data['devicelist'])

		if self.task == 'create':
			self.data['default'] = self.config.default_device_parameters
			result = self.connect.update(self.data)
			self.show.printOrders(result)

		if self.task == 'edit':
			self.data['devices'] = self.connect.getOption('Devices')
			self.data['default'] = self.config.default_device_parameters
			self.data = self.device.update(self.data)
			result = self.connect.update(self.data)
			self.show.printOrders(result)

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

		if self.task == 'create':
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
		apiresponse = self.connect.getOption('RoutingPolicies')
		self.data['routing_policy'] = self.namesOnly(apiresponse, 'policy_name')

		if self.task == 'get':
			self.data['ppapi'] = self.connect.getOption('ProcessingPolicy')
			self.data = self.processingpolicy.listAll(self.data)
			self.show.printformat(self.data)


	def normalizationPolicy(self):

		if self.task == 'get':
			self.data['normpackapi'] = self.connect.getOption('NormalizationPackage')
			self.data['normalizationpackage'] = self.normalizationpackage.getNames(self.data['normpackapi'])
			self.data['normpolapi'] = self.connect.getOption('NormalizationPolicy')

			self.data['normalizationpolicy'] = self.normalizationpolicy.getAll(self.data)

			self.show.printformat(self.data['normalizationpolicy'])

		if self.task == 'create':
			pass


	def normalizationPackage(self):

		if self.task == 'get':
			self.data['normpackapi'] = self.connect.getOption('NormalizationPackage')

			self.show.printformat(self.data['normpackapi'])


	def routingPolicy(self):

		if self.task == 'get':
			self.data['rpapi'] = self.connect.getOption('RoutingPolicies')

			self.show.printformat(self.data['rpapi'])


	def namesOnly(self, data, item):
		returndict = {}

		for stuff in data:
			returndict[stuff['id']] = stuff[item]

		return returndict
