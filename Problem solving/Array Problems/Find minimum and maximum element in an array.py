# Find minimum and maximum element in an array

def minimax(arr,n):
    m= min(arr)
    ma = max(arr)
    return m,ma


n = int(input("Enter a lenght of the array : "))

arr = list(map(int,input().split()))
print(minimax(arr,n))

