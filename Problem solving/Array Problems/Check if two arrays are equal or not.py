# Check if two arrays are equal or not :
def equalornot(arr1,arr2,n) :
    s1 = sorted(arr1)
    s2 = sorted(arr2)

    if s1 == s2 :
        return " Same "
    else :
        return "Not Same "


n = int(input("Enter a length of the array : "))
arr1 = list(map(int,input("Enter a array 1 elements : ").split()))
arr2 = list(map(int,input("Enter a array 1 elements : ").split()))

print("It was ",equalornot(arr1,arr2,n))
