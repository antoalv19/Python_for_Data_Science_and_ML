import numpy as np

#######################################################################################################################
############################################ FASE PRATICA - ARRAYS ####################################################
#######################################################################################################################

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
############################################## FINE FASE PRATICA - ARRAYS #############################################
#######################################################################################################################
############################################## INIZIO FASE PRATICA - INDEXING #########################################
#######################################################################################################################

# create sample array
index_arr = np.arange(0, 11)
print(index_arr)

# Get a value at an index
print(index_arr[2])

# Get values in a range
print(index_arr[2:6])

# Get values in a range from 0
print(index_arr[0:5])

# Broadcasting: Numpy arrays differ from a normal Python list because of their ability to broadcast
# Setting a value with index range (Broadcasting)
# index_arr[0:5] = 100

slice_of_arr = index_arr[0:6]
print(slice_of_arr)

# change slice - it is changes also in the original array | data is not copied because of memory problems
slice_of_arr[:] = 99
print(slice_of_arr)
print(index_arr)

# To get a copy, need to be explicit
arr_copy = index_arr.copy()
print(arr_copy)

"""
Indexing a 2D array (matrices)
The general format is arr_2d[row][col] or arr_2d[row,col]. I recommend usually using the comma notation for clarity.
"""
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))

print(arr_2d)

# indexing row
print(arr_2d[0])

# getting individual element value
print(arr_2d[1, 0])

# 2D array slicing - Shape (2,2) from top right corner
# Riga da 0 a 1 e colonna da 1 alla fine
slice_2d = arr_2d[:2, 1:]
print(slice_2d)

# Fancy indexing allows you to select entire rows or columns out of order:
fancy_index = np.zeros((10, 10))
print(fancy_index)

# Length of array
fancy_length = fancy_index.shape[1]

# set up array
for i in range(fancy_length):
    fancy_index[i] = i

print(fancy_index)

# Fancy indexing allows the following
fancy_index_1 = fancy_index[[2, 3, 4]]
fancy_index_2 = fancy_index[[9, 8, 7]]

print(fancy_index_1)
print(fancy_index_2)

# Selection: how to use brackets for selection based off of comparison operators.
arr_selection = np.arange(1, 11)
print(arr_selection)

# BOOL operator
print(arr_selection > 4)

bool_arr = arr_selection > 4

print(arr_selection[bool_arr])

print(arr_selection[arr_selection > 4])

x = 3

print(arr_selection[arr_selection > x])

#######################################################################################################################
############################################## FINE FASE PRATICA - INDEXING ###########################################
#######################################################################################################################
############################################## INIZIO FASE PRATICA - OPERATIONS########################################
#######################################################################################################################
# Arithmetic: You can easily perform array with array arithmetic, or scalar with array arithmetic.
aritm_arr = np.arange(0, 10)

# addizione
aritm_add = aritm_arr + aritm_arr
print(aritm_add)

# Moltiplicazione
aritm_mult = aritm_arr * aritm_arr
print(aritm_mult)

# Sottrazione
aritm_sub = aritm_arr - aritm_arr
print(aritm_sub)

# Divisione
aritm_div = aritm_arr / aritm_arr
print(aritm_div)

# 1 / arr
aritm_div0 = 1 / aritm_arr
print(aritm_div0)

# Power of 3
aritm_pow = aritm_arr ** 3
print(aritm_pow)

# UNIVERSAL ARRAY FUNCTIONS
# Taking square root
arr_sq = np.sqrt(aritm_arr)
print(arr_sq)

# Calculating exponential (e^)
arr_ep = np.exp(aritm_arr)
print(arr_ep)

# array max
arr_max = np.max(aritm_arr)
print(arr_max)

# array min
arr_min = np.min(aritm_arr)
print(arr_min)

# calculate sin
arr_sin = np.sin(aritm_arr)
print(arr_sin)

# calculate log
arr_log = np.log(aritm_arr)
print(arr_log)
