spam = ['apples', 'bananas', 'tofu', 'cats']

def fn(l):
#	l.insert(len(l)-1,'and')
	l[len(l)-1]='and '+l[len(l)-1]
	for i in l:
		print i+',' 

fn(spam)
