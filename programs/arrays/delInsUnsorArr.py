# Search Opration on unsorted array

# def search(arr, x, n):
# 	for i in range(n):
# 		if arr[i] == x:
# 			return f"value found at index : {i}"
# 	return "Not Found !!"

# arr = [5, 1, 3, 4, 2, 6]
# x = 10
# print(search(arr, x, len(arr)))

# Insert option on unsorted array
# def insert(arr, x):
# 	arr.append(x)
# 	return arr 

# arr = [5, 1, 4, 2, 6]
# x = 3
# pos = 3
# print(insert(arr, x, pos))

# Delete opration on unsorted array
def delete(arr, x):
	n = len(arr)
	p = pos(arr, x)
	for i in range(p, n - 1):
		arr[i] = arr[i + 1]
	n -= 1
	for i in range(n):
		print(arr[i], end= " ")

def pos(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i

arr = [5, 1, 4, 3, 2, 6]
x = 2
delete(arr, x)