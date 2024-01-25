# Roteted array :

def rotateArray(arr, k) :
    # Write your code here.
    n = len(arr)
    k = k % n 
    ar = arr[k :] + arr[ : k]
    return ar



arr = list(map(int,input("Enter a array elements : ").split()))
k = int(input("Enter a lenght of the array : "))

s =rotateArray(arr, k) 

for i in s :
    print(i,end = " ")
    
