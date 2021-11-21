def reverse(string):
	arr = list(string)
	s = 0
	e = len(arr) - 1
	while s < e:
		arr[s], arr[e] = arr[e], arr[s]
		s += 1
		e -= 1
	return "".join(arr)

string = "Hello"
print(reverse(string))