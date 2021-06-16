# Method first 

def kthSmall(arr, k):
    arr.sort()
    return arr[k-1]

if __name__ == '__main__':
    arr = [7, 10, 4, 3, 20, 15]
    print(" Enter the no. how small  value you want?")
    k = int(input())
    res = kthSmall(arr, k)
    print("3rd smallest element in the given array is: ", res)
