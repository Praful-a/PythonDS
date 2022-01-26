def reverseArr(arr, idx):
	if idx == len(arr):
		return   
	reverseArr(arr, idx + 1)
	print(arr[idx])

arr = [10, 20, 30, 40, 50]
reverseArr(arr, 0)