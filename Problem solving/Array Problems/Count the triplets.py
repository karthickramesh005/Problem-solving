#Count the triplets


def count_triplets(arr, n):
    count = 0

    # Iterate through all possible triplets
    for i in range(n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the sum of two elements equals the third element
                if arr[i] + arr[j] == arr[k] or arr[i] + arr[k] == arr[j] or arr[j] + arr[k] == arr[i]:
                    count += 1

    return count

# Example usage:
arr = list(map(int,input("Enter a elements : ").split()))
n = len(arr)
result = count_triplets(arr, n)
print("Output:", result)
