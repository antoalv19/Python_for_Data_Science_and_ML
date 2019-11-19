import numpy as np

# create list
test_list = [1, 2, 3]
print(test_list)

# create array
print(np.array(test_list))

# create matrix array
test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(test_matrix)

print(np.array(test_matrix))

# print array in interval
arr_interval = np.arange(0, 6)
print(arr_interval)

# print array in interval with specified range
arr_int_range = np.arange(0, 11, 2)
print(arr_int_range)

# generate array of zero
zeroes = np.zeros(3)
print(zeroes)

# generate matrix of zeroes
zero_matrix = np.zeros((3, 3))
print(zero_matrix)

# generate array of ones
ones = np.ones(3)
print(ones)

# generate matrix of ones
ones_matrix = np.ones((2, 4))
print(ones_matrix)

# linspace function
# return evenly spaced numbers over a specified interval
linear_space = np.linspace(0, 10, 4)
print(linear_space)

# print matrix
linear_matrix = np.linspace(0, 10, 50)
print(linear_matrix)

# create identity matrix
ident_matr = np.eye(5)
print(ident_matr)

# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1)
random_practice = np.random.rand(3)
print(random_practice)

# print matrix
random_practice_matr = np.random.rand(5, 5)
print(random_practice_matr)

# Return a sample (or samples) from the "standard normal" distribution.
rand_arr = np.random.randn(3)
print(rand_arr)

# print matrix from the dtandard normal distribution
rand_norm_matrix = np.random.randn(5, 5)
print(rand_norm_matrix)

# Return random integers from low (inclusive) to high (exclusive).
randint_lh = np.random.randint(0, 50)
print(randint_lh)

# return random integers - how many?
randint_number = np.random.randint(0, 50, 10)
print(randint_number)

# arange - create array in a range
arange_arr = np.arange(30)
print(arange_arr)

# change the shape of an array
test_reshape = arange_arr.reshape(6, 5)
print(test_reshape)

# max,min,argmax,argmin
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax
max_value = randint_number.max()
print("Max value is {}".format(max_value))

max_arg = randint_number.argmax()
print("Max argument is at index {}".format(max_arg))

min_value = randint_number.min()
print("Minimum value is {}".format(min_value))

min_arg = randint_number.argmin()
print("Minimum argument is at index {}".format(min_arg))

# Shape
# Shape is an attribute that arrays have (not a method) (also reshape)
test_shape = arange_arr.shape
print(test_shape)

# change shape of an array
test_reshape = arange_arr.reshape(1, 30)
print(test_reshape)
print(test_reshape.shape)

test_reshape_2 = arange_arr.reshape(30, 1)
print(test_reshape_2)
print(test_reshape_2.shape)

# dtype
# You can also grab the data type of the object in the array:

test_dtype = arange_arr.dtype
print(test_dtype)

#######################################################################################################################
############################################## FINE FASE 1 PRATICA ####################################################
#######################################################################################################################

