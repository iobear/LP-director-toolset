#!/usr/bin/env python
#

class Repos:
	"""docstring for Repos"""

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
