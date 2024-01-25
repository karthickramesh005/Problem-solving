# Remove duplicate elements from sorted Array

def remove_duplicate( arr, n):
        if n <= 1:
            return n
 
    # Initialize variables
        j = 0

    # Iterate through the array
        for i in range(1, n):
        # If the current element is different from the previous one
            if arr[i] != arr[j]:
                j += 1
                arr[j] = arr[i]

    # Return the number of distinct elements
        return j + 1
arr = list(map(int,input("Enter a first array elements : ").split()))
n = len(arr)

print(remove_duplicate(arr, n))
