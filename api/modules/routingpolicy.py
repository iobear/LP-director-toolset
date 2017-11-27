#!/usr/bin/env python
#

class RoutingPolicy:
	"""docstring for RoutingPolicy"""

	def update(self, parameters):
		"""docstring for routepol update"""

		returndata = {}
		data = {}
		returndata['task'] = parameters['task']
		returndata['option'] = parameters['option']

		for tmpdata in parameters['userinput']: #add user input to data dict

			keyvalue = tmpdata.split('=')

			if keyvalue[0] == 'policy_name' and parameters['task'] != 'create':
				rpid = self.findId(parameters['rpapi'], keyvalue[1]) #resolve policy_name name to id
				returndata['option'] = parameters['option'] + '/' + str(rpid)

				if parameters['task'] == 'edit':
					data[keyvalue[0]] = keyvalue[1]
			else:
				data[keyvalue[0]] = keyvalue[1]


		data['routing_criteria'] = []

		returndata['data'] = data
		returndata['userinput'] = ''

		return returndata


	def findId(self, devdict, devname):
		devid = '00'

		for devdetail in devdict:
			if devdetail['policy_name'] == devname:
					devid = str(devdetail['id'])

		return devid

