# Floor in a Sorted Array

def findFloor(a,n,x):
        #Your code here
        l,r = 0,n - 1
        ans = -1
        
        while l <= r :
            mid = (l + r) // 2
            
            if a[mid] == x :
                return mid
            elif a[mid] < x :
                ans = mid
                l = mid + 1
            else :
                r = mid - 1
        return ans
   


arr = list(map(int,input().split()))
n = len(arr)
x = int(input("Enter a value : "))
print(findFloor(arr,n,x))
