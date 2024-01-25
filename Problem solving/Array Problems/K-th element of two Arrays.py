# K-th element of two Arrays :
def kthElement(arr1, arr2, k):
        arr3 = arr1 + arr2
        arr3.sort()
        return arr3[k - 1]

arr1 = list(map(int,input("Enter  a first element array : ").split()))
arr2 = list(map(int,input("Enter  a second element array : ").split()))
k = int(input("Enter a position of element : "))
print("Knt element : ",kthElement(arr1, arr2, k))
