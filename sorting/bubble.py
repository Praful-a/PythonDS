def bubbleSort(arr, size):
    for i in range(0, size - 1):
        for j in range(0, size - i - 1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def printarr(arr, size):
    for i in range(0, size):
        print(arr[i], end=" ")

if __name__ == '__main__':
    arr = [1, -3, -4, 100, -200, 500]
    size = len(arr)
    print("\n .. Before Sorting ..\n")
    printarr(arr, size)
    bubbleSort(arr, size)
    print("\n .. After Sorting ..\n")
    printarr(arr, size)