# Third largest element :
def thirdlargest(arr,n):
    arr.sort(reverse = True)
    return arr[2]

    
n = int(input("Enter a lenght of the array : "))
arr = list(map(int,input().split()))

print(thirdlargest(arr,n))
        
