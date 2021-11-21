# Time Complexity = O(n) Space = O(1)
def isPalindrome(string):
	# arr = list(string)
	res = True
	s = 0
	e = len(string) - 1
	while s < e:
		if string[s] != string[e]:
			res = False 
			break 

		s += 1
		e -= 1
	if res:
		return f"{string} is palindrome"
	else:
		return f"{string} is not palindrome"

string = "abba"
print(isPalindrome(string))