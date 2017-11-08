#!/usr/bin/env python

import requests
import json
from config import ApiConfig

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Connect:

	def __init__(self):
		self.apiconfig = ApiConfig()


	def update(self, parameters):
		kvdata = {} 
		data = {}
		ip = []
		devicegroup = []
		ntp_server = []

		if parameters.get('default'):
				kvdata.update(parameters['default']) #add default device values to post data

		for tmpdata in parameters['userinput']: #make dict of user input

			keyvalue = tmpdata.split('=')

			if keyvalue[0].startswith( 'ntp_server' ):
				ntp_server.append(keyvalue[1])
				kvdata['ntp_server'] = ntp_server

			else:
				kvdata[keyvalue[0]] = keyvalue[1]


		if parameters.get('data'):
			data['data'] = parameters['data']
		else:
			data['data'] = kvdata

		postdata = json.dumps(data)

		api_path = self.apiconfig.api_init_path + self.apiconfig.pool + '/' + self.apiconfig.logpoint_identifier + '/' + parameters['option']
		url = self.apiconfig.api_host + api_path

		headers = {'content-type': 'application/json', 'Authorization':'Bearer %s' %self.apiconfig.auth_token}

		if parameters.get('task') == 'delete':
			result = requests.delete(url, headers=headers, verify=False)
		elif parameters.get('task') == 'edit':
			result = requests.put(url, data=postdata, headers=headers, verify=False)
		else:
			result = requests.post(url, data=postdata, headers=headers, verify=False)

		result = self.errorCheck(result)

		return result


	def getMonitor(self, apipath):

		endpoint = self.apiconfig.host + '/' + apipath

		headers = {"Authorization":"Bearer %s" %self.apiconfig.auth_token}

		result = requests.get(endpoint,headers=headers,verify=False)

		result = self.errorCheck(result)

		return result


	def getOption(self, option):

		api_path = self.apiconfig.init_path + self.apiconfig.pool + '/' + self.apiconfig.logpoint_identifier + '/' + option
		endpoint = self.apiconfig.host + api_path

		headers = {"Authorization":"Bearer %s" %self.apiconfig.auth_token}

		result = requests.get(endpoint,headers=headers,verify=False)

		result = self.errorCheck(result)

		return result


	def errorCheck(self, result):
		message = {}
		message['error'] = 1
		passthrough = 0

		message['httpstatus'] = result.status_code
	
		jresult = result.json()

		if isinstance(jresult, list): # if list not dict
			passthrough = 1

		elif jresult.get('err'):
			message['message'] = jresult.get('err').get('message')

		elif jresult.get('payload'):
			message['message'] = jresult.get('payload').get('message')

		elif jresult.get('status') == 'Error':
			message['message'] = jresult.get('message')

		else:
			message['message'] = jresult
			message['error'] = 0

		if passthrough == 1:
			message = jresult

		elif message.get('error') == 1: #TODO should not exit here, but return in select format
			print
			print (json.dumps(jresult))
			print
			raise SystemExit, 1

		return message

