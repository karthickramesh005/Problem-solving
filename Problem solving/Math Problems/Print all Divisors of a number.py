# Print all Divisors of a number : 

def print_divisors(N):
    divisors = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
    
    divisors.sort()
    
    # Print the divisors
    for divisor in divisors:
        print(divisor, end=" ")

# Example usage
N = int(input())
print_divisors(N)
