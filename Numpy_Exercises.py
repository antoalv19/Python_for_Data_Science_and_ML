# Import NumPy as np
import numpy as np

# Create an array of ten zeros
ten_zeros = np.zeros(10)
print(ten_zeros)

# Create an array of ten 1s
ten_one = np.ones(10)
print(ten_one)

# Create an array of ten 5s
ten_five = np.full(shape=10, fill_value=5, dtype=np.int)
print(ten_five)

# Create an array of the integers from 10 to 50
arr_50 = np.arange(10, 51)
print(arr_50)

# Create an array of all the even integers from 10 to 50
arr_even = arr_50[arr_50 % 2 == 0]

print(arr_even)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_08 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(matrix_08)

# Create a 3x3 identity matrix
matrix_ident = np.eye(3)
print(matrix_ident)

# Use NumPy to generate a random number between 0 and 1
random_num = np.random.rand()
print(random_num)

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
arr_25_stdev = np.array(np.random.rand(25))
print(arr_25_stdev)

# Create a 10 by 10 matrix from 0 to one
matrix_1010 = np.arange(0.01, 1.01, 0.01, dtype="float")
print(matrix_1010.reshape(10, 10))

# Create an array of 20 linearly spaced points between 0 and 1
array_20_lin = np.linspace(0, 1, 20)
print(array_20_lin)

# Numpy Indexing and Selection
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
mat = np.arange(1, 26).reshape(5, 5)
print(mat)

# WRITE CODE THAT REPRODUCES THE CELL BELOW
mat_1 = mat[2:, 1:]
print(mat_1)

# WRITE CODE THAT REPRODUCES THE CELL BELOW = 20
mat_20 = mat[3, -1]
print(mat_20)

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW [2, 7, 12]
mat_2712 = mat[:3, 1]
mat_2712 = mat_2712.reshape(3, 1)
print(mat_2712)

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW [21, 22, 23, 24, 25]
mat_last = mat[-1, :]
print(mat_last)

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW [16, 17, 18, 19, 20]
#                                                              [21, 22, 23, 24, 25]

mat_last_two = mat[-2:, :]
print(mat_last_two)

# Get the sum of all the values in mat
print(mat.sum())

# Get the standard deviation of the values in mat
print(mat.std())

# Get the sum of all the columns in mat
sum_each_row = np.sum(mat, axis=0)
print(sum_each_row)
