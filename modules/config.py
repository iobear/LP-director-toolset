#!/usr/bin/env python
#
# by bnj@logpoint.com
#

import configparser

class ApiConfig:
	"""docstring for ApiConfig"""

	config = configparser.ConfigParser()
	config.read('config.ini')

	apihost = config['API']['apihost']
	auth_token = config['API']['auth_token']

	# TODO if LPID or POOL option not given:
	logpoint_identifier = config['LPID'][config['LPID']['default']]
	pool = config['POOL'][config['POOL']['default']]

	#Default device parameters
	defaultdeviceparameter = config.items( "DEVICE" )
	timezone = config['DEVICE']['timezone']
	integrity = config['DEVICE']['integrity']
	availability = config['DEVICE']['availability']
	confidentiality = config['DEVICE']['confidentiality']