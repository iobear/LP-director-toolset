#!/usr/bin/env python
#

class NormalizationPackage:
	"""docstring for NormalizationPackage"""

	def getNames(self, data):
		returndict = {}

		for stuff in data:
			returndict[stuff['id']] = stuff['name']

		return returndict


	def getAll(self, data):

		return data
