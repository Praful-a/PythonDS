'''
12345
1234
123
12
1
'''
def pattern1(n):
	for row in range(n, 0, -1):
		for col in range(1, row+1):
			print(col, end="")
		print()

pattern1(5)