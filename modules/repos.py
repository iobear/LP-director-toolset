#!/usr/bin/env python
#

class Repos:
	"""docstring for Repos"""

	def update(self, data):
		returndata = {}
		returndata['option'] = 'Repos'
		returndata['data'] = {}

		returndata['data']['hiddenrepopath'] = []

		hiddenrepopath = []

		default = {}
		for key, value in data['default']: # prepare default values from config.ini
			if key == 'retention':
				default[key] = int(value)
			else:
				default[key] = value

		#returndata['data']['hiddenrepopath'].append(tmpdict) #adding default values from config.ini

		repo_path = {}
		i = 0
		for tmpdata in data['userinput']: #checking user input

			keyvalue = tmpdata.split('=')

			if keyvalue[0].startswith( 'path' ) or keyvalue[0].startswith( 'retention' ):

				repo_path[keyvalue[0]] = keyvalue[1]

				if i == [1,3,5,7]:
					insert = i - 1
					returndata['data']['hiddenrepopath'][insert] = repo_path

				i += 1

			else:
				returndata['data'][keyvalue[0]] = keyvalue[1]


		print returndata




		raise SystemExit, 1



		returndata['userinput'] = ''

		#if returndata['data'].get('hiddenrepopath')[0]:


		return returndata
		raise SystemExit, 1


	def getAll(self, data):
		repolist = []

		j = ' ' #join delimiter
		for repo in data:
			rpathrow = []
			retentionrow = []
			rpath = repo['repopath']

			for rp in rpath:
				rpathrow.append(rp['path'])
				retentionrow.append(str(rp['retention']))

			repolist.append({'path':j.join(rpathrow),'retention':j.join(retentionrow),'id':repo['id'],'name':repo['name']})

		return repolist
