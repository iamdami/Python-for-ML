# Operation that occurs when the shape of the arrays is the same

import numpy as np 

test_a = np.arange(1, 13).reshape(3, 4)
print(test_a * test_a)

"""
[[ 1 4 9 16]
 [ 25 36 49 64] 
 [ 81 100 121 144]]
"""
