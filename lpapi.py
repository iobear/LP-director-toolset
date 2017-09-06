#!/usr/bin/env python
#

from modules.main import API

import argparse
import json

api = API('txt', '0', '')

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--lpid', default=api.config.logpoint_identifier, help='logpoint server identifier from config.ini')
parser.add_argument('--pool', default=api.config.pool, help='pool identifier from config.ini')
parser.add_argument('task', default='', choices=['get', 'create', 'edit', 'delete', 'restart'], help='update or get information')
parser.add_argument('--parameter', '-p', default='', nargs='*', help='parameters for create, edit, update')
parser.add_argument('option', choices=['system', 'device', 'devicegroup', 'repo', 'syslogcollect', 'opendoor', 'processpol', 'normpol', 'routepol', 'normpack', 'ntp', 'syscol', 'od', 'ppo', 'npo', 'npa', 'dev', 'dg', 'rpo'], help='what part do you what work with?')
parser.add_argument('--output', '-o', default='txt', choices=['json', 'txt'], help='output format')
parser.add_argument('--file', '-f', default='', help='file for batch import')
parser.add_argument('--debug', default=0, choices=['0', '1'], help='enable API debug')


args = parser.parse_args()
api = API(args.output, args.task, args.debug, args.parameter, args.file)

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


