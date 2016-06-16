import os
import sys
import pprint

pb = {'bob':{'age':10,'Grade':'K','Gender':'M'},
	'Rob':{'age':15,'Grade':'1','Gender':'F'}}

#print pb['name']

pprint.pprint(pb)
print '_'*20

for keys, values in pb.items():
	print ("Key = %s, Value = %s, Value.Age = %s Value.Grade = %s Value.Gender = %s"%(keys, values, values.get('age',0), values.get('Grade',0), values.get('Gender',0)))
