
# Array Subset of another array :


def isSubset(a1, a2):
    # Convert arrays to sets for efficient subset checking
    set_a1 = set(a1)
    set_a2 = set(a2)
    
    # Check if set_a2 is a subset of set_a1
    if set_a2.issubset(set_a1):
        return "Yes"
    else:
        return "No"

# Example usage:
a1 = list(map(int,input("Enter a array 1 elements : ").split()))
a2 =list(map(int,input("Enter a array 2 elements : ").split()))

result = isSubset(a1, a2)
print(result)
