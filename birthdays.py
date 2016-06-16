birthdays = {'alice': 'apr 1','bob': 'Dec 12','Carol':'Mar 4'}

while True:
	print ('Enter a name: (blank to quit)')
	name = raw_input()
	if name == '':
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of '+ name)
	else:
		print "no info for" + name
		print "when is the birthday?"
		bday = raw_input("> ")
		birthdays[name] = bday
		print "bday updated"
		print birthdays
