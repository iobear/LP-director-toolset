#!/usr/bin/env python

import json
from apiconnect import Connect

class deviceGroups(object):
	"""docstring for deviceGroups"""

	def __init__(self):
		self.callapi = Connect()
#		pass

	def get(self, data):
		result = self.callapi.getoption('DeviceGroups/%s' %data)

		return str(result['description'])
