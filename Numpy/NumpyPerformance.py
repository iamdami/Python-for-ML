# General speed
# numpy > list comprehension > for loop

# When using for loop
def sclar_vector_product(scalar, vector):
    result = []
    for value in vector: 
        result.append(scalar * value)
    return result 
    
iternation_max = 100000000

vector = list(range(iternation_max))
scalar = 2 

%timeit sclar_vector_product(scalar, vector)


# When using list comprehension
%timeit [scalar * value for value in range(iternation_max)]


# When using numpy
%timeit np.arange(iternation_max) * scalar
