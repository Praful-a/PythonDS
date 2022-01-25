def pzz(n):
	if n == 0:
		return 
	print('Pre', n)
	pzz(n - 1)
	print('In', n)
	pzz(n - 1)
	print('Post', n)

pzz(2)