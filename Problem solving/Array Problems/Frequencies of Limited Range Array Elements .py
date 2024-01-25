# Frequencies of Limited Range Array Elements :
def frequencyCount(N,arr, P):
        P += 1
        for i in range(N):
            idx  = arr[i]%P
            if idx <= N:
                arr[idx-1] += P
        
        for i in range(N):
            arr[i] = arr[i]//P
        return arr



n = int(input("Enter a lenght of the arrray : "))
a1 = list(map(int,input("Enter a array 1 elements : ").split()))
p = int(input("Enter a value : "))

result =  frequencyCount(n, a1, p)
print(result)
