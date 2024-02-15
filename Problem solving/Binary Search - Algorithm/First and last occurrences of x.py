# First and last occurrences of x

def findoccurnces( arr, n, x):
        
        # code here
        first_occurrence = -1
        last_occurrence = -1

    # Binary search to find the first occurrence
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                first_occurrence = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1

    # Reset low and high for binary search to find the last occurrence
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                last_occurrence = mid
                low = mid + 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                 high = mid - 1

        return first_occurrence, last_occurrence
    
arr = list(map(int,input().split()))
n = len(arr)
x = int(input("Enter a value : "))
print(findoccurnces(arr, n, x))
