#!/usr/bin/env python
#

class OpenDoor:
	"""docstring for OpenDoor"""

	def create(self, parameters):
		data = {}

		callapi = Connect('OpenDoor')
		
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
		if str(data) == '[{}]':
			data = [{'open door':'None created'}]

		return data
