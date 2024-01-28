import numpy as np

arr = np.array([1, 2, 3, 4, 5])
tup = np.array((1,2,3,4,5))

print(arr)
print(tup)

print(type(arr))


# Create a 0-D array with value 42

arr1 = np.array(42)

print(arr1)


# Create a 1-D array containing the values 1,2,3,4,5:

arr2 = np.array([1, 2, 3, 4, 5])

print(arr2)


# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

arr3 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr3)

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr4)
print(arr4.ndim)  # it tells the dimension