# Given a square matrix, calculte the diagonal difference between sums of it's diagonals.
# a square matrix is given as array a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# The diagonal difference is |(1 + 5 + 9) - (3 + 5 + 7)| = 2

# consider the function below:
def diagonalDifference(arr):
    # Write your code here
    # Initialize sums of diagonals
    d1 = 0
    d2 = 0
    n = len(arr)
    # Loop through all rows
    for i in range(n):
        # Loop through all columns
        for j in range(n):
            # finding sum of primary diagonal
            if i == j:
                d1 += arr[i][j]
            # finding sum of secondary diagonal
            if i == n - j - 1:
                d2 += arr[i][j]
    # Absolute difference of the sums
    return abs(d1 - d2)

# Driver code
if __name__ == '__main__':
    # input array
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 19]]
    # Calling the function
    print(diagonalDifference(arr))