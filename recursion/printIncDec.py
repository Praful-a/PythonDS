def printIncDec(n):
	if (n == 0):
		return   
	print(n) 
	printIncDec(n - 1)
	print(n)

n = 5
printIncDec(n)