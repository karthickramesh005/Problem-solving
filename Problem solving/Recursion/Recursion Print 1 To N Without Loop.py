# Recursion Print 1 To N Without Loop

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n, end=' ')

# Example usage:
N = int(input("Enter a number : "))
print_numbers(N)
