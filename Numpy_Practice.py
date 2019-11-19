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

