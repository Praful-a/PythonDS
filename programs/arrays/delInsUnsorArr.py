# Search Opration on unsorted array
def search(arr, x, n):
	for i in range(n):
		if arr[i] == x:
			return f"value found at index : {i}"
	return "Not Found !!"

arr = [5, 1, 3, 4, 2, 6]
x = 10
print(search(arr, x, len(arr)))