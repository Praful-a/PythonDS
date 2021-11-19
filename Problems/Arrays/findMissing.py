# Time Complexity = O(n^2) Space = O(1)
def findMissing(arr, n):
	total = (n + 1)*(n + 2) // 2
	sum_of_arr = 0
	for i in arr:
		sum_of_arr += i 
	return total - sum_of_arr

arr = [1, 2, 4, 6, 3, 7, 8]
n = len(arr)
print(findMissing(arr, n))