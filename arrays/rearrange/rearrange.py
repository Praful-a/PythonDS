# First approach time complexity O(n^2)
"""arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
n = len(arr)
index = 0
for i in range(n):
   for j in range(n):
       if(i == arr[j]):
           arr[j], arr[i] = arr[i], arr[j]
    
for i in range(n):
    if (arr[i] != i):
        arr[i] = -1

print(arr)  """

# Second approach

# def fix(A, n):
#     for i in range(0, n):
#         if(A[i] != -1 and A[i] != i):
#             x = A[i]

#         while(A[x] != -1 and A[x] != x):
#             y = A[x]

#             A[x] = x

#             x = y

#         A[x] = x

#         if(A[i] != i):
#             A[i] = -1

# A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
# fix(A, len(A))

# for i in range(0, len(A)):
#     print(A[i], end=" ")

# HashSet approach
"""def fix(A):
    s = set()

    for i in range(len(A)):
        s.add(A[i])
    
    for i in range(len(A)):
        if i in s:
            A[i] = i
        else:
            A[i] = -1
    return A

# Driver Code
if __name__ == '__main__':
    A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    print(fix(A)) """

# Swap elements in Array

if __name__ == '__main__':
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    n = len(arr)
    i = 0
    while i < n:
        if(arr[i] >= 0 and arr[i] != i):
            (arr[arr[i]], arr[i]) = (arr[i], arr[arr[i]])
        else:
            i += 1
    
    for i in range(n):
        print(arr[i], end=" ")
