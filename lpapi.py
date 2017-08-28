#!/usr/bin/env python
#

from modules.main import API

import argparse
import json

api = API('txt', '0')

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--lpid', default=api.config.logpoint_identifier, help='logpoint server identifier from config.ini')
parser.add_argument('--pool', default=api.config.pool, help='pool identifier from config.ini')
parser.add_argument('task', default='', choices=['get', 'create', 'edit', 'restart'], help='update or get information')
parser.add_argument('--parameter', default='', nargs='*', help='parameters for create, edit, update')
parser.add_argument('option', choices=['system', 'device', 'devicegroup', 'repo', 'opendoor', 'processpol', 'normpol', 'routepol', 'normpack', 'ntp', 'od', 'ppo', 'npo', 'npa', 'dev', 'dg', 'rpo'], help='what part do you what work with?')
parser.add_argument('--output', default='txt', choices=['json', 'jsonraw', 'txt'], help='output format')
parser.add_argument('--debug', default=0, choices=['0', '1'], help='enable API debug')


args = parser.parse_args()
api = API(args.output, args.debug)

if args.option == 'opendoor' or args.option == 'od':
	if args.task == 'get':
		api.openDoor(args.task)
	if args.task == 'create':
		api.openDoor(args.task, args.parameter)

if args.option == 'repo':
	api.repos()

if args.option == 'system':
	if args.task == 'get':
		api.systemSettings(args.task)
	if args.task == 'create':
		api.systemSettings(args.task, args.parameter)

if args.option == 'ntp':
	api.systemSettingsNTP(args.task, args.parameter)

if args.option == 'processpol' or args.option == 'ppo':
	if args.task == 'get':
		api.processingPolicy(args.task)

if args.option == 'normpol' or args.option == 'npo':
	if args.task == 'get':
		api.normalizationPolicy(args.task)

if args.option == 'normpack' or args.option == 'npa':
	if args.task == 'get':
		api.normalizationPackage(args.task)

if args.option == 'routepol' or args.option == 'rpo':
	if args.task == 'get':
		api.routingPolicy(args.task)

if args.option == 'device' or args.option == 'dev':

	if args.task == 'get':
		api.devices(args.task)

	if args.task == 'create':

		if args.parameter:
			api.devices(args.task, args.parameter)

		else:
			print ('missing --parameter name=<device name> devicegroup=<devicegroup> ip=<ip>, ip2=<ip>, ip3=...')


if args.option == 'devicegroup' or args.option == 'dg':

	if args.task == 'get':
		api.deviceGroups(args.task)

	if args.task == 'create':
		if args.parameter:
			api.deviceGroups(args.task, args.parameter)
		else:
			print ('missing --parameter name=<group name> description=<description>')


