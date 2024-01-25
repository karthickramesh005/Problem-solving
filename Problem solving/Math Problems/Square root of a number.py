# Square root of a number :

def square(x):
        if (x == 0 or x == 1): 
            return x 
      
        start = 1
        end = x
        res = 0
        
        # binary search to find square root of a number
        while start <= end:
            mid = (start + end) // 2
            
            # if mid*mid == x, then mid is the required element
            if mid*mid == x:
                return mid
            
            # if mid*mid < x, then iterate for upper half
            if mid*mid < x:
                start = mid+1
                res = mid
                
            # else, iterate for lower half
            else:
                end = mid-1
        
        return res

x = int(input("Enter a number : "))
print(square(x))

