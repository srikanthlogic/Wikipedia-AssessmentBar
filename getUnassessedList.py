from mwapi import MWApi
import sys

def QueryAPI(catname):

	params = {'action':'query','list':'categorymembers','format':'json','cmtitle':'Category:'+catname, 'cmprop':'title','cmnamespace':'1','cmlimit':'500'}

	api = MWApi('http://en.wikipedia.org')
	while True:
		data = api.get(params)
		for page in data['query']['categorymembers']:
			print page['title']
		if data.has_key('query-continue'):
			params['cmcontinue'] = data['query-continue']['categorymembers']['cmcontinue']
		else:
			break

if __name__ == "__main__":
	catname = sys.argv[1]
	QueryAPI(catname)
