# Peak element

def peakElement(arr, n):
        # Code here
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

        # Check if mid is a peak
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
                return mid

        # If the element on the right is greater, search in the right half
            elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1

        # If the element on the left is greater, search in the left half
            else:
                high = mid - 1

        return -1
    
arr = [1,2,3]
print(peakElement(arr, len(arr)))
