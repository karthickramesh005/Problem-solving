# Triplet Sum in Array

def Triplesum(n,arr,x):
    for i in range(0,n- 2):
        for j in range(i + 1,n - 1):
            for s in range(j + 1,n):
                if arr[i]+arr[j]+arr[s] == x:
                    return "Yes"
    return "No"


n= int(input("Enter a lenght of the array : "))
arr = list(map(int,input("Enter a elements : ").split()))
x = int(input("Enter a Triple sum value : "))
r = Triplesum(n,arr,x)
print(r)
