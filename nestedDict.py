import pprint

allGuests = { 'Alice':{'apples': 5, 'pretzels':6},
	      'Bob':{'sandwiches':3,'apples':5},
	      'Carol':{'cups':4,'pretzels':3}}

#for keys,values in allGuests.items():
#	print("Key: %s Value: %s" %(keys,values))
def totalBrought(guests,item):
	numBrought = 0	
	for k, v in guests.items():
		numBrought = numBrought + v.get(item,0)
		return numBrought

print ("Number of items brought to the picnic...")
print ("%s apples" %totalBrought(allGuests,'apples'))
print ("%s pretzels" %totalBrought(allGuests,'pretzels'))
