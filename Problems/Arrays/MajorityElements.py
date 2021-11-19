# Time Complexity = O(n^2) Space = O(1)
# def findMajority(arr, n):
# 	res = False
# 	for i in range(n):
# 		count = 0
# 		for j in range(n):
# 			if arr[i] == arr[j]:
# 				count += 1
# 		if (count > n // 2):
# 			res = True
# 			break 
# 	if res:
# 		return arr[i]
# 	else:
# 		return -1


# Time Complexity = O(n) Space = O(n)
def findMajority(arr, n):
	m = {}
	res = False 
	for i in arr:
		if i not in m:
			m[i] = 1 
		else:
			m[i] += 1 
	for key in m:
		if m[key] > n // 2:
			res = True 
			break 
	if res:
		return key
	else:
		return -1 

arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
n = len(arr)
print(findMajority(arr, n))