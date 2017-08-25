#!/usr/bin/env python
#

class SystemSettingsNTP:
	"""docstring for SystemSettingsNTP"""

	def create(self, parameters):
		data = {}

		callapi = Connect('SystemSettingsNTP')
		
		data['userinput'] = parameters
		data['default'] = ''
		result = callapi.postoption(data)

		print (result)


	def getAll(self, data):

		return data
