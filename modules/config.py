#!/usr/bin/env python
#

import configparser

class ApiConfig:
	"""docstring for ApiConfig"""

	config = configparser.ConfigParser()
	config.read('config.ini')

	host = config['API']['host']
	init_path = config['API']['init_path']
	auth_token = config['API']['auth_token']

	logpoint_identifier = config['LPID'][config['LPID']['default']]
	pool = config['POOL'][config['POOL']['default']]

	default_device_parameters = config.items( "DEVICE" )
	timezone = config['DEVICE']['timezone']
	integrity = config['DEVICE']['integrity']
	availability = config['DEVICE']['availability']
	confidentiality = config['DEVICE']['confidentiality']

	default_repo_parameters = config.items( "REPO" )

	default_collector_parameters = config.items( "SYSLOGCOLLECTOR" )