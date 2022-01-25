def toh(n, t1d, t2d, t3d):
	if (n == 0):
		return   
	toh(n - 1, t1d, t3d, t2d)
	print(n, "[", t1d, "->",t2d, "]")
	toh(n - 1, t3d, t2d, t1d)

toh(3, 'A', 'B', 'C')