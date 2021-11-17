# Time coplexity = O(n^2) space = O(1)
def pair_for_sum(arr, x):
	res = False
	n = len(arr)
	for i in range(n):
		for j in range(i + 1, n):
			if arr[i] + arr[j] == x:
				print(f"{arr[i]}, {arr[j]}")
				res = True 
	return res

arr = [0, -1, 2, -3, 1]
x = -10
r = pair_for_sum(arr, x)
if r == True:
	print("Valid pair exists.")
else:
	print("No valid pair exists.")