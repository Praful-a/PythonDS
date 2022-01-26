def displayArr(arr, idx):
	if idx == len(arr):
		return  
	print(arr[idx])
	displayArr(arr, idx+1)

arr = [10, 20, 30, 40, 50]
displayArr(arr, 0)