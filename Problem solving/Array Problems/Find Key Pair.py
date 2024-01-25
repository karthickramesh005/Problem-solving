# Find Key Pair :
def keypair(n,arr,x):
    for i in range(0,n - 1):
        for j in range(i + 1,n):
            if (arr[i] + arr[j] == x) :
                return "Yes"
            
    return  "Not"
                
n = int(input("Enter a lenght of the array : "))
arr = list(map(int,input().split()))
x = int(input("Enter a key pair sum value : "))

result = keypair(n,arr,x)
print(result)
