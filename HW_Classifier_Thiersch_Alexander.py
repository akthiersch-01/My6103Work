#%%[markdown]
#
# # HW8 - Classifiers on Digits dataset
# 
# A more comprehensive dataset on digits is available (on Blackboard). It is quite large, 
# with 60k observations. Each oberservatin is a 28x28 pixel gray scale image (digitized), 
# and 256 gray levels. The first column of the dataset (csv) is the target y value (0 to 9). 
# The remaining 784 columns are the gray values for each pixel for each observation.
#  
# ## Question 1: Read in the dataset
# First, unzip the data file. 
# There is no column names in the csv. You better create a list of names like x0, x1, 
# or x000, x001, etc, for the 784 columns plus the y-target. Use the list when creating 
# the dataframe. 

# Which column is the y-target?
# - The first column
# Check the shape and data type, make sure everything looks fine.
# - df.shape == (60000, 785)
# - df.dtype == object, df.columns.dtype == int64
#
# ## Question 2: Preparing the data
# On my system, if I use all 60k observations, it took a long time to run the classifiers. 
# I ended up retaining only 8k observations. They are already randomized. The first 
# 8k rows work for me. If you system is faster/slower, you should adjust the total 
# accordingly. Keep in mind however you better have many more rows than columns.
# 
# Now prepare for the 4:1 train-test split.
# 
# If the latter modeling part does not run, check the X_train, X_test has the 
# right object type. Use the 8x8 pixel sample in class as a guide. 
# 
# ## Question 3: View some samples 
# Plot the first and the last row of your train set, and see the image as we 
# did in class. Make sure the format is a 28x28 array for the plot to work.
# 
# ## Question 4: Run the six classifiers
# For each each, print the train score, the test score, the confusion matrix, and the classification report.
# 
# * SVC(): you can try adjusting the gamma level between 'auto', 'scale', 0.1, 5, etc, and see if it makes any difference 
# * SVC(kernel="linear"): having a linear kernel should be the same as the next one, but the different implementation usually gives different results 
# * LinearSVC() 
# * LogisticRegression()
# * KNeighborsClassifier(): you can try different k values and find a comfortable choice 
# * DecisionTreeClassifier(): try 'gini', 'entropy', and various max_depth  
#  
#  
# ## Question 5: Cross-validation 
# Use cross-validation to get the cv scores (set cv=10, and use the accuracy score) for the six classifiers. 
# You can use the X_test and y_test for that instead of the one we picked out. You might or might not have 
# that complete set separated into X and y, although it should be easy.
# 
# When you use cross validation, it will be a few times slower than before as it score each model 10 different times.
# 
# While we are at it, let us try to time it. If the you the magic python functions (%), 
# you can easily clock the executation time of a line of code. Instad of this:    
# 
# tree_cv_acc = cross_val_score(tree, X_cv, y_cv, cv= 10, scoring="accuracy") 
# OR  
# tree_cv_acc = cross_val_score(tree, X_cv, y_cv, cv= 10, scoring="accuracy", n_jobs = -1) 
# n_jobs = -1 will use all the core/CPU in your computer. Notice the difference in speed.  
# https://ipython.readthedocs.io/en/stable/interactive/magics.html?highlight=%25time#magic-time
# 
# we use this:     
# 
# %timeit tree_cv_acc = cross_val_score(tree, X_train, y_train, cv= 10, scoring='accuracy')    
# And I get, without n_jobs: ~ 18.2 s ± 167 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
# With n_jobs=-1, I have ~ 3.18 s ± 277 ms per loop (mean ± std. dev. of 7 runs, 1 loop each) 
# These are with 20k data rows.
# 
# Note that %timeit will also try a few (default 7) runs to find out the average time of 
# the cv function took.  The tree algorithm turns out not too bad.
# 
# Which classifier is the fastest and the slowest for you?
# 


###########  HW  ################
#%%
# First read in the datasets. 
import os
import numpy as np
import pandas as pd
from sklearn.datasets import load_digits

# list of column names
column_names = ['Y']
for number in range(784):
    column_names.append('x{:03d}'.format(number))

# Import data
df = pd.read_csv('mnist_train.csv', names=column_names, header=None)
print("\nReady to continue.")
#%%
from sklearn.model_selection import train_test_split
x_8k = df.loc[:, df.columns != 'Y'].head(8000)
y_8k = df['Y'].head(8000)
x_train, x_test, y_train, y_test = train_test_split(x_8k, y_8k, train_size=0.8, random_state=333)

print("\nReady to continue.")

#%%
# ## Question 3: View some samples 
# Plot the first and the last row of your train set, and see the image as we 
# did in class. Make sure the format is a 28x28 array for the plot to work.

# What do they look like?
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
import matplotlib.pyplot as plt 

x_array = np.asarray(x_train)
x_train_reshape_first = np.reshape(x_array[0], (28, 28))
plt.gray()
plt.imshow(x_train_reshape_first) 
# plt.matshow(digits.images[0]) 
plt.show() 

x_train_reshape_last = np.reshape(x_array[-1], (28, 28))
plt.gray() 
plt.matshow(x_train_reshape_last) 
plt.show() 

print("\nReady to continue.")


#%% 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

clf1 = SVC()
clf2 = SVC(kernel='linear')
clf3 = LinearSVC()
clf4 = LogisticRegression()
clf5 = KNeighborsClassifier()
clf6 = DecisionTreeClassifier()

clf_list = [clf1, clf2, clf3, clf4, clf5, clf6]
clf_names = ['SVC', 'SVC(kernel="linear")', 'Linear SVC', 'Logistic Regression', 'KNN', 'Decision Tree']

for clf, name in zip(clf_list, clf_names):
    clf.fit(x_train, y_train)
    print(f'{name} train score:  {clf.score(x_train,y_train)}')
    print(f'{name} test score:  {clf.score(x_test,y_test)}')
    print(f'============{name} Confusion Matrix============')
    print(confusion_matrix(y_test, clf.predict(x_test)))
    print(f'========={name} Classification Report=========')
    print(classification_report(y_test, clf.predict(x_test)))
print("\nReady to continue.")



#%%
# Sample code for cross validation
# We could use just the entire dataset (60k rows) for train-test split (90% training), 
# so that's 54000 data points for training. 
# Or we can start over, and get a set of X and y for CV here. 
# If we need to change size at some point, it's easier to do it here.
# NOTE: You might want to temporarily disable auto sleep/hibernation of your computer.
'''nmax = 2000 # nmax = 10000 # or other smaller values if your system resource is limited.
cvdigits = dfdigits.iloc[0:nmax,:]
X_cv = cvdigits.iloc[:,1:785] # 28x28 pixels = 784, so index run from 1 to 784 # remember that pandas iloc function like regular python slicing, do not include end number
print("cvdigits shape: ",cvdigits.shape)
print("X_cv shape: ",X_cv.shape)
y_cv = cvdigits.iloc[:,0]'''

x_8k = df.loc[:, df.columns != 'Y'].head(8000)
y_8k = df['Y'].head(8000)
x_train, x_test, y_train, y_test = train_test_split(x_8k, y_8k, train_size=0.9, random_state=333)

for clf, name in zip(clf_list, clf_names):
    %timeit -r 1 print(f'{name} CV score: {cross_val_score(clf, x_train, y_train, cv=10, scoring="accuracy")}')

for clf, name in zip(clf_list, clf_names):
    %timeit -r 1 print(f'{name} CV score: {cross_val_score(clf, x_train, y_train, cv=10, scoring="accuracy", n_jobs=-1)}')
# Logit Regression 
# %timeit -r 1 print(f'\nLR CV accuracy score: { cross_val_score(lr, X_cv, y_cv, cv= 10, scoring="accuracy", n_jobs = -1) }\n')   
# the flag -r 1 is to tell timeit to repeat only 1 time to find the average time. The default is to repeat 7 times.
# I get something like below
# without n_jobs, quit: STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.
# with n_jobs = -1, 
# nmax = 2000, it took ~ 6.81 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
# LR CV accuracy score: [0.86  0.88  0.86  0.835 0.83  0.82  0.85  0.85  0.905 0.875]
#
# nmax = 4000, it took ~ 56 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
# LR CV accuracy score: [0.86  0.88  0.86  0.835 0.83  0.82  0.85  0.85  0.905 0.875]
#
# nmax = 8000, it took ~ 6min 33s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
# LR CV accuracy score: [0.86  0.88  0.86  0.835 0.83  0.82  0.85  0.85  0.905 0.875]
# 
# BUT if I hook up my laptop to external monitors as I usually do, even with 
# nmax = 2000, it took ~ 53.3 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)
# It is EIGHT times slower than before. The GPGPU is occupied with other tasks, and unable to 
# to dedicate on the task at hand.
"""
====================8k n_jobs default====================
SVC CV score: [0.96111111 0.95416667 0.96111111 0.96527778 0.95416667 0.95277778
 0.95972222 0.96388889 0.95833333 0.96111111]
SVC CV score: [0.96111111 0.95416667 0.96111111 0.96527778 0.95416667 0.95277778
 0.95972222 0.96388889 0.95833333 0.96111111]
38 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

SVC(kernel="linear") CV score: [0.91666667 0.91805556 0.92916667 0.93888889 0.92361111 0.9
 0.91527778 0.92083333 0.92222222 0.92777778]
SVC(kernel="linear") CV score: [0.91666667 0.91805556 0.92916667 0.93888889 0.92361111 0.9
 0.91527778 0.92083333 0.92222222 0.92777778]
19 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

Linear SVC CV score: [0.86805556 0.86805556 0.84583333 0.89166667 0.85833333 0.85416667
 0.87083333 0.84444444 0.85       0.86111111]
Linear SVC CV score: [0.86111111 0.86666667 0.85833333 0.86944444 0.86111111 0.85416667
 0.87083333 0.84583333 0.84861111 0.87361111]
18.9 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

Logistic Regression CV score: [0.88472222 0.86111111 0.88611111 0.90416667 0.875      0.86944444
 0.88333333 0.87361111 0.86944444 0.87916667]
Logistic Regression CV score: [0.88472222 0.86111111 0.88611111 0.90416667 0.875      0.86944444
 0.88333333 0.87361111 0.86944444 0.87916667]
10.4 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

KNN CV score: [0.94861111 0.94444444 0.94444444 0.94305556 0.94722222 0.95138889
 0.95138889 0.95416667 0.94444444 0.94027778]
KNN CV score: [0.94861111 0.94444444 0.94444444 0.94305556 0.94722222 0.95138889
 0.95138889 0.95416667 0.94444444 0.94027778]
1.38 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

Decision Tree CV score: [0.78194444 0.78055556 0.7875     0.83333333 0.79305556 0.80972222
 0.81944444 0.80833333 0.80555556 0.79583333]
Decision Tree CV score: [0.78888889 0.79722222 0.77083333 0.83472222 0.79861111 0.80694444
 0.82916667 0.8        0.80416667 0.80555556]
7.31 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

====================8k n_jobs=-1====================
SVC CV score: [0.96111111 0.95416667 0.96111111 0.96527778 0.95416667 0.95277778
 0.95972222 0.96388889 0.95833333 0.96111111]
SVC CV score: [0.96111111 0.95416667 0.96111111 0.96527778 0.95416667 0.95277778
 0.95972222 0.96388889 0.95833333 0.96111111]
15.6 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

SVC(kernel="linear") CV score: [0.91666667 0.91805556 0.92916667 0.93888889 0.92361111 0.9
 0.91527778 0.92083333 0.92222222 0.92777778]
SVC(kernel="linear") CV score: [0.91666667 0.91805556 0.92916667 0.93888889 0.92361111 0.9
 0.91527778 0.92083333 0.92222222 0.92777778]
8.65 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

Linear SVC CV score: [0.87083333 0.85833333 0.85138889 0.88055556 0.86388889 0.85555556
 0.87638889 0.83611111 0.85416667 0.875     ]
Linear SVC CV score: [0.85       0.85833333 0.85833333 0.87361111 0.85555556 0.84166667
 0.86388889 0.84861111 0.85138889 0.86944444]
4.56 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

Logistic Regression CV score: [0.88472222 0.86111111 0.88611111 0.90416667 0.875      0.86944444
 0.88333333 0.87361111 0.86944444 0.87916667]
Logistic Regression CV score: [0.88472222 0.86111111 0.88611111 0.90416667 0.875      0.86944444
 0.88333333 0.87361111 0.86944444 0.87916667]
3.44 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

KNN CV score: [0.94861111 0.94444444 0.94444444 0.94305556 0.94722222 0.95138889
 0.95138889 0.95416667 0.94444444 0.94027778]
KNN CV score: [0.94861111 0.94444444 0.94444444 0.94305556 0.94722222 0.95138889
 0.95138889 0.95416667 0.94444444 0.94027778]
748 ms ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

Decision Tree CV score: [0.79027778 0.78888889 0.78194444 0.81666667 0.78472222 0.81388889
 0.81388889 0.8        0.79861111 0.79861111]
Decision Tree CV score: [0.78194444 0.78333333 0.78472222 0.83888889 0.80416667 0.80694444
 0.81805556 0.79583333 0.81388889 0.80277778]
1.28 s ± 0 ns per loop (mean ± std. dev. of 1 run, 1 loop each)

"""

# %%
