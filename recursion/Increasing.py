def printIncreasing(n):
	if (n == 0):
		return   
	printIncreasing(n - 1)
	print(n)

n = 5
printIncreasing(n)