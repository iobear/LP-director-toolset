#!/usr/bin/env python

import requests
import json
from config import ApiConfig

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Connect:

	def __init__(self, lphost = ''):
		self.config = ApiConfig()

		if not lphost:
			lphost = self.config.lpid_host.get('default')

		self.lpid = self.config.lpid_host.get(lphost)

		if not self.lpid:
			print
			print ('{"status": "error host not found in config.ini"}')
			print
			raise SystemExit, 1


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
				if keyvalue[1].isdigit():
					keyvalue[1] = int(keyvalue[1])

				kvdata[keyvalue[0]] = keyvalue[1]


		if parameters.get('data'):
			data['data'] = parameters['data']
		else:
			data['data'] = kvdata

		if parameters.get('task') == 'activate':
			parameters['option'] = parameters['option'] + '/' + data['data']['id'] + '/activate'
			data['data'] = {}

		postdata = json.dumps(data)

		api_path = self.config.init_path + self.config.pool + '/' + self.lpid + '/' + parameters['option']
		# Debug
		# print ('Api path')
		# print api_path

		url = self.config.host + api_path

		headers = {'content-type': 'application/json', 'Authorization':'Bearer %s' %self.config.auth_token}

		if parameters.get('task') == 'delete':
			result = requests.delete(url, headers=headers, verify=False)
		elif parameters.get('task') == 'edit':
			result = requests.put(url, data=postdata, headers=headers, verify=False)
		else:
			# Debug
			# print ('Post data:')
			# print (postdata)
			result = requests.post(url, data=postdata, headers=headers, verify=False)
			# print ('Result order:')

		result = self.errorCheck(result)

		return result


	def getMonitor(self, apipath):

		endpoint = self.config.host + '/' + apipath

		headers = {"Authorization":"Bearer %s" %self.config.auth_token}

		result = requests.get(endpoint,headers=headers,verify=False)

		result = self.errorCheck(result)

		return result


	def getOption(self, option):

		api_path = self.config.init_path + self.config.pool + '/' + self.lpid + '/' + option
		endpoint = self.config.host + api_path

		headers = {"Authorization":"Bearer %s" %self.config.auth_token}

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

