# find factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
N = int(input("Enter a number : "))
result = factorial(N)
print(result)
