def allIndices(arr, x, idx, fsf):
	if (idx == len(arr)):
		return [None] * fsf 

	if (arr[idx] == x):
		iarr = allIndices(arr, x, idx + 1, fsf + 1)
		iarr[fsf] = idx 
		return iarr 
	else:
		iarr = allIndices(arr, x, idx + 1, fsf)
		return iarr


arr = [2, 3, 6, 9, 8, 3, 2, 3, 6, 4]
d = 2
print(allIndices(arr, d, 0, 0))