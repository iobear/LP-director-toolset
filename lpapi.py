#!/usr/bin/env python
#

from modules.main import API
from modules.config import ApiConfig

import argparse
import json

#config = ApiConfig()

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--lphost', '-lph', help='logpoint server name from config.ini')
parser.add_argument('--pool', help='pool name from config.ini')
parser.add_argument('task', default='', choices=['get', 'create', 'edit', 'delete', 'restart'], help='update or get information')
parser.add_argument('--parameter', '-p', default='', nargs='*', help='parameters for create, edit, update')
parser.add_argument('option', choices=['system', 'device', 'devicegroup', 'repo', 'syslogcollect', 'opendoor', 'processpol', 'normpol', 'routepol', 'normpack', 'ntp', 'syscol', 'od', 'ppo', 'npo', 'npa', 'dev', 'dg', 'rpo','dlp', 'distributedlogpoint'], help='what part do you what work with?')
parser.add_argument('--output', '-o', default='txt', choices=['json', 'txt'], help='output format')
parser.add_argument('--file', '-f', default='', help='file for batch import')
parser.add_argument('--debug', default=0, choices=['0', '1'], help='enable API debug')


args = parser.parse_args()
api = API(args)

if args.option == 'opendoor' or args.option == 'od':
	api.openDoor()

if args.option == 'repo':
	api.repos()

if args.option == 'syscol' or args.option == 'syslogcollect':
	api.syslogcollectors()

if args.option == 'system':
	api.systemSettings()

if args.option == 'ntp':
	api.systemSettingsNTP()

if args.option == 'processpol' or args.option == 'ppo':
	api.processingPolicy()

if args.option == 'normpol' or args.option == 'npo':
	api.normalizationPolicy()

if args.option == 'normpack' or args.option == 'npa':
	api.normalizationPackage()

if args.option == 'routepol' or args.option == 'rpo':
	api.routingPolicy()

if args.option == 'device' or args.option == 'dev':
	api.devices()

if args.option == 'devicegroup' or args.option == 'dg':
	api.deviceGroups()

if args.option == 'distributedlogpoint' or args.option == 'dlp':
	api.distributedLogpoints()
