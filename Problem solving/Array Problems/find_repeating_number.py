# find_repeating_number :

def find_repeating_number(arr):
    visited = set()

    for num in arr:
        if num in visited:
            return num
        visited.add(num)

    # If no repeating number is found
    return None

# Example usage:
input_array = list(map(int,input("Enter a array elements : ").split()))

repeating_number = find_repeating_number(input_array)

if repeating_number is not None:
    print("Repeating number:", repeating_number)
else:
    print("No repeating number found.")
