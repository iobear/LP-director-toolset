#!/usr/bin/env python
#

class ProcessingPolicy:
	"""docstring for ProcessingPolicy"""

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


	def update(self, parameters):
		"""docstring for normpol update"""

		returndata = {}
		data = {}
		returndata['task'] = parameters['task']
		returndata['option'] = parameters['option']

		for tmpdata in parameters['userinput']: #add user input to data dict

			keyvalue = tmpdata.split('=')

			if keyvalue[0] == 'policy_name' and returndata['task'] != 'create':

				policy_names = self.getNamesOnly(parameters['ppapi'])
				device_id = self.findId(policy_names, keyvalue[1]) #resolve id
				returndata['option'] = parameters['option'] + '/' + str(device_id)

			if keyvalue[0] == 'routing_policy' or keyvalue[0] == 'enrich_policy':
				device_id = self.findId(parameters[keyvalue[0]], keyvalue[1]) #resolve id
				data[keyvalue[0]] = device_id

			else:
				data[keyvalue[0]] = keyvalue[1]

		returndata['data'] = data
		returndata['userinput'] = ''

		return returndata


	def findId(self, devdict, devname):
		devid = 'None'

		for devdetail in devdict:
			if devdict[devdetail] == devname:
				devid = str(devdetail)

		return devid
