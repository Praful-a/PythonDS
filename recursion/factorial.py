def fact(n):
	if n < 1:
		return "Please enter positive number !"
	elif ((n == 0) or (n == 1)):
		return 1 
	return n * fact(n - 1)

n = 5
print(fact(n))