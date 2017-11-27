#!/usr/bin/env python
#

class NormalizationPolicy:
	"""docstring for NormalizationPolicy"""


	def getNames(self, data):
		returndict = {}

		for stuff in data:
			returndict[stuff['id']] = stuff['name']

		return returndict


	def getAll(self, data):

		thelist = []
		j = '; ' #join delimiter

		for np in data['normpolapi']:

			normpack = []

			for ids in np['normalization_packages']: #resolve norm pack id's
				
				normpack.append(data['normalizationpackage'][ids])

			signatures = len(np['selected_signatures'])
			thelist.append({'name':np['name'], 'id':np['id'], 'active':np['active'], 'signatures':signatures, 'normalization_packages':j.join(normpack)})

		return thelist


	def update(self, parameters):
		"""docstring for normpol update"""

		returndata = {}
		data = {}
		returndata['task'] = parameters['task']
		returndata['option'] = parameters['option']

		for tmpdata in parameters['userinput']: #add user input to data dict

			keyvalue = tmpdata.split('=')

			if keyvalue[0] == 'name' and returndata['task'] != 'create':
				device_id = self.findId(parameters['normpolapi'], keyvalue[1]) #resolve NormalizationPolicy name to id
				returndata['option'] = parameters['option'] + '/' + str(device_id)
			else:
				data[keyvalue[0]] = keyvalue[1]

		returndata['data'] = data
		returndata['userinput'] = ''

		return returndata


	def findId(self, devdict, devname):
		devid = '00'

		for devdetail in devdict:
			if devdetail['name'] == devname:
					devid = str(devdetail['id'])

		return devid

