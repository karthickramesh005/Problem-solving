# Intersection of two arrays

def Intersection(arr1,arr2):
    s1 = set(arr1)
    s2 = set(arr2)
    uni = s1.intersection(s2)
    return len(uni)
arr1 = list(map(int,input("Enter a first array elements : ").split()))
arr2 = list(map(int,input("Enter a second array elements : ").split()))
print("Intersection of two array count : ",Intersection(arr1,arr2))
