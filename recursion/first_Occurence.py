# worst case
def firstIdx(arr, idx, d):
	if (idx == len(arr)):
		return -1 
	fiisa = firstIdx(arr, idx + 1, d)
	if (arr[idx] == d):
		return idx 
	else:
		return fiisa

# best case
def firstIdx(arr, idx, d):
	if (idx == len(arr)):
		return -1 
	if (arr[idx] == d):
		return idx 
	else:
		fiisa = firstIdx(arr, idx + 1, d)
		return fiisa

arr = [2, 3, 6, 9, 8, 3, 2, 6, 2, 4]
print(firstIdx(arr, 0, 3))