# Time Complexity = O(n^2) Space = O(1)
# def findElement(arr, n):
# 	res = False 
# 	for i in range(n):
# 		count = 0 
# 		for j in range(n):
# 			if arr[i] == arr[j]:
# 				count += 1
# 		if count % 2 != 0:
# 			res = True 
# 			break 
# 	if res:
# 		return arr[i]
# 	else:
# 		return -1

# Time Complexity = O(n) Space = O(n)
def findElement(arr, n):
	res = False 
	m = {}
	for i in arr:
		if i not in m:
			m[i] = 1
		else:
			m[i] += 1
	for key in m:
		if m[key] % 2 != 0:
			res = True 
			break 
	if res:
		return key
	else:
		return -1

arr = [1, 2, 3, 2, 3, 1, 3]
n = len(arr)
print(findElement(arr, n))