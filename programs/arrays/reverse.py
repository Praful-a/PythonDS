""" Method 1

def reverse(arr):
    n = len(arr)
    for cur in range(n-1, -1, -1):
        print(arr[cur], end=" ")

if __name__ == '__main__':
    arr = [1, 2, 3]
    reverse(arr)  """

""" Method 2"""
# def reverse(arr, start, end):
#     while start < end:
#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = temp
#         start += 1
#         end -= 1

# if __name__ == '__main__':
#     arr = [1, 2, 3]
#     end = len(arr)
#     reverse(arr, 0, end-1)
#     print("\nRevered list is :")
#     print(arr)
# Time Complexity is O(n)

""" Method 3"""

def reverse(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse(arr, start + 1, end - 1)

if __name__ == '__main__':
    arr = [1, 2, 3]
    end = len(arr)
    reverse(arr, 0, end-1)
    print("\nRevered list is :")
    print(arr)
# Time Complexity is O(n)

