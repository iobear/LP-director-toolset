#!/usr/bin/env python

class Devices:
	"""docstring for Devices"""

	def update(self, parameters):
		"""docstring for changing a device"""

		returndata = {}
		data = {}
		ip = []
		devicegroup = []
		returndata['task'] = parameters['task']
		returndata['option'] = parameters['option']

		data.update(parameters['default']) #add default device values to post data

		if parameters.get('data'):
			parameters['userinput'] = ''
			for line in parameters['data']['data']: #add data to defaults from config.ini
				data[line] = parameters['data']['data'][line]

		for tmpdata in parameters['userinput']: #add user input to data dict

			keyvalue = tmpdata.split('=')

			if keyvalue[0].startswith( 'ip' ):
				ip.append(keyvalue[1])
				data['ip'] = ip

			elif keyvalue[0].startswith( 'devicegroup' ):

				devicegroup.append(keyvalue[1])
				data['devicegroup'] = devicegroup
			else:
				data[keyvalue[0]] = keyvalue[1]

		if parameters['task'] == 'edit' or parameters['task'] == 'delete':

			if data.get('id'):
				devid = data['id']
				data.pop('id', None)
			else:
				devid = self.findDeviceId(parameters['devices'], data['name'])

			returndata['option'] = parameters['option'] + '/' + str(devid)

		for line in data: #find dev grp id's
			if line == 'devicegroup':
				for i, grpname in enumerate(data[line]):
					devgrpid = self.findDeviceId(parameters['devicegroups'], grpname)
					data['devicegroup'][i] = devgrpid
					devgrpid = ''

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


