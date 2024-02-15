''' Given a binary matrix (containing only 0 and 1) of order NxN. All rows are sorted already, We need to find the row number with the maximum number of 1s.
Also, find the number of 1s in that row. '''

def max_ones_row(matrix):
    max_row = 0
    max_count = 0
    for i, row in enumerate(matrix):
        count = sum(row)
        if count > max_count:
            max_row = i
            max_count = count
    return max_row, max_count

# Example usage:
matrix = [[0, 0, 1], [0, 1, 1], [0, 0, 0]]
row_number, max_count = max_ones_row(matrix)
print("Row number =", row_number)
print("MaxCount =", max_count)
