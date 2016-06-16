#!/usr/bin/python

a = []
b = ['aa','bb','cc','dd',]

print "a is %s" %a
print "b is %s" %b[:2]

for i in range(10):
	a.append(i)

print "a is %s" %a

c = a + b
print "c is %s" %c

d = a * 3
print "d is %s" %d

for i in a,b,c:
	print i

print "c before deletion: %s" %c
for i in range(1):
	c.remove(i)
print "c after deletion: %s" %c

c.pop()
print c
