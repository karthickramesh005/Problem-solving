# Search a 2D Matrix :

def searchMatrix(matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Input elements for the 2D array using list comprehension
my_2d_array = [[int(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(columns)] for i in range(rows)]

k = int(input("Enter a search element : "))
print(searchMatrix(matrix, target))
