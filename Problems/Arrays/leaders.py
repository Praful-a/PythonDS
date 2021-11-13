# Using two loops Time complexity = O(n^2)
# def printLeader(arr, size):
# 	for i in range(size):
# 		for j in range(i + 1, size):
# 			if arr[i] <= arr[j]:
# 				break 
# 		if j == size - 1:
# 			print(arr[i], end=" ")

# Using second method check elements from right Time = O(n)
def printLeader(arr, size):
	max_ele = arr[size - 1]
	print(max_ele, end=" ")
	for i in range(size - 2, -1, -1):
		if arr[i] > max_ele:
			print(arr[i], end=" ")
			max_ele = arr[i]

arr = [16, 17, 4, 3, 5, 2]
printLeader(arr, len(arr))