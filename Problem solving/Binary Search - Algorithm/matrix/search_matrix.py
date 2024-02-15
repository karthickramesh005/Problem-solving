''' Given a matrix of size n x m, where every row and column is sorted in increasing order, and a number x.
Find whether element x is present in the matrix or not . '''

def search_matrix(matrix, target):
    if not matrix:
        return False

    n = len(matrix)
    m = len(matrix[0])
    
    # Start from the top-right corner
    row = 0
    col = m - 1
    
    while row < n and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            # Move down if the current element is smaller than the target
            row += 1
        else:
            # Move left if the current element is larger than the target
            col -= 1
    
    return False

# Example usage:
matrix = [
    [3, 30, 38],
    [36, 43, 60],
    [40, 51, 69]
]
x = 62
print(search_matrix(matrix, x))
