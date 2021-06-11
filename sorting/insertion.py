def printArr(arr, n):
    print(" .. Array elements are ..")
    for i in range(n):
        print(arr[i], end=" ")

def insertionSort(arr, n):

    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp

if __name__ == '__main__':
    arr = []
    size = int(input(" Enter the size of array :"))
    print("Enter the array elements : ")
    for i in range(size):
        arr.append(int(input()))
    print(" .. Before Sorting ..")
    printArr(arr, size)
    insertionSort(arr, size)
    print(" .. After Sorting ..");
    printArr(arr, size)