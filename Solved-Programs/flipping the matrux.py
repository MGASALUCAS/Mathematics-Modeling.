# a program to flip the matrix and find the maximum possible sum of the upper-left quadrant.
def flipMatrix(matrix):
    # Write your code here
    # Initialize the value of result
    result = 0
    n = len(matrix)
    # Loop through all rows
    for i in range(n):
        # Loop through all columns
        for j in range(n):
            # finding sum of upper-left quadrant
            if i < n // 2 and j < n // 2: # logicallt this means that if i is less than n // 2 and j is less than n // 2. // has meaning of floor division. floor division means that the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
                result += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1]) # this line means that the value of result will be increased by the maximum value of the matrix.
    return result