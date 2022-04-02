# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import dm6103 as dm

# The dataset is obtained from 
# https://gssdataexplorer.norc.org 
# for you here. But if you are interested, you can try get it yourself. 
# create an account
# create a project
# select these eight variables: 
# ballot, id, year, hrs1 (hours worked last week), marital, 
# childs, income, happy, 
# (use the search function to find them if needed.)
# add the variables to cart 
# extract data 
# name your extract
# add all the 8 variables to the extract
# Choose output option, select only years 2000 - 2018 
# file format Excel Workbook (data + metadata)
# create extract
# It will take some time to process. 
# When it is ready, click on the download button. 
# you will get a .tar file
# if your system cannot unzip it, google it. (Windows can use 7zip utility. Mac should have it (tar function) built-in.)
# Open in excel (or other comparable software), then save it as csv
# So now you have Happy table to work with
#
# When we import using pandas, we need to do pre-processing like what we did in class
# So clean up the columns. You can use some of the functions we defined in class, like the total family income, and number of children. 
# Other ones like worked hour last week, etc, you'll need a new function. 
# Happy: change it to numeric codes (ordinal variable)
# Ballot: just call it a, b, or c 
# Marital status, it's up to you whether you want to rename the values. 
# 
#
# After the preprocessing, make these plots
# Box plot for hours worked last week, for the different marital status. (So x is marital status, and y is hours worked.) 
# Violin plot for income vs happiness,
# Use happiness as numeric, make scatterplot with jittering in both x and y between happiness and number of children. Choose what variable you want for hue/color.
# If you have somewhat of a belief that happiness is caused/determined/affected by number of children, or the other 
# way around (having babies/children are caused/determined/affected by happiness), then put the dependent 
# variable in y, and briefly explain your choice.

dfhappy = dm.api_dsLand('Happy')

#%%
# checking the values of each column to create functions specific to process the current the data set
# dfhappy.column_name.value_counts(dropna=False)

# clean up ballet column name to ballot
dfhappy.rename({'ballet': 'ballot'}, axis=1, inplace=True)


# %%
def clean_df_any(row, col):
    curr_row = row[col].strip()
    try:
        curr_row = int(curr_row)
        return curr_row
    except ValueError:
        pass
    if curr_row == "Eight or m":
        return min(8 + np.random.chisquare(2), 12)
    if curr_row == "Not applicable":
        return np.nan
    if curr_row == "Dk na":
        return np.nan
    if curr_row == "No answer":
        return np.nan
    return curr_row


def clean_df_income(row):
    curr_row = row['income'].strip()
    if curr_row == "Don't know":
        return np.nan
    if curr_row == "No answer":
        return np.nan
    if curr_row == "Refused":
        return np.nan
    if curr_row == "Lt $1000":
        return np.random.uniform(0, 999)
    if curr_row == "$1000 to 2999":
        return np.random.uniform(1000, 2999)
    if curr_row == "$3000 to 3999":
        return np.random.uniform(3000, 3999)
    if curr_row == "$4000 to 4999":
        return np.random.uniform(4000, 4999)
    if curr_row == "$5000 to 5999":
        return np.random.uniform(5000, 5999)
    if curr_row == "$6000 to 6999":
        return np.random.uniform(6000, 6999)
    if curr_row == "$7000 to 7999":
        return np.random.uniform(7000, 7999)
    if curr_row == "$8000 to 9999":
        return np.random.uniform(8000, 9999)
    if curr_row == "$10000 - 14999":
        return np.random.uniform(10000, 14999)
    if curr_row == "$15000 - 19999":
        return np.random.uniform(15000, 19999)
    if curr_row == "$20000 - 24999":
        return np.random.uniform(20000, 24999)
    if curr_row == "$25000 or more":
        return 25000 + 10000 * np.random.chisquare(2)
    return np.nan


def clean_df_happy(row):
    curr_row = row['happy'].strip()
    if curr_row == "Don't know":
        return np.nan
    if curr_row == "No answer":
        return np.nan
    if curr_row == "Not applicable":
        return np.nan
    if curr_row == "Not too happy":
        return 0
    if curr_row == "Pretty happy":
        return 1
    if curr_row == "Very happy":
        return 2
    return np.nan


def clean_df_ballot(row):
    curr_row = row['ballot'].strip()[-1:]
    return curr_row


print("\nReady to continue.")
#%%
# preprocess data
#hrs1 column should be numeric not object type
dfhappy['hrs1'] = dfhappy.apply(clean_df_any, col='hrs1', axis=1)
dfhappy['hrs1'] = pd.to_numeric(dfhappy['hrs1'], errors='coerce')

dfhappy['marital'] = dfhappy.apply(clean_df_any, col='marital', axis=1)

#childs should not be decimals, round up any decimal number
dfhappy['childs'] = dfhappy.apply(clean_df_any, col='childs', axis=1)
dfhappy['childs'] = dfhappy['childs'].apply(np.ceil)

dfhappy['income'] = dfhappy.apply(clean_df_income, axis=1)

dfhappy['happy'] = dfhappy.apply(clean_df_happy, axis=1)

dfhappy['ballot'] = dfhappy.apply(clean_df_ballot, axis=1)

#%%
# boxplot hours worked last week v. marital status
sns.set_palette('Set2')
sns.boxplot(x='marital', y='hrs1', data=dfhappy)
plt.title("Hours Worked Last Week vs. Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Hours Worked Last Week")
plt.show()

#%%
# violin plot income v. happiness
sns.set_palette('Set2')
sns.violinplot(x='happy', y='income', data=dfhappy)
plt.title("Income vs. Happiness")
plt.xticks([0, 1, 2], ['Not too happy', 'Pretty happy', 'Very happy'])
plt.xlabel("Happiness Level")
plt.ylabel("Income")
plt.show()

#%%
# scatter plot happiness v. number of children by marital
sns.set_palette('Set2')
sns.lmplot(x='childs', y='happy', data=dfhappy, x_jitter=0.4,y_jitter=0.2, fit_reg=False, hue='marital', legend=False)
plt.title("Happiness vs. Number of Children")
plt.xlabel("Number of Children")
plt.ylabel("Happiness Level")
plt.legend(title='Marital Status', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.yticks(np.arange(0,3,1))
plt.xticks(np.arange(0,13,1))
plt.show()


#%%

