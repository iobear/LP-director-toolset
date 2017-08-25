#!/usr/bin/env python
#

class NormalizationPolicy:
	"""docstring for NormalizationPolicy"""

	def create(self, parameters):
		data = {}

		callapi = Connect('NormalizationPolicy')
		
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

		thelist = []
		j = '; ' #join delimiter

		for np in data['normpolapi']:

			normpack = []

			for ids in np['normalization_packages']: #resolve norm pack id's
				
				normpack.append(data['normalizationpackage'][ids])

			signatures = len(np['selected_signatures'])
			thelist.append({'name':np['name'], 'id':np['id'], 'active':np['active'], 'signatures':signatures, 'normalization_packages':j.join(normpack)})

		return thelist
