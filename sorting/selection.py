def selection_sort(arr, n):
    for i in range(n - 1):
        min_idx = i   
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j 
        temp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = temp 
    return arr

arr = [1, -3, -4, 100, -200, 500]
size = len(arr)
print(selection_sort(arr, size))