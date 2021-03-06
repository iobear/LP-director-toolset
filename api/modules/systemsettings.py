#!/usr/bin/env python
#

class SystemSettings:
	"""docstring for SystemSettings"""

	def create(self, parameters):
		data = {}

		callapi = Connect('SystemSettingsGeneral')
		
		data['userinput'] = parameters
		data['default'] = ''
		result = callapi.postoption(data)

		print (result)


	def getNames(self, data):
		returndict = {}

		for stuff in data:
			returndict[stuff['id']] = stuff['name']

		return returndict


	def getAll(self, data):

		return data
