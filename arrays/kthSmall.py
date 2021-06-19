# Method first 
class solution: 
    def kthsmallest(self, arr, l, r, k):
        for i in range(l, r):
            for j in range(0, r-i):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr[k-1]


if __name__ == '__main__':
    t = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ob = solution()
    print(ob.kthsmallest(arr, 0, t-1, k))