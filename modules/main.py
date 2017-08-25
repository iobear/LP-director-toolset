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

	def __init__(self, out, debug):
		#self.callapi = Connect()
		self.show = Format(out, debug)

	def repos(self):
		self.data['repoapi'] = self.connect.getOption('Repos')

		self.data['repos'] = self.repo.getAll(self.data['repoapi'])

		self.show.printformat(self.data['repos'])

	def devices(self, task, parameter = ''):
		self.data['userinput'] = parameter
		self.data['option'] = 'Devices'
		self.data['groupapi'] = self.connect.getOption('DeviceGroups')
		self.data['devicegroups'] = self.devicegroup.getNames(self.data['groupapi'])
		self.data['ppapi'] = self.connect.getOption('ProcessingPolicy')
		self.data['processingpolicy'] = self.processingpolicy.getNames(self.data['ppapi'])

		if task == 'get':
			self.data['deviceapi'] = self.connect.getOption('Devices')
			self.data = self.device.listall(self.data)
			#print self.data
			self.show.printformat(self.data['devicelist'])

		if task == 'create':
			self.data['default'] = self.config.defaultdeviceparameter
			result = self.connect.postoption(self.data)
			self.show.printOrders(result)


	def openDoor(self, task, parameter = ''):
		self.data['userinput'] = parameter
	
		if task == 'get':
			self.data['opendoorapi'] = self.connect.getOption('OpenDoor')
			self.data['opendoor'] = self.opendoor.getAll(self.data['opendoorapi'])
			self.show.printformat(self.data['opendoor'])

		if task == 'create':
			self.data['option'] = 'OpenDoor'
			self.data['default'] = ''
			result = self.connect.postoption(self.data)
			self.show.printOrders(result)


	def systemSettingsNTP(self, task, parameter = ''):
		self.data['userinput'] = parameter
	
		if task == 'get':
			self.data['systemsettingsntpapi'] = self.connect.getOption('SystemSettingsNTP')
			self.data['systemsettingsntp'] = self.systemsettingsntp.getAll(self.data['systemsettingsntpapi'])
			self.show.printformat(self.data['systemsettingsntp'])

		if task == 'restart':
			self.data['option'] = 'SystemSettingsNTP/ntprestart'
			self.data['default'] = ''
			result = self.connect.postoption(self.data)
			self.show.printOrders(result)


		if task == 'create':
			self.data['option'] = 'SystemSettingsNTP'
			self.data['default'] = ''
			result = self.connect.postoption(self.data)
			self.show.printOrders(result)


	def systemSettings(self, task, parameter = ''):
		self.data['userinput'] = parameter

		if task == 'get':
			self.data['systemsettingsapi'] = self.connect.getOption('SystemSettingsGeneral')

			self.show.rotatePrint(self.data['systemsettingsapi'])

		if task == 'create':
			self.data['option'] = 'SystemSettingsGeneral'
			self.data['default'] = ''
			result = self.connect.postoption(self.data)
			self.show.printOrders(result)		

	def deviceGroups(self, task, parameter = ''):
		self.data['userinput'] = parameter
		self.data['option'] = 'DeviceGroups'

		if task == 'get':
			self.data['groupapi'] = self.connect.getOption('DeviceGroups')

			self.data['devicegroups'] = self.devicegroup.getAll(self.data['groupapi'])

			self.show.printformat(self.data['devicegroups'])

		if task == 'create':
			self.data['default'] = ''

			result = self.connect.postoption(self.data)

			self.show.printOrders(result)


	def processingPolicy(self):
		self.data['ppapi'] = self.connect.getOption('ProcessingPolicy')

		self.show.printformat(self.data['ppapi'])
		#self.data['processingpolicy'] = self.processingpolicy.getAll(self.data['ppapi'])

		#self.show.printformat(self.data['processingpolicy'])


	def normalizationPolicy(self):
		self.data['normpackapi'] = self.connect.getOption('NormalizationPackage')
		self.data['normalizationpackage'] = self.normalizationpackage.getNames(self.data['normpackapi'])
		self.data['normpolapi'] = self.connect.getOption('NormalizationPolicy')

		self.data['normalizationpolicy'] = self.normalizationpolicy.getAll(self.data)

		self.show.printformat(self.data['normalizationpolicy'])


	def normalizationPackage(self):
		self.data['normpackapi'] = self.connect.getOption('NormalizationPackage')

		self.show.printformat(self.data['normpackapi'])


