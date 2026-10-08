import numpy as np

# Create a random array of 9 integers
array = np.random.randint(1, 100, 9)

print("Original Array:")
print(array)

# Find square root of each element
print("\nSquare Root of Array:")
print(np.sqrt(array))

# Find number of dimensions
print("\nNumber of Dimensions:")
print(array.ndim)

# Reshape the array into 3 x 3
new_array = array.reshape(3, 3)

print("\nReshaped Array:")
print(new_array)

# Find number of dimensions after reshaping
print("\nNumber of Dimensions After Reshaping:")
print(new_array.ndim)

# Flatten the array using ravel()
print("\nRavelled Array:")
print(new_array.ravel())

# Reshape again into 3 x 3
newm = new_array.reshape(3, 3)

print("\nNew Matrix:")
print(newm)

# Array slicing
print("\nnewm[2,1:3]:")
print(newm[2, 1:3])

print("\nnewm[1:2,1:3]:")
print(newm[1:2, 1:3])

print("\nnew_array[0:3,0:0]:")
print(new_array[0:3, 0:0])

print("\nnew_array[0:2,0:1]:")
print(new_array[0:2, 0:1])

print("\nnew_array[0:3,0:1]:")
print(new_array[0:3, 0:1])

print("\nnew_array[1:3]:")
print(new_array[1:3])