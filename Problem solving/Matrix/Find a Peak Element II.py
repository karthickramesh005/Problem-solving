# Find a Peak Element II
def findPeakGrid(mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        row, col = 0, len(mat[0]) - 1

        while row < len(mat) and col >= 0:
            if col > 0 and mat[row][col - 1] > mat[row][col]:
                col -= 1
            else:
                row += 1

        return [row - 1, col]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(findPeakGrid( matrix))
