msg = 'it was a warm and sunny day in paradise'

#{'a': 7, ' ': 8, 'e': 1, 'd': 3, 'i': 3, 'm': 1, 'n': 4, 'p': 1, 's': 3, 'r': 2, 'u': 1, 't': 1, 'w': 2, 'y': 2}

count = {}


for i in msg:
	count.setdefault(i,0)
	count[i] = count[i] + 1
	print count
