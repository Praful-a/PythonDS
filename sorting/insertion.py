# Time complaxity = O(n^2)
def insertion_sort(arr, n):
    for i in range(1, n - 1):
        key = arr[i]
        j = i 
        while(arr[j - 1] > key and j >= 1):
            arr[j] = arr[j - 1]
            j -= 1 
        arr[j] = key  
    return arr 

arr = [1, -3, -4, 100, -200, 500]
size = len(arr)
print(insertion_sort(arr, size))