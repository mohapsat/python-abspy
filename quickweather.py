import sys
import json
import requests
import pprint

#!python 3

# read the requested location from the cmmand line
# download json weather data from openweathermap.org
# converts the json to python data sructure

#pseudocode
# join sys.argv to get the location
# call requests.get() to the weather data
# call json.loads to conver to python data structure
# print weather forecast

#if len(sys.argv) > 1:
#	print sys.argv[1]
#else:
#	print sys.argv[0]+" need an arg"

if len(sys.argv) < 2:
	print ('usage: python ' +sys.argv[0] + ' location')
	sys.exit()

location = ' '.join(sys.argv[1:])

print location

# TODO:download json data from openweathermap.org

url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

response = requests.get(url)
response.raise_for_status()

# TODO:Load JSON to py variable

weatherData = json.loads(response.text)

pprint.pprint(weatherData)

#print weather descriptions



