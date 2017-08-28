#!/usr/bin/env python

import time

class Devices:
	"""docstring for Devices"""


	def create(self, parameters):
		"""docstring for create device"""

		data = {}


	def listall(self, blob):

		data = blob['deviceapi']
		blob['devicelist'] = []

		for i, devices in enumerate(data):
			tmpdict = {}

			tmpdict['id'] = devices['id']
			tmpdict['name'] = devices['name']
			tmpdict['active'] = devices['active']
			
			ips = data[i]['ip']

			j = ' ' #join delimiter
			iprow = []
			for ip in ips:
				iprow.append(ip)

			tmpdict['ip'] = j.join(iprow)

			devicegroupss = data[i]['device_groups']
			devgrprow = []

			for dev in devicegroupss:
				devgrprow.append(blob['devicegroups'][dev])

			tmpdict['devicegroup'] = j.join(devgrprow)

			processpolicys = data[i]['col_apps']
			processprow = []
			for pp in processpolicys:
				processprow.append(pp['processpolicy'])

			newprocessprow = list(set(processprow)) #make list uniq
			processprow = []
			for pp in newprocessprow:
				processprow.append(blob['processingpolicy'][pp])

			tmpdict['processpolicy'] = j.join(processprow)

			blob['devicelist'].append(tmpdict)

		return blob


