# bubble_sort Algorithm :

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
N = int(input("Enter a lenght of the array : "))
arr =list(map(int,input().split()))
bubble_sort(arr)

print("Sorted array:", end=" ")
for i in arr:
    print(i, end=" ")
