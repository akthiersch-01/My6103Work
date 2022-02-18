# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# HW Numpy 
# ## By: Alexander Thiersch
# ### Date: 02/18/2022
#

#%%
# NumPy

import numpy as np

# %%
# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########
# This exercise is to test true/shallow copies, and related concepts. 
# ----------------------------------------------------------------
# 
# ######  Part 1a      Part 1a      Part 1a   ##########
# 
list2 = [ [11,12,13], [21,22,23], [31,32,33], [41,42,43] ] # two dimensional list (2-D array)  # (4,3)
nparray2 = np.array(list2)
print("nparray2:", nparray2)

# We will explain more of this indices function in class next. See notes in Class05_02_NumpyCont.py
idlabels = np.indices( (4,3) ) 
print("idlabels:", idlabels)

i,j = idlabels  # idlabels is a tuple of length 2. We'll call those i and j
nparray2b = 10*i+j+11
print("nparray2b:",nparray2b)

# 1.a) Is nparray2 and nparray2b the "same"? Use the logical "==" test and the "is" test. 
# Write your codes, 

nparray2 == nparray2b

nparray2 is nparray2b

# and describe what you find.
    # nparray2 == nparray2b is True, and nparray2 is nparray2b is False. 
    # == is used to determine value equity. This determines if the objects have the same value.
    # Whereas, "is" is used to determine a reference equity. This determine if somehting is the exact same object.
    # nparray2 and nparray2b have the same value, but they are not the same object.



# %%
# ######  Part 1b      Part 1b      Part 1b   ##########
# 
# 1.b) What kind of object is i, j, and idlabels? Their shapes? Data types? Strides?
    # i, j, and idlabels are numpy.ndarray objects.
    # i, j, and idlabels shapes are 4x3, 4x3, and 2x4x3 respectively.
    # i, j, and idlabels data types are int64
# write your codes here

#type
type(i) #numpy.ndarray
type(j) #numpy.ndarray
type(idlabels) #numpy.ndarray

#shape
i.shape  # 4 x 3
j.shape  # 4 x 3
idlabels.shape  # 2 x 4 x 3

# data type
i.dtype #int64
j.dtype #int64
idlabels.dtype #int64

# strides
i.strides  # (24, 8)
j.strides  # (24, 8)
idlabels.strides  # (96, 24, 8)



# %%
# ######  Part 1c      Part 1c      Part 1c   ##########
# 
# 1.c) If you change the value of i[0,0] to, say 8, print out the values for i and idlabels, both 
# before and after the change.

# write your codes here
print(i)
print(idlabels)

i[0,0] = 8

print(i)
print(idlabels)


# Describe what you find. Is that what you expect?
    # Prior to altering the i the 0th row of the array displays 0 0 0.
    # After altering the i the 0th row of the array displays 8 0 0.
    #However, the idlabels did not change despite altering the array.
    #The changes to i is what I expected becasue using the index i[0,0] (i[row,column]) and setting it equal to allows us to change a specific value within the array.
    #It is expecred that the idlabes did not change becasue i[0,0] is speciifcaly changing a value within the array and not the idlabels of each row or column.

# Also try to change i[0] = 8. Print out the i and idlabels again.

i[0]=8
print(i)
print(idlabels)

# i[0]=8 changes the specifically all the 0th row values in the i array.
# This is observed when printing i as all the values in the 0th row are 8.
# However, the idlabels are still unchaged because the index does not change the id labels of the columns and rows.

# %%
# ######  Part 1d      Part 1d      Part 1d   ##########
# 
# 1.d) Let us focus on nparray2 now. (It has the same values as nparray2b.) 
# Make a shallow copy nparray2 as nparray2c
# now change nparray2c 1,1 position to 0. Check nparray2 and nparray2c again. 
#
# Print out the two arrays now. Is that what you expect?
    # After altering the array nparray2c at position 1,1 to 0, it alterd both nparray2c and nparray2. 
    # This is not what I expected. I only expected nparray2c to be altered not nparray2 becasue I specifically indexed the nparray2c array.
    # Additionally, when using == operator both arrays are True and have value equity. However, when using "is" the two arrays a different objects.
    # 
# Also use the "==" operator and "is" operator to test the 2 arrays. 
# write your codes here
#
nparray2c = nparray2[:]
print(nparray2)
print(nparray2c)

nparray2c[1,1] = 0
print(nparray2)
print(nparray2c)

nparray2c == nparray2
nparray2c is nparray2

#%%
# ######  Part 1e      Part 1e      Part 1e   ##########
# Let us try again this time using the intrinsic .copy() function of numpy array objects. 
nparray2 = np.array(list2) # reset the values. list2 was never changed.
nparray2c = nparray2.copy() 
# now change nparray2c 0,2 position value to -1. Check nparray2 and nparray2c again.
# Are they true copies?
    # After altering the nparray2c array at 0,2 position value to -1 the 0th row and 2nd column is changed to -1.
    # nparray2c is not a true copy because when using the "is" operator it returns False. This indicates that nparray2c is not a clone of nparray2 as its reference values are not the same.

# write your codes here
# Again use the "==" operator and "is" operator to test the 2 arrays. 
#
nparray2c[0,2] = -1 

nparray2c == nparray2
nparray2c is nparray2

print(nparray2c)
print(nparray2)

# Since numpy can only have an array with all values of the same type, we usually 
# do not need to worry about deep levels copying. 
# 
# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########




# %%
# ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########
# Write NumPy code to test if two arrays are element-wise equal
# within a (standard) tolerance.
# between the pairs of arrays/lists: [1e10,1e-7] and [1.00001e10,1e-8]
# between the pairs of arrays/lists: [1e10,1e-8] and [1.00001e10,1e-9]
# between the pairs of arrays/lists: [1e10,1e-8] and [1.0001e10,1e-9]
# Try just google what function to use to test numpy arrays within a tolerance.

print(np.allclose([1e10,1e-7], [1.00001e10,1e-8])) #False, not equal element-wise. 
print(np.allclose([1e10,1e-8], [1.00001e10,1e-9])) #True, same element-wise.
print(np.allclose([1e10,1e-8], [1.0001e10,1e-9])) #False, not rqual element-wise.


# ######  END of QUESTION 2    ###   END of QUESTION 2   ##########


# %%
# ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########
# Write NumPy code to reverse (flip) an array (first element becomes last).
x = np.arange(12, 38)
print(x)

np.flip(x)
print(x)

#Or can also code x[::-1]
#x = x[::-1] #reverse (flip) an array
#print(x)



# ######  END of QUESTION 3    ###   END of QUESTION 3   ##########


# %%
# ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########
# First write NumPy code to create an 7x7 array with ones.
# Then change all the "inside" ones to zeros. (Leave the first 
# and last rows untouched, for all other rows, the first and last 
# values untouched.) 
# This way, when the array is finalized and printe out, it looks like 
# a square boundary with ones, and all zeros inside. 
# ----------------------------------------------------------------

# np.ones creates an array of 1s. dtype=int64 has to be specified since default is float64 and thus would print as 1.
numpy_array = np.ones((7, 7), dtype="int64")
print(numpy_array)
x_index = 0
for x in numpy_array:
    y_index = 0
    for y in x:
        if x_index == 0 or x_index == 6:
            break
        else:
            if 0 < y_index < 6:
                print(x_index, y_index)
                numpy_array[x_index][y_index] = 0
        y_index += 1
    x_index += 1
print(numpy_array)


# ######  END of QUESTION 4    ###   END of QUESTION 4   ##########



# %%
# ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########
# Broadcasting, Boolean arrays and Boolean indexing.
# ----------------------------------------------------------------
i=3642
myarray = np.arange(i,i+6*11).reshape(6,11)
print(myarray)
# 
# a) Obtain a boolean matrix of the same dimension, indicating if 
# the value is divisible by 7. 

bool_matrix_div_7 = myarray%7 == 0
print(bool_matrix_div_7)

# b) Next get the list/array of those values of multiples of 7 in that original array  

mult_seven = myarray[bool_matrix_div_7]
print(mult_seven)

# ######  END of QUESTION 5    ###   END of QUESTION 5   ##########


#
# The following exercises are  
# from https://www.machinelearningplus.com/python/101-numpy-exercises-python/ 
# and https://www.w3resource.com/python-exercises/numpy/index-array.php
# Complete the following tasks
# 

# ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########

#%%
flatlist = list(range(1,25))
print(flatlist) 

#%%
# 6.1) create a numpy array from flatlist, call it nparray1. What is the shape of nparray1?
# remember to print the result
#
# write your codes here
#
nparray1 = np.array(flatlist)
print(nparray1.shape)

#%%
# 6.2) reshape nparray1 into a 3x8 numpy array, call it nparray2
# remember to print the result
#
# write your codes here
#
nparray2 = np.reshape(nparray1, (3, 8))
print(nparray2)



#%%
# 6.3) swap columns 0 and 2 of nparray2, and call it nparray3
# remember to print the result
#
# write your codes here
#
nparray3 = nparray2[:, [2, 1, 0, 3, 4, 5, 6, 7]]
print(nparray3)

#%%
# 6.4) swap rows 0 and 1 of nparray3, and call it nparray4
# remember to print the result
#
# write your codes here
#
nparray4 = nparray3[:, [1, 0, 2, 3, 4, 5, 6, 7]]
print(nparray4)

#%%
# 6.5) reshape nparray4 into a 2x3x4 numpy array, call it nparray3D
# remember to print the result
#
# write your codes here
#
nparray3D = np.reshape(nparray4, (2, 3, 4))
print(nparray3D)

#%%
# 6.6) from nparray3D, create a numpy array with boolean values True/False, whether 
# the value is a multiple of three. Call this nparray5
# remember to print the result
# 
# write your codes here
#
nparray5 = nparray3D%3 == 0
print(nparray5)

#%%
# 6.7) from nparray5 and nparray3D, filter out the elements that are divisible 
# by 3, and save it as nparray6a. What is the shape of nparray6a?
# remember to print the result
#
# write your codes here
#
nparray6 = nparray3D[nparray5]
print(nparray6)
print(nparray6.shape)

#%%
# 6.8) Instead of getting a flat array structure, can you try to perform the filtering 
# in 6.7, but resulting in a numpy array the same shape as nparray3D? Say if a number 
# is divisible by 3, keep it. If not, replace by zero. Try.
# Save the result as nparray6b
# remember to print the result
# 
# write your codes here
#
# 
nparray6b = np.copy(nparray3D)
x_index = 0
for x in nparray6b:
    y_index = 0
    for y in x:
        z_index = 0
        for z in y:
            if z % 3 > 0:
                nparray6b[x_index][y_index][z_index] = 0
            z_index += 1
        y_index += 1
    x_index +=1
print(nparray6b)

# ######  END of QUESTION 6    ###   END of QUESTION 6   ##########

#%%
#
