#!/usr/bin/env python

import requests
import json
from config import ApiConfig

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Connect:

	def __init__(self):
		self.apiconfig = ApiConfig()

	def postoption(self, parameters):

		kvdata = {} 
		data = {}
		ip = []
		devicegroup = []
		ntp_server = []

		kvdata.update(parameters['default']) #add default device values to post data

		for tmpdata in parameters['userinput']: #make dict of user input

			keyvalue = tmpdata.split('=')

			if keyvalue[0].startswith( 'ip' ):
				ip.append(keyvalue[1])
				kvdata['ip'] = ip

			elif keyvalue[0].startswith( 'devicegroup' ):
				devicegroup.append(keyvalue[1])
				kvdata['devicegroup'] = devicegroup

			elif keyvalue[0].startswith( 'ntp_server' ):
				ntp_server.append(keyvalue[1])
				kvdata['ntp_server'] = ntp_server

			else:
				kvdata[keyvalue[0]] = keyvalue[1]

		data['data'] = kvdata

		postdata = json.dumps(data)
	
		apipath = '/configapi/v1/' + self.apiconfig.pool + '/' + self.apiconfig.logpoint_identifier + '/' + parameters['option']
		url = 'https://' + self.apiconfig.apihost + apipath

		headers = {'content-type': 'application/json', 'Authorization':'Bearer %s' %self.apiconfig.auth_token}

		result = requests.post(url, data=postdata, headers=headers, verify=False)

		result = self.errorCheck(result)

		return result


	def getMonitor(self, apipath):

		endpoint = 'https://' + self.apiconfig.apihost + '/' + apipath

		headers = {"Authorization":"Bearer %s" %self.apiconfig.auth_token}

		result = requests.get(endpoint,headers=headers,verify=False)

		result = self.errorCheck(result)

		return result


	def getOption(self, option):

		apipath = '/configapi/v1/' + self.apiconfig.pool + '/' + self.apiconfig.logpoint_identifier + '/' + option
		endpoint = 'https://' + self.apiconfig.apihost + apipath

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
			print (jresult)
			print
			raise SystemExit, 1

		return message

