#%%[markdown]
# You may use web search, notes, etc. 
# Do not use help from another human. If you use help from another student, 
# then I have no choice but to consider that student not a human, and will be 
# booted off my class immediately. You will also arrive at the same fate.
# 
#%%
import pandas as pd
import dm6103 as dm
df = dm.api_dsLand('Diet6wk','Person')
df.columns.values[3] = 'origweight'
#df.info()

print(df)
#%%
# The dataframe is on a person's weight 6 weeks after starting a diet. 
# Build these models:
# 
# 1. Using statsmodels library, build a linear model for the wight6weeks as a function of the other variables. Use gender and Diet as categorical variables. Print out the model summary. What is the r-squared value of the model?  
# 
# R-squared = 0.927
#
from statsmodels.formula.api import ols
model1 = ols(formula='weight6weeks ~ Age + origweight + Height + gender + Diet', data=df)
print( type(model1) )

model1_Fit = model1.fit()
print( type(model1_Fit) )
print( model1_Fit.summary() )



#%%
# 2. Again using the statsmodels library, build a multinomial-logit regression model for the Diet (3 levels) as a function of the other variables. Use gender as categorical again. Print out the model summary. What is the  model's "psuedo r-squared" value?  
# 
# from statsmodels.formula.api import glm
from statsmodels.formula.api import mnlogit  # use this for multinomial logit in statsmodels library, instead of glm for binomial.
# Sample use/syntax:
# model = mnlogit(formula, data)
#
# psuedo r-squared 0.09026
#
model2 = mnlogit(formula='pd.to_numeric(Diet) ~ weight6weeks + Age + origweight + Height + gender', data=df)

model2_Fit = model2.fit()
print( model2_Fit.summary() )



#%%
# 3a. Use SKLearn from here onwards. 
# Use a 2:1 split, set up the training and test sets for the dataset, with Diet as y, and the rest as Xs. Use the seed value/random state as 1234 for the split.
#
from sklearn.model_selection import train_test_split

X_train1, X_test1, y_train1, y_test1 = train_test_split(x, Diet, test_size = 2:1, random_state=1234)
full_split1 = linear_model.LinearRegression()
full_split1.fit(X_train1, y_train1)
y_pred1 = full_split1.predict(X_test1)
full_split1.score(X_test1, y_test1)

print('score (train):', full_split1.score(X_train1, y_train1))
print('score (test):', full_split1.score(X_test1, y_test1))
print('intercept:', full_split1.intercept_) 
print('coef_:', full_split1.coef_) 


#%%
# 
# 3b. Build the corresponding logit regression as in Q2 here using sklearn. Train and score it. What is the score of your model with the training set and with the test set?
# 

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train1, y_train1)
lr.score(X_test1, y_test1)


#%%
# 4. Using the same training dataset, now use a 3-NN model, score the model with the training and test datasets. 
# 
from sklearn.neighbors import KNeighborsClassifier
knn_cv = KNeighborsClassifier(n_neighbors=df)

from sklearn.model_selection import cross_val_score
cv_results1 = cross_val_score(knn_cv, X_train1, y_train1, cv=10)
print(cv_results1) 
print(np.mean(cv_results1)) 


cv_results2 = cross_val_score(knn_cv, X_test1, y_test1, cv=10)
print(cv_results2) 
print(np.mean(cv_results2)) 


#%%
