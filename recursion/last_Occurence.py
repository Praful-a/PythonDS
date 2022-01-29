def lastIndex(arr, idx, d):
	if idx == len(arr):
		return -1
	liisa = lastIndex(arr, idx + 1, d)
	if(liisa == -1):
		if(arr[idx] == d):
			return idx 
		else:
			return -1 
	else:
		return liisa  

arr = [2, 3, 6, 9, 8, 3, 2, 3, 6, 4]
d = 3
print(lastIndex(arr, 0, d))