# First approach time complexity O(n^2)
arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
n = len(arr)
index = 0
for i in range(n):
   for j in range(n):
       if(i == arr[j]):
           arr[j], arr[i] = arr[i], arr[j]
    
for i in range(n):
    if (arr[i] != i):
        arr[i] = -1

print(arr)

