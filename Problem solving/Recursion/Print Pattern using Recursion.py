# Print Pattern using Recursion  :
def print_sequence(n, initial_value):
    if n > 0:
        print(n, end=" ")
        print_sequence(n - 5, initial_value)
    elif n < initial_value:
        print(n, end=" ")
        print_sequence(n + 5, initial_value)

# Example usage:
N =  16
print_sequence(N, N)

