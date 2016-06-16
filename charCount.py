msg = 'it was a c a gslkds in paradise'
count = {}

for char in msg:
	count.setdefault(char,0)
	count[char] += 1
print count
