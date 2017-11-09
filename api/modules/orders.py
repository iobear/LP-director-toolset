#!/usr/bin/env python
#

from apiconnect import Connect

class Orders():
	"""docstring for orders"""

	def __init__(self):
#		self.id = id
		self.callapi = Connect()
		self.done = {}

	def read(self, id):
		result = self.callapi.getMonitor(id)

		return result