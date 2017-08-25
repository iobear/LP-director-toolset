#!/usr/bin/env python
#

class NormalizationPackage:
	"""docstring for NormalizationPackage"""

	def create(self, parameters):
		data = {}

		callapi = Connect('NormalizationPackage')
		
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
