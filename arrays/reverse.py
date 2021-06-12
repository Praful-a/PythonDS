import time

# def reverse(arr):
#     for i in range(len(arr)-1, -1, -1):
#         print(arr[i], end=" ")
 
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5]
#     reverse(arr)

# start = time.time()
# arr = [1, 2, 3, 4, 5]
# print(arr[::-1])
# end = time.time()
# print(end - start)

# Iterative solution

# def reversed(arr, start, end):
#     while(start < end):
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1

# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5]
#     print("\n .. Before reverse ..")
#     print(arr)
#     reversed(arr, 0, len(arr)-1)
#     print(" .. After reverse ..")
#     print(arr)

# Recursive solution

def reversed(arr, start, end):
    if start >= end:
        return 
    arr[start], arr[end] = arr[end], arr[start]
    reversed(arr, start+1, end-1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print("\n .. Before reverse ..")
    print(arr)
    reversed(arr, 0, len(arr)-1)
    print(" .. After reverse ..")
    print(arr)
