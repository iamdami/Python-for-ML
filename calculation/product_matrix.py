# Matix Product

matrix_a = [[1,1,2], [2,1,1]]
matrix_b = [[1,1], [2,1], [1,3]]
result = [[sum(i*j for i, j in zip(row_a, column_b))
    for column_b in zip(*matrix_b)] for row_a in matrix_a]

print(result)
# [[5, 8], [5, 6]]
