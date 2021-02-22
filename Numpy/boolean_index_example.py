import numpy as np

A = np.array([
    [12, 13, 14, 12, 16, 14, 11, 10, 9],
    [11, 14, 12, 15, 15, 16, 10, 12, 11],
    [10, 12, 12, 15, 14, 16, 10, 12, 12],
    [9, 11, 16, 15, 14, 16, 15, 12, 10],
    [12, 11, 16, 14, 10, 12, 16, 12, 13], 
    [10, 15, 16, 14, 14, 14, 16, 15, 12],
    [13, 17, 14, 10, 14, 11, 14, 15, 10],
    [10, 16, 12, 14, 11, 12, 14, 18, 11],
    [10, 19, 12, 14, 11, 12, 14, 18, 10],
    [14, 22, 17, 19, 16, 17, 18, 17, 13],
    [10, 16, 12, 14, 11, 12, 14, 18, 11], 
    [10, 16, 12, 14, 11, 12, 14, 18, 11],
    [10, 19, 12, 14, 11, 12, 14, 18, 10], 
    [14, 22, 12, 14, 11, 12, 14, 17, 13],
    [10, 16, 12, 14, 11, 12, 14, 18, 11]])
B = A < 15 
print(B.astype(np.int))


"""
[[1, 1, 1, 1, 0, 1, 1, 1, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 0, 1, 1, 1],
 [1, 1, 0, 0, 1, 0, 0, 1, 1],
 [1, 1, 0, 1, 1, 1, 0, 1, 1], 
 [1, 0, 0, 1, 1, 1, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1], 
 [1, 0, 1, 1, 1, 1, 1, 0, 1], 
 [1, 0, 1, 1, 1, 1, 1, 0, 1], 
 [1, 0, 0, 0, 0, 0, 0, 0, 1], 
 [1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1], 
 [1, 0, 1, 1, 1, 1, 1, 0, 1], 
 [1, 0, 1, 1, 1, 1, 1, 0, 1]]
"""
