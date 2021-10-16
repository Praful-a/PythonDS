# Looping way Time Complexity O(n)
# def reverse(arr, s, e):
# 	while s < e:
# 		arr[s], arr[e] = arr[e], arr[s]
# 		s += 1
# 		e -= 1
# 	return arr 

# arr = [1, 2, 3, 4, 5]
# s = 0
# e = len(arr) - 1
# print(reverse(arr, s, e))

# Recursive way Time & Space Complexity O(n)
# def reverse(arr, s, e):
# 	if s >= e:
# 		return
# 	arr[s], arr[e] = arr[e], arr[s]
# 	reverse(arr, s + 1, e - 1)
# 	return arr

# arr = [1, 33, 4, 55, 6]
# s = 0
# e = len(arr) - 1
# print(reverse(arr, s, e))


# Pythonic way Time Complexity O(n)
# def reverse(arr):
# 	return arr[::-1]

# arr = [1, 33, 4, 55, 6]
# print(reverse(arr))

# String Reverese Looping way Time Complexity O(n)
def reverse(arr, s, e):
	while s < e:
		arr[s], arr[e] = arr[e], arr[s]
		s += 1
		e -= 1
	return arr 

string = "Hello this is me"
arr = list(string)
s = 0
e = len(arr) - 1
res = reverse(arr, s, e)
print(''.join(res))
