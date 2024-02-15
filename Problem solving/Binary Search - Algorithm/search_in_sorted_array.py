# search_in_sorted_array

def search_in_sorted_array(arr, N, K):
    left, right = 0, N - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == K:
            return 1  # K is present in the array

        elif arr[mid] < K:
            left = mid + 1

        else:
            right = mid - 1

    return 0  # K is not present in the array

# Example usage:
N = 5
K = 6
arr = [1, 2, 3, 4, 6]

output = search_in_sorted_array(arr, N, K)
print(output)  # Output: 1
