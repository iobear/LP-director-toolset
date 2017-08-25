#!/usr/bin/env python
#

class ProcessingPolicy:
	"""docstring for ProcessingPolicy"""

	def create(self, parameters):
		data = {}

		callapi = Connect('ProcessingPolicy')
		
		data['userinput'] = parameters
		data['default'] = ''
		result = callapi.postoption(data)

		print (result)

	def getNames(self, data):
		returndict = {}

		for devicegrps in data:
			returndict[devicegrps['id']] = devicegrps['policy_name']

		return returndict

	def getAll(self, data):

		return data
