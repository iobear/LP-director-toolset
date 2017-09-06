#!/usr/bin/env python
#

class SyslogCollector:
	"""docstring for SyslogCollector"""

	def update(self, parameters):
		"""docstring for changing a SyslogCollector"""

		returndata = {}
		data = {}
		returndata['task'] = parameters['task']
		returndata['option'] = parameters['option']

		data.update(parameters['default']) #add default device values to post data

		if parameters.get('data'):
			parameters['userinput'] = ''
			for line in parameters['data']['data']: #add data to defaults from config.ini
				data[line] = parameters['data']['data'][line]

		for tmpdata in parameters['userinput']: #add user input to data dict

			keyvalue = tmpdata.split('=')

			data[keyvalue[0]] = keyvalue[1]

		data['processpolicy'] = self.findId(parameters['processingpolicy'], data['processpolicy'])
		data['device_id'] = self.findId(parameters['devices'], data['name'])

		returndata['data'] = data
		returndata['userinput'] = ''

		return returndata



	def findId(self, devdict, devname):
		devid = '00'

		for devdetail in devdict:
			if devdict[devdetail] == devname:
				devid = str(devdetail)

		return devid

