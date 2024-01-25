# Search an Element in an array

def searchelement(arr,n,x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


n = int(input("Enter a lenght of the array : "))
arr = list(map(int,input("Enter a array elements : ").split()))
x = int(input("Enter a search element : "))
print(searchelement(arr,n,x))
