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
			print (printthis)

		elif self.out == 'txt':

			print
			print (tabulate(printthis, headers="keys", tablefmt="pipe"))
			print
			

	def printOrders(self, result):
			orders = Orders()

			if self.debug == '1':
				print ('RESULT:')
				print (result)
				print ('ORDERS:')
				print ('----')

			response = 0
			while response == 0:
				#print result['message']['message']
				progress = orders.read(result['message']['message'])
				orderresult = progress.get('message')

				if self.debug == '1':
					print ('DEBUG:')
					print (orderresult)

				print
				response = len(orderresult.get('response'))
				time.sleep(1)

			self.printformat([orderresult.get('response')])


	def rotatePrint(self, printthis):

		if self.out == 'json':
			print (printthis)

		elif self.out == 'txt':

			print 
			for item in printthis:
				for key, value in item.iteritems():
					print ' | ' + str(key) + ' = ' +  str(value)

			print
