# Time coplexity = O(n^2) space = O(1)
# def pair_for_sum(arr, x):
# 	res = False
# 	n = len(arr)
# 	for i in range(n):
# 		for j in range(i + 1, n):
# 			if arr[i] + arr[j] == x:
# 				print(f"{arr[i]}, {arr[j]}")
# 				res = True 
# 	return res


# Method1 : Sorting and Two-Pointers technique.
def pair_for_sum(arr, x):
	res = False
	arr.sort()
	l = 0 
	r = len(arr) - 1
	while l < r:
		if (arr[l] + arr[r]) < x:
			l += 1
		elif (arr[l] + arr[r]) > x:
			r -= 1
		else:
			print(f"{arr[l]}, {arr[r]}")
			res = True
			break
	return res

arr = [0, -1, 2, -3, 1]
x = -10
r = pair_for_sum(arr, x)
if r == True:
	print("Valid pair exists.")
else:
	print("No valid pair exists.")