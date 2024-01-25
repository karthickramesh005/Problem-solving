# find perfectNumber : 

def isPerfectNumber(N):
    if N <= 0:
        return 0  # Negative numbers and zero are not perfect

    # Find factors and calculate sum excluding the number itself
    factors_sum = 0
    for i in range(1, N):
        if N % i == 0:
            factors_sum += i

    # Check if the sum of factors is equal to the number
    if factors_sum == N:
        return 1  # It's a perfect number
    else:
        return 0  # It's not a perfect number

# Example usage:
N = int(input("Enter a number : "))
result = isPerfectNumber(N)
print(result)
