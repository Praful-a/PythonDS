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
# def pattern3(n):
# 	for row in range(n, 0, -1):
# 		for col in range(row, 0, -1):
# 			print(col, end="")
# 		print()

# pattern3(5)

'''
54321
5432
543
54
5
'''
# def pattern4(n):
# 	for row in range(1, n+1):
# 		for col in range(n, row-1, -1):
# 			print(col, end="")
# 		print()

# pattern4(5)

'''
1
12
123
1234
12345
'''
# def pattern5(n):
# 	for row in range(1, n+1):
# 		for col in range(1, row+1):
# 			print(col, end="")
# 		print()

# pattern5(5)

'''
5
45
345
2345
12345
'''
# def pattern6(n):
# 	for row in range(n, 0, -1):
# 		for col in range(row, n+1):
# 			print(col, end="")
# 		print()

# pattern6(5)

'''
1
21
321
4321
54321
'''
# def pattern7(n):
# 	for row in range(1, n+1):
# 		for col in range(row, 0, -1):
# 			print(col, end="")
# 		print()

# pattern7(5)

'''
5
54
543
5432
54321
'''
# def pattern8(n):
# 	for row in range(n, 0, -1):
# 		for col in range(n, row - 1, -1):
# 			print(col, end="")
# 		print()

# pattern8(5)

'''
1
22
333
4444
55555
'''
# def pattern9(n):
# 	for row in range(1, n+1):
# 		for col in range(row):
# 			print(row, end="")
# 		print()

# pattern9(5)

'''
5
44
333
2222
11111
'''
# def pattern10(n):
# 	for row in range(n, 0, -1):
# 		for col in range(n, row-1, -1):
# 			print(row, end="")
# 		print()

# pattern10(5)

'''
55555
4444
333
22
1
'''
# def pattern11(n):
# 	for row in range(n, 0, -1):
# 		for col in range(row):
# 			print(row, end="")
# 		print()

# pattern11(5)

'''
11111
2222
333
44
5
'''
# def pattern12(n):
# 	for row in range(1, n+1):
# 		for col in range(n, row-1, -1):
# 			print(row, end="")
# 		print()

# pattern12(5)

'''
12345
4321
123
21
1
'''
# def pattern13(n):
# 	for row in range(n, 0, -1):
# 		num = 1 if(row % 2 == 1) else row
# 		for col in range(1, row + 1):
# 			print(num, end="")
# 			if (row % 2 == 1):
# 				num += 1
# 			else:
# 				num -= 1
# 		print()

# pattern13(5)


'''
1234567
12345
123
1
'''
# def pattern14(n):
# 	for row in range(n, 0, -2):
# 		for col in range(1, row + 1):
# 			print(col, end="")
# 		print()

# pattern14(7)

'''
1
01
101
0101
'''
def pattern15(n):
	for row in range(1, n):
		for col in range(row, 0, -1):
			print(col%2, end="")
		print()

pattern15(5)