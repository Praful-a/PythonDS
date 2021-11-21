def isPalindrome(string):
	arr = list(string)
	res = True
	s = 0
	e = len(arr) - 1
	while s < e:
		if arr[s] != arr[e]:
			res = False 
			break 
		s += 1
		e -= 1
	if res:
		return f"{string} is palindrome"
	else:
		return f"{string} is not palindrome"

string = "abc"
print(isPalindrome(string))