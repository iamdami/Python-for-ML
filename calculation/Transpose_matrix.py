# Matrix Transpose

matrix_a = [[1,2,3], [4,5,6]]
result =[[element for element in i] for i in zip(*matrix_a)]

print(result)
# [[1, 4], [2, 5], [3, 6]]
