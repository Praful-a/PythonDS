# Time complexity = O(n) Space complexity = O(n)
# def power(x, n):
# 	if (n == 0):
# 		return 1 
# 	else:
# 		xp = power(x, n - 1)
# 		return x * xp 

# print(power(2, 5))

def power(x, n):
	if (n == 0):
		return 1 
	xp = power(x, n // 2)
	xn = xp * xp 

	if (n % 2 == 1):
		xn = xn * x
	return xn 

print(power(2, 2))