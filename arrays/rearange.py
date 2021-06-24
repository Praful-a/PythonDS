
def rearange(arr, n):
    j = 0
    for i in range(n):
        if(arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j + 1
    print(arr)

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
rearange(arr, n)