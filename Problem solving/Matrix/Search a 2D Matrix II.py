# Search a 2D Matrix II

def searchMatrix( matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # Start from the top-right corner

        while row < rows and col >= 0:
            current_value = matrix[row][col]

            if current_value == target:
                return True
            elif current_value > target:
                col -= 1  # Move left in the current row
            else:
                row += 1  # Move down to the next row

        return False

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
t = int(input())
print(searchMatrix( matrix, t))

# Print the rotated matrix

