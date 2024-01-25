# Union of two arrays

def union(arr1,arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    uni = s1.union(s2)
    return len(uni)
arr1 = list(map(int,input("Enter a first array elements : ").split()))
arr2 = list(map(int,input("Enter a second array elements : ").split()))
print("union of two array count : ",union(arr1,arr2))
