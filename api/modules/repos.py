#!/usr/bin/env python
#

class Repos:
	"""docstring for Repos"""

	def update(self, data):
		'''
		udating repos
		Had a bit of trouble with this one, should be possible to write it cleaner.
		'''

		#build datastructure
		returndata = {}
		returndata['task'] = data['task']
		returndata['option'] = 'Repos'
		returndata['userinput'] = ''
		returndata['data'] = {}
		returndata['data']['hiddenrepopath'] = []
		repo_path = {}

		for key, value in data['default']: # prepare default values from config.ini
			if key == 'retention':
				repo_path[key] = int(value)
			else:
				repo_path[key] = value

		i = 0
		for tmpdata in data['userinput']: #checking user input

			keyvalue = tmpdata.split('=')

			if keyvalue[0].startswith( 'path' ) or keyvalue[0].startswith( 'retention' ): #creating hiddenrepopath

				if keyvalue[0] == 'retention':
					repo_path[keyvalue[0]] = int(keyvalue[1])
				else:
					repo_path[keyvalue[0]] = keyvalue[1]

				if i in [1,3,5,7]: #if we have a path/retention pair - insert
					returndata['data']['hiddenrepopath'].append(repo_path)
					repo_path = {}

				i += 1

			elif keyvalue[0] == 'id': #check if edit, not create
				returndata['option'] = 'Repos/' + str(keyvalue[1])

			else:
				returndata['data'][keyvalue[0]] = keyvalue[1]

		if not returndata['data']['hiddenrepopath']:
			returndata['data']['hiddenrepopath'].append(repo_path)

		return returndata


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
