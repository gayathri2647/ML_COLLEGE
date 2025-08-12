# NumPy Illustration

# NumPy is a Python library used for working with arrays.

# NumPy stands for Numerical Python.

# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a
# lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.



###### 1) Creating an array   ######

# To create an array, we can pass a list, tuple or
# any array-like object into the array() method,
# and it will be converted into an ndarray

# Passing list as an argument
import numpy as np
arr = np.array([1,2,3,4])
print(arr)
print(type(arr))
'''
# Passing tuple as an argument

import numpy as np
arr = np.array((1,2,3,4))
print(arr)
print(type(arr))

# 0 - Dimensional array
import numpy as np
arr = np.array([11])
print(arr)
print(type(arr))

# 1 - Dimensional array
import numpy as np
arr = np.array([11,22,33,44])
print(arr)
print(type(arr))

# 2 - Dimensional array
import numpy as np
arr = np.array([[11,22,33,44],[55,66,77,88]])
print(arr)
print(type(arr))

# Check Number of Dimensions
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
'''

###### 2) Accessing an array elements  ######
'''
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[3])
print(arr[2] + arr[3])

# Accessing 2 - Dimensional array
import numpy as np
arr = np.array([[11,22,33,44],[55,66,77,88]])
print(arr[0,1])   # The first value represents the dimension and the second value represents the index
print(arr[1,1])
print(arr[1,-1])
print(arr[0,-1])
'''

###### 3) Slicing an array   ######
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[3:-1])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::])
print(arr[::2])
'''

# Slicing 2-D array
'''
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0, 1:4])
print(arr[1, 1:-1])
print(arr[0, 1:-1])
print(arr[0, :])
print(arr[1, :])
print(arr[0:2, 2])
print(arr[0:2, 2:4])
'''

##### 4)  Data Types in Python   #####
'''
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
'''

#####   5) Data Types in NumPy     #####
'''
List of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
'''
import numpy as np
arr = np.array([1, 2, 3, 4])
# dtype is a property in array object which returns the datatype of the object
print(arr.dtype)   

import numpy as np
arr = np.array([1.1, 2.2, 3.3, 4.4])
print(arr.dtype)

import numpy as np
arr = np.array(['arun', 'siva', 'santhosh'])
print(arr.dtype)

#  Creating Arrays With a Defined Data Type
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

import numpy as np
arr = np.array([1, 2, 3, 4], dtype='f')
print(arr)
print(arr.dtype)
'''

##### 6)  Copy and view in an array #####
# The main difference between a copy and a view of an array
# is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy
# will not affect original array, and any changes made to
# the original array will not affect the copy.

# The view does not own the data and any changes made to
# the view will affect the original array, and any changes made to
# the original array will affect the view.

'''
#  Illustration of copy()
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

#  Illustration of view()
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42   # Make a change in an original array
print(arr)
print(x)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31    # Make a change in a view
print(arr)
print(x)
'''

##### 7)  Displaying the Shape of an Array #####
# The shape of an array is the number of elements in each dimension.

# NumPy arrays have an attribute called shape that
# returns a tuple with each index having the number of corresponding elements.

'''
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.shape)

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
'''

#####  8) Reshaping arrays using reshape()  ,  flatten()  and ravel()    #####
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

'''
#### using reshape()  ####
# Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

# Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 4)
print(newarr)

# Reshape From 2-D to 1-D
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
newarr1 = arr.reshape(1,8)   # returns 2-D array with 1 row and 8 coulmns
newarr2 = arr.reshape(-1)    # returns 1-D array
print(newarr1)
print(newarr2) 

# Other examples
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
newarr3 = arr.reshape(-1,1)  # Here -1 represents the no.of rows in the given input
print(newarr3)
print(newarr3.ndim)
print(newarr3.shape)
newarr4 = arr.reshape(1,-1)  # Here -1 represents the no.of columns in the given input
print(newarr4)
print(newarr4.ndim)
print(newarr4.shape)
'''

'''
#### Using flatten() to convert 2-D into 1-D    ####
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
newarr=arr.flatten('C')
# The flatten() function is used to get a copy of an given array
# collapsed into one dimension. 'C' means to flatten in row-major (C-style) order.
# 'F' means to flatten in column-major (Fortran- style) order
print(newarr)

newarr=arr.flatten('F')
print(newarr)

#### Using ravel() to convert 2-D into 1-D    ####
newarr=arr.ravel('C')
print(newarr)
newarr=arr.ravel('f')
print(newarr)

#### using reshape() to mention the order
newarr1 = arr.reshape(-1,order='c')    # returns 1-D array
newarr2 = arr.reshape(-1,order='f')    # returns 1-D array

newarr3 = np.reshape(arr,-1,'C')
newarr4 = np.reshape(arr,-1,'f')
print(newarr1)
print(newarr2)
print(newarr3)
print(newarr4)
'''

'''
#### Illustration of difference between flatten() and ravel()
import numpy as np
arr = np.arange(12).reshape(3,4) # arange() is used to create an array with the given range
print(arr)
newarr=arr.flatten('C')
newarr[5] = 111   # The change will be reflected in new array only. It wont reflect in original
arr[1][2] = 444   # The change will be reflected in original only. It wont reflect in new array
print(arr)       
print(newarr)    

import numpy as np
arr = np.arange(12).reshape(3,4) # arange() is used to create an array with the given range
print(arr)
newarr=arr.ravel('C')
arr[1][2] = 444  # The change will be reflected in new array too
newarr[5] = 111  # The change will be reflected in original array too
print(arr)       
print(newarr)
'''

####   ravel()                                      flatten()     ###
# --------------------------------------------------------------- ###
# 1. Returns only the reference            1. Return copy of the 
#    /view of the original array              initial array

# 2. The changes will be reflected         2. The changes done in new array
#    in both original and coped arrays        will not be reflected in original

# 3. Fasterthan flatten(), since it        3. Slower than ravel(). Since, it 
#    wont take up the memory. Simply          occupies memory.
#    refer the original only

'''
# More examples for arange()
import numpy as np
arr = np.arange(12)
print(arr)

arr = np.arange(12).reshape(3,4) 
print(arr)

arr = np.arange(1,13)
print(arr)

arr = np.arange(1,13).reshape(3,4) 
print(arr)

arr = np.arange(10,100,10)
print(arr)

arr = np.arange(10,100,10).reshape(3,3) 
print(arr)

arr = np.arange(-5,-1)
print(arr)

arr = np.arange(-5,-1,2)
print(arr)

arr = np.arange(-5,10,3)
print(arr)

arr = np.arange(15,1,-1)
print(arr)

arr = np.arange(15,1,-3)
print(arr)

arr = np.arange(15,15)     ####  Assume the output before execute????
print(arr)

arr = np.arange(1,15,-2)     ####  Assume the output before execute????
print(arr)

arr = np.arange(15,1,2)     ####  Assume the output before execute????
print(arr)

#######   Think over the difference between range() and arange()
'''

#####    9)  Iteration of arrays   ######
'''
# Iteration of 1-D array
import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

# Iteration of 2-D array
import numpy as np
arr = np.arange(1,13).reshape(3,4)
for x in arr:
  print(x)

# Iteration of 2-D array
import numpy as np
arr = np.arange(1,13).reshape(3,4)
for x in arr:
     for y in x:
          print(y)
'''

#####    10)  Concatenating arrays using concatenate() and stack()  ######
'''
# Conatenation using concatenate()
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2))
print(arr)

import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# Conatenation using stack()
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2))
print(arr)

import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
'''

#####    11)  Splitting arrays   ######
# Splitting breaks one array into multiple
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 5)
print(newarr)

# splitting 2-D array
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
'''


#####   12)  Searching in an array using where()   #####
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) # Index positions of 4 will be displayed
print(x)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0) # index position of even nos
print(x)

import numpy as np
arr = np.array([16, 70, 8, 9])
x = np.searchsorted(arr, 70)  # performs a binary search in the array, and returns the index
print(x)
'''

#####   13) Sorting array   #####
'''
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
'''

##### Other programs   #####
'''
import numpy as np
A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
print(A)

# Array of zeros
import numpy as np
zeors_array = np.zeros( (2, 3))  # Array of zeros as float values
print(zeors_array)

# Array of zeros
import numpy as np
# Array of zeros as integer values
zeors_array = np.zeros( (2, 3), dtype = int )
print(zeors_array)

# Array of ones
ones_array = np.ones( (1, 5), dtype=np.int32 ) # specifying dtype
print(ones_array)      # Output: [[1 1 1 1 1]]

##### Matrix operations  #####
# Matrix addition
import numpy as np
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B      # adding 2 matrices
print(C)

# Matrix multiplication using dot()
import numpy as np
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print(C)

# Matrix multiplication using *
import numpy as np
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A * B      # adding 2 matrices
print(C)

# Transpose of a Matrix using transpose()
import numpy as np
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose())

# Identity matrix
import numpy as np
dimension = int(input("Enter the dimension of identitiy matrix: "))
identity_matrix = np.identity(dimension, dtype="int")
print(identity_matrix)
'''

'''
# create an array with zero above the main diagonal
import numpy as np
# To create an array with zero above the main diagonal
# forming a lower triangular matrix, use the numpy.tri() method in Python Numpy
# The 1st parameter is the number of rows in the array
# The 2nd parameter is the number of columns in the array
arr = np.tri(4, 4,dtype = int)
# Displaying our array
print("Array...",arr)

# Caculating no.of elements in an array
import numpy as np
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.size) # Display no.of elements
print(A.ndim)  # Display the dimension
print(A.shape) # Display the shape of an array
'''

# To create an array with zero below the main diagonal
import numpy as np
arr = np.arange(25).reshape(5,5)
print(np.tril(arr))
#print(arr)

# To create an array with zero below the main diagonal
import numpy as np
arr = np.arange(25).reshape(5,5)
print(np.tril(arr,k = -2))
#print(arr)

# To create an array with zero below the main diagonal
import numpy as np
arr = np.arange(25).reshape(5,5)
print(np.tril(arr,k = -1))
#print(arr)

# To create an array with zero above the main diagonal using tril()
import numpy as np
arr = np.arange(25).reshape(5,5)
print(np.tril(arr,k = 1))
#print(arr)
   
