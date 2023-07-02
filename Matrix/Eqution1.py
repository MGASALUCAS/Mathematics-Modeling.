import numpy as np

# Define the matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

C = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

# Calculate the result
result = np.dot(A, np.dot(B, C)) - np.dot(C, np.dot(B, A))

# Print the result
print(result)
