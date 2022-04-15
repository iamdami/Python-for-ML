import numpy as np 

test_a = np.array([[1, 2, 3]]) 
test_b = np.array([[4, 5, 6]]) 
print(np.concatenate((test_a, test_b), axis=0))

"""
[[1 2 3]
 [4 5 6]]
"""

"""
test_a = np.array([[1, 2], [3]]) 
test_b = np.array([[5, 6], [7]])

하면 발생하는 오류
        ↓
Creating an ndarray from ragged nested sequences
(which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes)
is deprecated. 
If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
  b = numpy.array([[5, 6], [7]])
[list([1, 2]) list([3]) list([5, 6]) list([7])]
"""


# 이건 됨!
a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([[5, 6], [7, 8]])
print(numpy.concatenate((a, b), axis=0))

"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""
