# Time Complexity = O(n^2)
# def bubbleSort(arr, size):
#     for i in range(0, size - 1):
#         for j in range(0, size - i - 1):
#             if (arr[j] > arr[j+1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def printarr(arr, size):
#     for i in range(0, size):
#         print(arr[i], end=" ")

# if __name__ == '__main__':
#     arr = [1, -3, -4, 100, -200, 500]
#     size = len(arr)
#     print("\n .. Before Sorting ..\n")
#     printarr(arr, size)
#     bubbleSort(arr, size)
#     print("\n .. After Sorting ..\n")
#     printarr(arr, size)

# Time Complexity = O(n)
# def bubble_srt(arr, n):
#     swapped = True
#     for i in range(n - 1):
#         swapped = False 
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True 
#         if swapped == False:
#             break 
#     return arr


# Recursive 
def bubble_srt(arr, n):
    if n == 1:
        return 
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_srt(arr, n - 1)
    return arr

arr = [1, -3, -4, 100, -200, 500]
size = len(arr)
print(bubble_srt(arr, size))


