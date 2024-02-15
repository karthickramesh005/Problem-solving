#    Given an ascending sorted rotated array Arr of distinct integers of size N. The array is right rotated K times.
#Find the value of K

def findKRotation(arr,  n):
        # code here
        return arr.index(min(arr))
arr= [5, 1, 2, 3, 4]

n = 5
print(findKRotation(arr,  n))
