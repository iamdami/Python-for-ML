import numpy as np 

a = np.array([[1, 4], [9, 16]], float)
b = np.array([0, 0, 1, 1, 0], int)
c = np.array([0, 1, 1, 1, 1], int)

print(a[b, c])  # Convert b to row index and c to column index to display


"""
[ 1.  4. 16. 16.  4.]
"""
