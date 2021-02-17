# Extract values of diagonal matrix
import numpy as np

matrix = np.arange(9).reshape(3, 3)
np.diag(matrix)
"""[0 4 8]"""


matrix = np.arange(9).reshape(3, 3)
np.diag(matrix, k=1)
"""[1, 5]"""
