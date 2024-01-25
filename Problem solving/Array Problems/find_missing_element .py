#find_missing_element 

def find_missing_element(N, A):
    # Calculate the expected sum of first N natural numbers
    expected_sum = N * (N + 1) // 2
    
    # Calculate the sum of the given array
    actual_sum = sum(A)
    
    # Find the missing element by subtracting the actual sum from the expected sum
    missing_element = expected_sum - actual_sum
    
    return missing_element

# Example usage:
N = int(input("Enter a lenght of the array : "))
A = list(map(int,input().split()))

result = find_missing_element(N, A)
print("Missing element:", result)
