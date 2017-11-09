#!/usr/bin/env python
#

class DeviceGroups:
	"""docstring for DeviceGroups"""

	def getNamesOnly(self, data):
		returndict = {}

		for devicegrps in data:
			returndict[devicegrps['id']] = devicegrps['name']

		return returndict


	def getAll(self, data):

		grouplist = []

		for i,devicegrps in enumerate(data):
			tmpdict = {}

			tmpdict['name'] = devicegrps['name']
			tmpdict['desc'] = devicegrps['description']
			tmpdict['id'] = devicegrps['id']
			tmpdict['active'] = devicegrps['active']
			tmpdict['count'] = len(devicegrps['devices'])

			grouplist.append(tmpdict)

		#listsorted = sorted(grouplist, key=lambda count: count[0], reverse=True) #order by device count
		return grouplist