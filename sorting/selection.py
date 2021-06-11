def printArr(arr, n):
    print(" .. Array elements are ..")
    for i in range(n):
        print(arr[i], end=" ")

def selectionSort(arr, n):
    
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if(arr[j] < arr[min_ind]):
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]


if __name__ == '__main__':
    arr = []
    size = int(input(" Enter the size of array :"))
    print("Enter the array elements : ")
    for i in range(size):
        arr.append(int(input()))
    print(" .. Before Sorting ..")
    printArr(arr, size)
    selectionSort(arr, size)
    print("\n\n.. After Sorting ..")
    printArr(arr, size)