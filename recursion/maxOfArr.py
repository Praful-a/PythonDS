def maxOfArr(arr, idx):
	if idx == len(arr) - 1:
		return arr[idx]

	misa = maxOfArr(arr, idx + 1)
	if (misa > arr[idx]):
		return misa 
	else:
		return arr[idx]

arr = [220, 33, 40, 19, 7]
print(maxOfArr(arr, 0))