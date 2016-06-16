import json
import pprint
import sys
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo";
response = requests.get(url)
response.raise_for_status()

nasaData = json.loads(response.text)

#pprint.pprint(nasaData)

#pynasaData = json.dumps(nasaData)

#pprint.pprint(pynasaData)

#for k,v in nasaData.iteritems():
#	print ("KEY: %s \t\tVALUE: %s"%(k,v))
print '-' * 50
print("Title: %s"%(nasaData['title']))
print '-'*50
print('\nExplanation: %s'%(nasaData['explanation']))
