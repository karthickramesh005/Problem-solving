# Minimum Number in a sorted rotated array

def minNumber(arr):
        #Your code here
        m = min(arr)
        return m

arr = list(map(int,input("Enter a array values : ").split()))
print(minNumber(arr))
