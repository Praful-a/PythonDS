'''
12345
1234
123
12
1
'''
# def pattern1(n):
# 	for row in range(n, 0, -1):
# 		for col in range(1, row+1):
# 			print(col, end="")
# 		print()

# pattern1(5)

'''
12345
2345
345
45
5
'''
# def pattern2(n):
# 	for row in range(1, n+1):
# 		for col in range(row, n+1):
# 			print(col, end="")
# 		print()

# pattern2(5)

'''
54321
4321
321
21
1
'''

def pattern3(n):
	for row in range(n, 0, -1):
		for col in range(row, 0, -1):
			print(col, end="")
		print()

pattern3(5)