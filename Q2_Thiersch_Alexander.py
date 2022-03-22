#%%[markdown]
# You may use web search, notes, etc. 
# Do not use help from another human. If you use help from another student, 
# then I have no choice but to consider that student not a human, and will be 
# booted off my class immediately. You will also arrive at the same fate.
#
# I have a dataframe with all python classes from an online site.
# Complete the tasks below without importing any libraries except pandas.
# After we load the csv file as a dataframe, write codes to find out how 
# much time I will need total to learn the followings: 
# 1. all the classes in the list there? 
# 2. all the classes with "machine learning" (case insensitive) in the category column (some courses have multiple categories)? 
# 3. all the classes with the phrase "machine learning" (case insensitive) in the objective? 
# 4. all the classes with either "machine learning" (case insensitive) in the category, or with 
# the phrase "machine learning" (case insensitive) in the objective? 
#
# 
# Name: Alexander Thiersch\
# Date: 03/22/2022\
# DATS 6103\
# Quiz 2

#%%
import pandas as pd
import q2data as q2
# classes = pd.read_csv('DC_Py_list.csv')
classes = q2.df 
print(classes.info())
print(classes.head())
# use the dataframe "classes" to answer the questions. 
# Q1 should be straightforward (take 1 minute to solve).
# 
# Q2 and Q3 are similar. Once you get Q2, the rest is the same.
# One method is to create a boolean array/dataframe that fits the matching criteria. 
# Remeber the broadcasting and filter methods in numpy/pandas?
# To do case-insentive match, you can google and see how that can be done.
# As a first try, just do the exact match of 'machine learning'. You will not get 
# all the case-insensitive matches, but at least you will get something. 
# Do these for Q3 and Q4 with exact match first without worrying about upper/lower case.
# Get those to make sense first.
# 
# Then come back and try to modify your code to include case-sensitivity. 
# (You will still get most of the credits if only case-sensitivity not working.)
#
# Finally 
# Q4 is to combine Q2 and Q3 logically. (Should take only a couple minutes.)

#%%
# 1

classes.info()

classes['time'].sum()

# 234.0

#%%
# 2

c1 = classes[classes['category'].str.contains('machine learning', na=False, case=False)]
print(c1)
c1['time'].sum()

# 54.5

#%%
# 3

c2 = classes[classes['objective'].str.contains('machine learning', na=False, case=False)]
print(c2)
c2['time'].sum()


# 15.5

#%%
# 4

c3 = classes[(classes['category'].str.contains('machine learning', na=False, case=False)) | (classes["objective"].str.contains('machine learning', na=False, case=False))]
print(c3)
c3['time'].sum()

# 61.25

# %%
