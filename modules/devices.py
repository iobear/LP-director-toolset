#!/usr/bin/env python

class Devices:
	"""docstring for Devices"""

	def update(self, parameters):
		"""docstring for changing a device"""

		returndata = {}
		data = {}
		ip = []
		devicegroup = []
		returndata['http'] = 'POST'
		returndata['option'] = parameters['option']

		data.update(parameters['default']) #add default device values to post data

		for tmpdata in parameters['userinput']: #add user input to data dict

			keyvalue = tmpdata.split('=')

			if keyvalue[0].startswith( 'ip' ):
				ip.append(keyvalue[1])
				data['ip'] = ip

			elif keyvalue[0].startswith( 'devicegroup' ):

				for devgrp in parameters['devicegroups']: #find id to devicegroup
					if parameters['devicegroups'][devgrp] == keyvalue[1]:
						devgrpid = devgrp

				devicegroup.append(devgrpid)
				devgrpid = ''
				data['devicegroup'] = devicegroup
			else:
				data[keyvalue[0]] = keyvalue[1]

		if parameters['task'] == 'edit' or parameters['task'] == 'delete':
			returndata['http'] = 'put'
			if parameters['task'] == 'delete':
				returndata['http'] = 'delete'

			if data.get('id'):
				devid = data['id']
				data.pop('id', None)
			else:
				devid = self.findDeviceId(parameters['devices'], data['name'])

			returndata['option'] = parameters['option'] + '/' + str(devid)

		returndata['data'] = data
		returndata['userinput'] = ''

		return returndata


	def findDeviceId(self, devdict, devname):
		devid = ''

		for devdetail in devdict:
			if devdict[devdetail] == devname:
				devid = str(devdetail)

		return devid


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


