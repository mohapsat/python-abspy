#!/usr/bin/python

# tuple are immutable lists, whose values cannot be changed

tup1 = (1,2,3)
try:
	tup1.pop()
except AttributeError:
	print "'tuple' object has no attribute 'pop':" + "Please pop from a list"
	
print tup1 

tup2 = tup1 * 3
print "lenght: %d Values: %s" %(len(tup2),tup2)

tup3 = list(tup2)
print tup3
tup4 = tuple('Hello')
print tup4

x = 'o' not in tup4
print x

tup3.sort(reverse=True)
print tup3


#tup3.sort(reverse=True)
#print "tup3 reverse sorted" tup3


for i in tup1:
	print "Value at %d is %s" %(tup1.index(i),i)

for i in tup4:
	print "******* " + i +" ********"
