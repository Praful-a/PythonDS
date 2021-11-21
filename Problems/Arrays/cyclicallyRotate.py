# Time Complexity = O(n) Space = O(1)
# def rotateCyclic(arr, n):
# 	temp = arr[-1]
# 	for i in range(n - 2, -1, -1):
# 		arr[i + 1] = arr[i]
# 	arr[0] = temp 
# 	return arr 

# Two pointer approach with same time and space complexity
def rotateCyclic(arr, n):
	s = 0 
	e = n - 1
	while s != e:
		arr[s], arr[e] = arr[e], arr[s]
		s += 1
	return arr 

arr = [1, 2, 3, 4, 5]
n = len(arr)
print(rotateCyclic(arr, n))