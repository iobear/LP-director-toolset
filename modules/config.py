#!/usr/bin/env python
#

import configparser

class ApiConfig:
	"""docstring for ApiConfig"""

	config = configparser.ConfigParser()
	config.read('config.ini')

	apihost = config['API']['apihost']
	auth_token = config['API']['auth_token']

	logpoint_identifier = config['LPID'][config['LPID']['default']]
	pool = config['POOL'][config['POOL']['default']]

	#Default device parameters
	defaultdeviceparameter = config.items( "DEVICE" )
	timezone = config['DEVICE']['timezone']
	integrity = config['DEVICE']['integrity']
	availability = config['DEVICE']['availability']
	confidentiality = config['DEVICE']['confidentiality']