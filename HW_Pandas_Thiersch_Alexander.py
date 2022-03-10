# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

# %% [markdown]
#
# # HW Pandas
# ## By: Alexander Thiersch
# ### Date: 03/10/2022
#

# %% [markdown]
# Let us improve our Stock exercise and grade conversion exercise with Pandas now.
#

# %%
from turtle import color
import dm6103 as dm
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Load the data frame from api
dfaapl = dm.api_dsLand('AAPL_daily', 'date')
print("\nReady to continue.")


# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########

# What are the variables in the df?
dfaapl.keys()
# The variables in the df are price and volume.

# What are the data types for these variables?
dfaapl.price
dfaapl.volume
# The price variable is a float data type.
# The volume variable is a int64 data type.


# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########

# %%
# You can access pd dataframe columns using the dot notation as well as using column names
print(dfaapl.price, '\n')
# same as
print(dfaapl['price'])


# %%
# Step 1
# Create the Stock class
#

class Stock:
    """
    Stock class of a publicly traded stock on a major market
    """
    import dm6103 as dm
    import os
    import numpy as np
    import pandas as pd

    def __init__(self, symbol, name, init_tbname):
        """
        :param symbol: stock symbol
        :param name: company name
        :param init_tbname: the initial table name on our DSLand API with historical data. Date is index, with eod price and vol as columns.
        """
        # note that the complete list of properties/attributes below has more than items than
        # the numnber of arguments of the constructor. That's perfectly fine.
        # Some property values are to be assigned later after instantiation.
        self.symbol = symbol.upper()
        self.name = name
        # this is a pandas df, make sure import_history() returns a pd dataframe
        self.data = self.import_history(init_tbname)
        # the pandas df self.data will have columns price, volume, delta1, delta2, and index is date
        # Calculate the daily change values from stock price itself, append to df
        self.init_delta1()
        self.init_delta2()  # Calculate the daily values second derivative, append to df
        self.firstdate = self.data.index[-1]
        self.lastdate = self.data.index[0]

    def import_history(self, tbname):
        """
        import stock history from api_dsLand, with colunms date, eod_price, volume
        """
        return dm.api_dsLand(tbname, 'date')  # use date as index

    def init_delta1(self):
        """
        compute the daily change from price_eod, append to data as new column as delta1
        """
        # notice that:
        # aapl['price'] returns a pandas series
        # aapl[['price']] returns a pandas dataframe
        # aapl['price'].values returns a numpy array of the values only

        self.data['delta1'] = 0  # initialize a new column with 0s
        # self.data['price'] is same as self.price for df
        self.data['delta1'] = self.data['price'][0:-1] - \
            self.data.price.values[1:]
        # the first term on the right is the full pd series with index attached. Second one is a simple numpy array without the date
        # index. That way, the broadcasting will not try to match the indices/indexes on the two df
        return  # you can choose to return self

    def init_delta2(self):
        """
        compute the daily change for the entire list of delta1, essentially the second derivatives for price_eod
        """
        # essentially the same function as init_delta1.

        # ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########

        # write your codes here
        self.data['delta2'] = 0
        self.data['delta2'] = self.data['delta1'][0:-1] - \
            self.data.delta1.values[1:]

        # ######  END of QUESTION 2    ###   END of QUESTION 2   ##########

        return self  # you can choose to return self

    def add_newday(self, newdate, newprice, newvolume):
        """
        add a new data point at the beginning of data df
        """
        # Make plans
        # insert a new row to self.data with
        # (date, price, volume, delta1, delta2) to the pandas df,
        # and also should update self.lastdate
        #

        # update self.lastdate
        # ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########

        # write your codes here, should be just one line
        self.lastdate = newdate

        # ######  END of QUESTION 3    ###   END of QUESTION 3   ##########

        # get ready a new row, in the form of a pandas dataframe.
        # Pandas dataframe does not have an insert function. The usual method is to use .append()
        # and .append() is most efficient to append a df to another df of the same columns.
        # we do this quite a lot: assume it's done already, then implement it later, as long as it doesn't break the codes
        newRow = self.setNewRow(newdate, newprice, newvolume)
        # need this function setNewRow() to return a dataframe

        # this will put the new row on top, and push self.data after the new data
        self.data = newRow.append(self.data)

        return self

    def setNewRow(self, newdate, newprice, newvolume):
        # first create a true copy of the first row
        df = self.data.iloc[[0]].copy()
        # use iloc[[0]] to create a dataframe, instead of iloc[0,:] which results in a Pandas.Series
        # then put in the new values
        # df.index[0] = newdate # doesn't work. Pandas index is immutable.
        df.index = [newdate]  # Can change the entire series of index however.
        df.price[0] = newprice
        # ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########

        # write your codes here
        df.volume[0] = newvolume  # set volume value
        df.delta1[0] = newprice - self.data.price.values[0]  # set delta1 value
        df.delta2[0] = df.delta1[0] - \
            self.data.delta1.values[0]  # set delta2 value

        # ######  END of QUESTION 4    ###   END of QUESTION 4   ##########
        return df  # return the dataframe with one one row of data

    def nday_change_percent(self, n):
        """
        calculate the percentage change in the last n days, returning a percentage between 0 and 100
        """
        # ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########

        change = self.data['price'][0] - self.data['price'][n]  # change = ??
        percent = change / self.data['price'][n] * 100  # percent = ??

        # ######  END of QUESTION 5    ###   END of QUESTION 5   ##########
        print(self.symbol, ": Percent change in",
              n, "days is {0:.2f}".format(percent))
        return percent  # percent ??

    def nday_max_price(self, n):
        """
        find the highest price within the last n days 
        """
        # ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########

        # return ??  # you can try to use the .max() function of a pandas dataframe

        return self.data['price'][0:n + 1].max()
        # ######  END of QUESTION 6    ###   END of QUESTION 6   ##########

    def nday_min_price(self, n):
        """
        find the lowest price within the last n days 
        """
        # ######  QUESTION 7      QUESTION 7      QUESTION 7   ##########

        # return ??
        return self.data['price'][0:n + 1].min()

        # ######  END of QUESTION 7    ###   END of QUESTION 7   ##########


# %%
# ######  QUESTION 8      QUESTION 8      QUESTION 8   ##########
# Try these:
filename = 'AAPL_daily'
aapl = Stock('AAPL', 'Apple Inc', filename)
aapl.data.head()  # record the answer here:
"""
	         price	volume	delta1	delta2
date				
9/12/19	223.085	32226670	-0.505	-7.395
9/11/19	223.590	44289650	6.890	4.360
9/10/19	216.700	31777930	2.530	1.620
9/9/19	214.170	27309400	0.910	0.930
9/6/19	213.260	19362290	-0.020	-4.110
"""

aapl.data.tail()  # record the answer here:
"""
	      price	volume	delta1	delta2
date				
9/18/14	101.79	36971170	0.21	-0.51
9/17/14	101.58	60783090	0.72	1.49
9/16/14	100.86	66754370	-0.77	-0.74
9/15/14	101.63	61169670	-0.03	NaN
9/12/14	101.66	62826040	NaN	NaN
"""

aapl.nday_max_price(333)  # record the answer here: 232.07

aapl.nday_min_price(500)  # record the answer here: 142.19

aapl.nday_change_percent(500)  # record the answer here: 39.53%

aapl.add_newday('9/13/19', 218.42, 12345678)  # record the answer here
aapl.data.head()
"""
	        price	volume	delta1	delta2
9/13/19	218.420	12345678	-4.665	-4.160
9/12/19	223.085	32226670	-0.505	-7.395
9/11/19	223.590	44289650	6.890	  4.360
9/10/19	216.700	31777930	2.530	  1.620
9/9/19	214.170	27309400	0.910	  0.930
"""

# ######  END of QUESTION 8    ###   END of QUESTION 8   ##########


# %%
# Next, re-solve the grade-changing exercise (calculating GPA)
#
# %%
dats = dm.api_dsLand('Dats_grades')
dm.dfChk(dats)


# %%
# What are the variables in the df?
# The variables in the dataframe are H1, H2, H3, H4, H5, H6, H7, H8, Q1, Q2, Proj1, and Proj2.

# What are the data types for these variables?
# The data type for all the variables is float.

# The file has grades for a DATS class. Eight homeworks (out of 10 each), 2 quizzes (out of 100 each), and 2 projects (out of 100 each)
# Find out the class average for each item (HW, quiz, project)
# Hint, use .mean() function of pandas dataframe

# ######  QUESTION 9      QUESTION 9      QUESTION 9   ##########

# write your codes here
dats.mean()

"""
Mean for each item (HW, Quiz, Project)
H1        9.817204
H2        9.834409
H3        9.811828
H4        9.895699
H5        9.803226
H6        9.676344
H7        9.769892
H8        9.823656
Q1       85.114753
Q2       84.882299
Proj1    94.730108
Proj2    92.662118
"""

# ######  END of QUESTION 9    ###   END of QUESTION 9   ##########

# %%
# create a new column right after the last hw column, to obtain the average HW grade.
# use column name HWavg. Make the average out of the total of 100.
# Hint: use .iloc to select the HW columns, and then use .mean(axis=1) to find the row average

# ######  QUESTION 10      QUESTION 10      QUESTION 10   ##########

# write your codes here
dats.insert(8, 'HWavg', dats.iloc[:, 0:8].mean(axis=1))


# ######  END of QUESTION 10    ###   END of QUESTION 10   ##########

dats.head()  # check result


# %%
# The course total = 30% HW, 10% Q1, 15% Q2, 20% Proj1, 25% Proj2.
# Calculate the total and add to the df as the last column, named 'total', out of 100 max.

# ######  QUESTION 11      QUESTION 11      QUESTION 11   ##########

# write your codes here
dats['total'] = (dats.HWavg * 8 * 0.30) + dats.Q1 * 0.10 + \
    dats.Q2 * 0.15 + dats.Proj1 * 0.20 + dats.Proj2 * 0.25

# ######  END of QUESTION 11    ###   END of QUESTION 11   ##########

dats.head()  # check result

# %%
# Now with the two new columns, calculate the class average for everything again.

# ######  QUESTION 12      QUESTION 12      QUESTION 12   ##########

# write your codes here
dats.mean()  # for everything

"""
New Mean for each item (HW, Quiz, Project)
H1        9.817204
H2        9.834409
H3        9.811828
H4        9.895699
H5        9.803226
H6        9.676344
H7        9.769892
H8        9.823656
HWavg     9.804032
Q1       85.114753
Q2       84.882299
Proj1    94.730108
Proj2    92.662118
total    86.885049
"""


# Calculate specific
HWavg_class = dats['HWavg'].mean()
total_class = dats['total'].mean()

# ######  END of QUESTION 12    ###   END of QUESTION 12   ##########

# %%
# Save out your dataframe as a csv file
# import os

# ######  QUESTION 13      QUESTION 13      QUESTION 13   ##########

# write your codes here
dats.to_csv('dats.csv')


# ######  END of QUESTION 13    ###   END of QUESTION 13   ##########


# %%
# Finally, re-solve our homework exercise for calculating GPA using functions, but with a dataframe now.
# In Week03 hw, we wrote a function to convert course total to letter grades. You can use your own, or the one from the solution file here.
def find_grade(total):
    # write an appropriate and helpful docstring
    """
    convert total score into grades
    :param total: 0-100 
    :return: str
    """
    # ######  QUESTION 14      QUESTION 14      QUESTION 14   ##########

    # copy your codes here, either from your Week03 hw, or the solution file
    if total < 60:
        grade = "F"
    elif total < 70:
        grade = "D"
    elif total < 73:
        grade = "C-"
    elif total < 77:
        grade = "C"
    elif total < 80:
        grade = "C+"
    elif total < 83:
        grade = "B-"
    elif total < 87:
        grade = "B"
    elif total < 90:
        grade = "B+"
    elif total < 93:
        grade = "A-"
    elif total < 100:
        grade = "A"

    # ######  END of QUESTION 14    ###   END of QUESTION 14   ##########
    return grade  # grade

# %%
# Let us create one more column for the letter grade, just call it grade.
# Instead of broadcasting some calculations on the dataframe directly, we need to apply (instead of broadcast) this find_grade()
# function on all the elements in the total column
# ######  QUESTION 15      QUESTION 15      QUESTION 15   ##########


dats['grade'] = dats['total'].apply(find_grade)

# write your code using the .apply() function to obtaine a new column of letter grade (call that new column 'grade') from the total.

# ######  END of QUESTION 15    ###   END of QUESTION 15   ##########


# %%
# Create a bar chart for the grade distribution
# Save your chart out to a file as an image.
# Hint: use .value_counts() on the grade column to make a bar plot

# ######  QUESTION 16      QUESTION 16      QUESTION 16   ##########

# write your codes here
grade_value_counts = dats.grade.value_counts().sort_index(ascending=True)

grade_value_counts.keys()

grade_value_counts.values

plt.bar(grade_value_counts.keys(), grade_value_counts.values, color='green')
plt.title('Bar Chart of Grade Distribution', color='white')
plt.xlabel('Letter Grade', color='white')
plt.ylabel('Letter Grade Frequency', color='white')
plt.tick_params(axis='x', colors='white')  
plt.tick_params(axis='y', colors='white')
plt.show()


# ######  END of QUESTION 16    ###   END of QUESTION 16   ##########


# %%
