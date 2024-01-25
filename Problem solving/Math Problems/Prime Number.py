# Prime Number :

def is_prime(N):
    if N <= 1:
        return 0  # N is not a prime number

    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return 0  # N is not a prime number

    return 1  # N is a prime number

# Example usage:
N = int(input())
result = is_prime(N)
print(result)
