#!/usr/bin/env python
#

import time
import json
from tabulate import tabulate
from orders import Orders

class Format:
	"""docstring for Printer"""

	def __init__(self, out, debug = 0):
		self.out = out
		self.debug = debug


	def printformat(self, printthis):

		if self.out == 'json':
			print (json.dumps(printthis))

		elif self.out == 'txt':

			print
			print (tabulate(printthis, headers="keys", tablefmt="pipe"))
			print
			

	def printOrders(self, result):
			orders = Orders()

			if self.debug == '1':
				print ('-- RESULT --')
				print (result)
				print ('-- Getting ORDER --')

			response = 0
			while response == 0:
				progress = orders.read(result['message']['message'])
				orderresult = progress.get('message')

				if self.debug == '1':
					print ('-- Raw result --')
					print (orderresult)

				response = len(orderresult.get('response'))
				time.sleep(1)

			self.printformat([orderresult.get('response')])


	def rotatePrint(self, printthis): #print dict vertical, instead of horizontal

		if self.out == 'json':
			print (json.dumps(printthis))

		elif self.out == 'txt':

			for item in printthis:
				for key, value in item.iteritems():
					print (' | ' + str(key) + ' = ' +  str(value))

			print
