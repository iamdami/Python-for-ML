import numpy as np

test_matrix = np.array([[1,2,3],[4,5,6]], float)
scalar = 3

print(test_matrix + scalar) 
print(test_matrix - scalar)
print(test_matrix * 5)
print(test_matrix / 5)
print(test_matrix // 0.2) 
print(test_matrix ** 2)

"""
# test_matrix + scalar 
[[4. 5. 6.] 
 [7. 8. 9.]] 
 
# test_matrix - scalar 
[[-2. -1. 0.] 
 [ 1. 2. 3.]] 
 
# test_matrix * 5 
[[ 5. 10. 15.] 
 [20. 25. 30.]] 
 
# test_matrix / 5 
[[0.2 0.4 0.6] 
 [0.8 1. 1.2]]
 
# test_matrix // 0.2 
[[ 4. 9. 14.] 
 [19. 24. 29.]]
 
# test_matrix ** 2
[[ 1. 4. 9.]
 [16. 25. 36.]]
"""
