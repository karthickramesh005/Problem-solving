# Cyclically rotate an array by one :

def rotate(arr) :
    a = arr[-1]
    arr.pop()
    arr.insert(0,a)
    return arr


n = int(input("Enter a lenght of the array : "))
arr = list(map(int,input("Enter a array elements : ").split()))
s = rotate(arr)

for i in s :
    print(i,end = " ")
