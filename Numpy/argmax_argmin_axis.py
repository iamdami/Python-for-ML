import numpy as np 

a = np.array([[1, 2, 4, 7], [9, 88, 6, 45], [9, 76, 3, 4]])
print(np.argmax(a, axis=1), np.argmin(a, axis=0))

"""
[3 1 1] [0 0 2 2]
"""
