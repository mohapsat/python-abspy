#! python 3

import requests
import sys
import json
import pprint

if len(sys.argv) < 2:
	print('Need search string for duckduckgo api to work..')
	sys.exit()

url = '+'.join(sys.argv[1:])

#http://api.duckduckgo.com/?q=valley+forge+national+park&format=json&pretty=1
apiurl = 'http://api.duckduckgo.com/?q=%s&format=json&pretty=1'%url

print apiurl

response = requests.get(apiurl)
response.raise_for_status()

data = json.loads(response.text)

print(data)
#pprint.pprint(data)

#print "-" * 50
#print "Related Data"
#print "-" * 50

#reltopics = data['RelatedTopics']


