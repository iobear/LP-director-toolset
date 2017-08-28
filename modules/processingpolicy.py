#!/usr/bin/env python
#

class ProcessingPolicy:
	"""docstring for ProcessingPolicy"""

	# def create(self, parameters):
	# 	data = {}

	# 	callapi = Connect('ProcessingPolicy')
		
	# 	data['userinput'] = parameters
	# 	data['default'] = ''
	# 	result = callapi.postoption(data)

	# 	print (result)

	def getNamesOnly(self, data):
		returndict = {}

		for devicegrps in data:
			returndict[devicegrps['id']] = devicegrps['policy_name']

		return returndict

	def listAll(self, data):

		#translate routing_policy id to name
		ppolist = []
		for ppo in data['ppapi']:
			ppo['routing_policy'] = data.get('routing_policy').get(ppo.get('routing_policy'))
			ppolist.append(ppo)

		return ppolist
