# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
# Name: Alexander Thiersch\
# Date: 03/22/2022\
# DATS 6103\
# Midterm

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dm6103 as dm

world1 = dm.api_dsLand('World1', 'id')
world2 = dm.api_dsLand('World2', 'id')

print("\nReady to continue.")


#%% [markdown]
# # Two Worlds 
# 
# I was searching for utopia, and came to this conclusion: If you want to do it right, do it yourself. 
# So I created two worlds. 
#
# Data dictionary:
# * age00: the age at the time of creation. This is only the population from age 30-60.  
# * education: years of education they have had. Education assumed to have stopped. A static data column.  
# * marital: 0-never married, 1-married, 2-divorced, 3-widowed  
# * gender: 0-female, 1-male (for simplicity)  
# * ethnic: 0, 1, 2 (just made up)  
# * income00: annual income at the time of creation   
# * industry: (ordered with increasing average annual salary, according to govt data.)   
#   0. leisure n hospitality  
#   1. retail   
#   2. Education   
#   3. Health   
#   4. construction   
#   5. manufacturing   
#   6. professional n business   
#   7. finance   
# 
# 
# Please do whatever analysis you need, convince your audience both, one, or none of these 
# worlds is fair, or close to a utopia. 
# Use plots, maybe pivot tables, and statistical tests (optional), whatever you deem appropriate 
# and convincing, to draw your conclusions. 
# 
# There are no must-dos (except plots), should-dos, cannot-dos. The more convenicing your analysis, 
# the higher the grade. It's an art.
#

#%% [markdown]
# # Introduction
#
# The following project attemps to determine which world between World 1 and World 2 is more "utopian". 
# A "utopian" world will be defined by how equal it is.
# For example, with respect to gender, ethnicity, and marital status, does each categorical variable exhibit a distinct differences in annual income? Or is annual income equally distributed among gender, ethnicity, and marital status?
# In other words, a more "utopian" society is a more equal society.
# The project is divided into multiple sections with various plots that attempt to visualize the equality or inequality in each world. 
#
# # Table of Contents
# Section 1: Summary statistics of all the variables in World 1 and World 2
#
# Section 2: Histograms of each variable per world with an overlayed kernal density plot
# 
# Section 3: Boxplots of relevant related numeric and caregorical variables
#
# Section 4: Scatterplots of relevant numeric variables colored by categrorical variable
#
# Section 5: Barplots of relevant numeric variables colored by a categrorical variable
#
# Seciont 6: Conlusion

#%% [markdown]
# # Section 1: Summary Statisitcs
#
# The following section below provides basic summary statisitcs for all the variables in World 1 and World 2.

#%%
# World 1
# summary statistics of each world
world1_summary = world1.describe()
"""
              age00     education       marital        gender        ethnic      industry       income00
count  24000.000000  24000.000000  24000.000000  24000.000000  24000.000000  24000.000000   24000.000000
mean      44.292292     15.074750      0.881167      0.494042      1.001542      3.339958   60642.159542
std        8.264683      2.888239      0.795291      0.499975      0.816436b     2.228642   28104.324971
min       30.001000      0.000000      0.000000      0.000000      0.000000      0.000000   19928.000000
25%       37.193000     13.000000      0.000000      0.000000      0.000000      1.000000   38990.500000
50%       44.267500     16.000000      1.000000      0.000000      1.000000      3.000000   53923.500000
75%       50.994750     16.000000      1.000000      1.000000      2.000000      5.000000   75373.250000
max       59.999000     22.000000      3.000000      1.000000      2.000000      7.000000  162668.000000
"""

#%%
# World 2
world2_summary = world2.describe()
"""
              age00     education       marital        gender        ethnic      industry       income00
count  24000.000000  24000.000000  24000.000000  24000.000000  24000.000000  24000.000000   24000.000000
mean      44.310798     15.105417      0.887208      0.487083      1.000958      3.349458   60634.731750
std        8.249013      2.828157      0.801673      0.499844      0.815619      2.228743   28195.281599
min       30.001000      0.000000      0.000000      0.000000      0.000000      0.000000   19680.000000
25%       37.249750     13.000000      0.000000      0.000000      0.000000      1.000000   38927.000000
50%       44.298000     16.000000      1.000000      0.000000      1.000000      3.000000   53521.500000
75%       51.063250     16.000000      1.000000      1.000000      2.000000      5.000000   76042.250000
max       59.995000     22.000000      3.000000      1.000000      2.000000      7.000000  161737.000000
"""
#%% [markdown]
# # Section 2: Histograms
#
# The following section below provides histograms for all the variables in World 1 and World 2. 
# These histograms were plotted in order to gain a better understanding of the distribution of the data within each variable within each world.
#
#%% [markdown]
# # Histograms for Age
#
# The following histgrams below display the distribution of age for both World 1 and World 2. 
# These histograms show that there is a wide range and frequencies of ages between World 1 and World 2. 
# Neither age histogram appears to be extrememly skewed or severely different between each world, indicating that each world has a similar distribution of all ages.


#%%
# world1.age00
sns.histplot(world1['age00'], bins=30, stat='density', edgecolor="white", color='#ADD8E6')
sns.kdeplot(world1['age00'], color='#528AAE')
plt.title("World 1: Age Distribution")
plt.xlabel('Age (years)')
plt.ylabel('Density')
plt.show()

# world 2
# world2.age00
sns.histplot(world2['age00'], bins=30, stat='density', edgecolor="white", color='#ADD8E6')
sns.kdeplot(world2['age00'], color='#528AAE')
plt.title("World 2: Age Distribution")
plt.xlabel('Age (years)')
plt.ylabel('Density')
plt.show()

#%% [markdown]
# # Histograms for Education
#
# The following histgrams below display the distribution of education for both World 1 and World 2. 
# The histograms between World 1 and World 2 display extremely similar distributions.
# These histograms show that there is left-tailed skewness in the distribution for both World 1 and World 2.
# Additionally, both histograms peak at approximately 15 years of education.
# Thes histograms suggest World 1 and World 2 have similar education distributions and that a lot of people have at least 10 to 15 years of education.


#%%
# world1.education
sns.histplot(world1['education'], bins=15, stat='density', edgecolor="white", color='#FEDEBE')
sns.kdeplot(world1['education'], color='#FE6E00')
plt.title("World 1: Education Distribution")
plt.xlabel('Education (years)')
plt.ylabel('Density')
plt.show()

# world2.education
sns.histplot(world2['education'], bins=15, stat='density', edgecolor="white", color='#FEDEBE')
sns.kdeplot(world2['education'], color='#FE6E00')
plt.title("World 2: Education Distribution")
plt.xlabel('Education Length (years)')
plt.ylabel('Density')
plt.show()

#%% [markdown]
# # Histograms for Marital Status
#
# The following histgrams below display the distribution of marital status for both World 1 and World 2. 
# The histograms between World 1 and World 2 display extremely similar distributions.
# These histograms for both World 1 and World 2 peak when maritial status equals 1 indicating that the majority of people are married in both worlds.
# These histograms suggest that World 1 and World 2 have similar distributions of the different types of marital statuses.


#%%
# world1.marital
sns.histplot(world1['marital'], bins=4, stat='density', edgecolor="white", color='#F2B8C6')
sns.kdeplot(world1['marital'], color='#FE7F9C')
plt.title("World 1: Marital Distribution")
plt.xlabel('Marital Status')
plt.ylabel('Density')
plt.show()

# world2.marital
sns.histplot(world2['marital'], bins=4, stat='density', edgecolor="white", color='#F2B8C6')
sns.kdeplot(world2['marital'], color='#FE7F9C')
plt.title("World 2: Marital Distribution")
plt.xlabel('Marital Status')
plt.ylabel('Density')
plt.show()


#%% [markdown]
# # Histograms for Gender
#
# The following histgrams below display the distribution of gender for both World 1 and World 2. 
# The histograms between World 1 and World 2 display extremely similar distributions.
# These histograms for both World 1 and World 2 peak similary when gender equals 0 and 1.
# These histograms suggest that World 1 and World 2 have a similar distribution of both males and female genders. 

#%%
# world1.gender
sns.histplot(world1['gender'], bins=2, stat='density', edgecolor="white", color='#BE93D4')
sns.kdeplot(world1['gender'], color='#7A4988')
plt.title("World 1: Gender Distribution")
plt.xlabel('Gender')
plt.ylabel('Density')
plt.show()

# world2.gender
sns.histplot(world2['gender'], bins=2, stat='density', edgecolor="white", color='#BE93D4')
sns.kdeplot(world2['gender'], color='#7A4988')
plt.title("World 2: Gender Distribution")
plt.xlabel('Gender')
plt.ylabel('Density')
plt.show()

#%% [markdown]
# # Histograms for Ethnicity
#
# The following histgrams below display the distribution of ethnicity for both World 1 and World 2. 
# The histograms between World 1 and World 2 display extremely similar distributions.
# These histograms for both World 1 and World 2 peak similary when ethnicity equals 0, 1, and 2.
# These histograms suggest that World 1 and World 2 have a similar distribution of all the different types of ethnicities. 

#%%
# world1.ethnic
sns.histplot(world1['ethnic'], bins=3, stat='density', edgecolor="white", color='#FDEE87')
sns.kdeplot(world1['ethnic'], color='#FFC30B')
plt.title("World 1: Ethnicity Distribution")
plt.xlabel('Ethnicity')
plt.ylabel('Density')
plt.show()

# world2.ethnic
sns.histplot(world2['ethnic'], bins=3, stat='density', edgecolor="white", color='#FDEE87')
sns.kdeplot(world2['ethnic'], color='#FFC30B')
plt.title("World 2: Ethnic Distribution")
plt.xlabel('Ethnicity')
plt.ylabel('Density')
plt.show()

#%% [markdown]
# # Histograms for Industry
#
# The following histgrams below display the distribution of industry for both World 1 and World 2. 
# The histograms between World 1 and World 2 display extremely similar distributions.
# These histograms suggest that World 1 and World 2 have a similar distribution of all the different types of industries.

#%%
# world1.industry
sns.histplot(world1['industry'], bins=8, stat='density', edgecolor="white", color='#D3D3D3')
sns.kdeplot(world1['industry'], color='#808080')
plt.title("World 1: Industry Distribution")
plt.xlabel('Industry')
plt.ylabel('Density')
plt.show()

# world2.industry
sns.histplot(world2['industry'], bins=8, stat='density', edgecolor="white", color='#D3D3D3')
sns.kdeplot(world2['industry'], color='#808080')
plt.title("World 2: Industry Distribution")
plt.xlabel('Industry')
plt.ylabel('Density')
plt.show()

#%% [markdown]
# # Histograms for Income
#
# The following histgrams below display the distribution of income for both World 1 and World 2. 
# The histograms between World 1 and World 2 display extremely similar distributions.
# The histograms both exhibit right tailed-skewness, indicating that the majority of people in both World 1 and World 2 earn an annual income between $25,000 and $75,000.
# These histograms suggest that World 1 and World 2 have a similar distribution of income.
#%%
# world1.income00
sns.histplot(world1['income00'], bins=30, stat='density', edgecolor="white", color='#98BF64')
sns.kdeplot(world1['income00'], color='#597D35')
plt.title("World 1: Income Distribution")
plt.xlabel('Annual Income ($)')
plt.ylabel('Density')
plt.show()

# world2.income00
sns.histplot(world2['income00'], bins=30, stat='density', edgecolor="white", color='#98BF64')
sns.kdeplot(world2['income00'], color='#597D35')
plt.title("World 2: Income Distribution")
plt.xlabel('Annual Income ($)')
plt.ylabel('Density')
plt.show()
#%% [markdown]

# Given the histograms above, it appears that World 1 and World 2 have similar distributions of data across all variables within their repective datasets.
# However, these inital histograms do not necessary indicate that World 1 and World 2 are the same.
# Further analysis is required to determine which world is "better" or more "utopian" than the other.


#%% [markdown]
# # Section 3: Boxplots
#
# The following section below provides Boxplots for relevant the variables in World 1 and World 2. 
# These boxplots were plotted in order to gain a better understanding of the distribution of the data within each categorical variables in relation in numeric variables within each world.
#
#%% [markdown]
# # Boxplots: Income vs. Gender
#
# The Income vs. Gender boxplot for World 1 shows that men have a higher medain annual income, a larger interquartile range for annual income, and a higher maximum value for annual income relative to women.
# This indicates that men in World 1 within the annual income distribution of data make more money than women. Additionlly, the female boxplot plot in World 1 has a large number of large outliers above the maximum value, indicating that the higher salary range approximately above $120,000 is uncommon in the distrubution of annual income among females.
#
# However, in World 2 the boxplots visualizing the income distribution between males and females is very similar. This indicates that males and females in World 2 have a similar distribution in annual income. 
#
# Overall, what these boxplots indicate is that the distribution of income among males and females between the two worlds is starkly different.
# World 1 appears to have a an unequal distribution, whereas World 2 appears to have a equal distribution annual income among males and females.
#Given these boxplots World 2 appears to be more utopian than World 1.
#
#%%
# Boxplots Income vs. Gender
# World 1
sns.boxplot(x='gender', y='income00', data=world1, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World 1: Income vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# World 2
sns.boxplot(x='gender', y='income00', data=world2, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World 2: Income vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

#%% [markdown]
# # Boxplots: Income vs. Ethnicity
#
# The Income vs. Ethnicity boxplot for World 1 shows that there is an unequal distribution of annual income among ethnicity types. 
# In the World 1 boxplot enthicity type 1 has the lowest median annual income, enthicity type 0 has the second lowest annual income, and ethnicity type 2 has the highest median income.
# Additionally, ethnicity type 2 has the highest maximum value of annual income, which is approximately 160,000 and has a larger interquartile range consisting of higher annual incomes relative to ethnicity type 0 and 1.
# Furthermore, ethnicity types 0 and 1 have a large amount of outliers in the higher range of annual incomes, indicating that these annual incomes are uncommon within the main distribution of annual incomes among ethnicity 0 and 1.
#
# In World 2, the boxplots between ethnicity types 0, 1, and 2 and annual income all appear to be equal.
# Each ethnicity type appears to have an equal median annual incomes, interquartile ranges, maximum values, minimum values, and a similar number and position of outliers.
#
# Overall, what these boxplots indicate is that World 1 and World 2 

#%%
# Boxplot: Income vs. Ethnicity
# World 1
sns.boxplot(x='ethnic', y='income00', data=world1, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World 1: Income vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# World 2
sns.boxplot(x='ethnic', y='income00', data=world2, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World 2: Income vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

#%% [markdown]
# # Boxplots: Income vs. Marital Status
#
# The Income vs. Marital Status boxplot for World 1 shows a relative equal distribution of annual income among marital status.
# Additionally in World 1, all marital types appear to have the same median annual income.
# However in World 1, the widowed marital status type has a slightly lower maximum value and a lower interquartile range of annual income relative to the other marital status types.
# 
# In World 2, the boxplots between marital status types and income all appear to be relatively equal.
# Each ethnicity type appears to have an equal median annual incomes, interquartile ranges, maximum values, minimum values, and a similar number and position of outliers.
# However, in World 2 widowed marital status type has a slightly smaller interquartile range. 
#
# Overall, what these boxplots indicate is that World 1 and World 2 appear to have relatively equal distributions of annual income among marital status. 
# However, World 2 appears to be slightly more equal than World 1 because the World 2 widowed boxplot matches the rest of the marital status boxplots within World 2, particulary with respect to its maximum value..
# Whereas the World 1 widowed boxplot, has a slightly lower maximum value compared to the other marital status boxplots.
# This suggests that World 2 is more "utopian" than World 1, but not significantly. 
# Both World 1 and World 2 have similar and relatively equal distributions. 
#%%
# Boxplot: Income vs. Marital
# World 1
sns.boxplot(x='marital', y='income00', data=world1, palette=['#F7E654', '#F0AB00', '#5482AB', '#00B0CA'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1, 2, 3], ['Never-Married', 'Married', 'Divorced', 'Widowed'])
plt.title("World 1: Income vs. Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# World 2
sns.boxplot(x='marital', y='income00', data=world2, palette=['#F7E654', '#F0AB00', '#5482AB', '#00B0CA'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1, 2, 3], ['Never-Married', 'Married', 'Divorced', 'Widowed'])
plt.title("World 2: Income vs. Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

#%% [markdown]
# # Boxplots: Income vs. Industry
#
# The Income vs. Industry boxplot for World 1 and World 2 display similar distributions.
# In both worlds, the finance industry makes the most annual income and the leisrue/hospitality industry makes the least amount of annual income.
# The boxplot also indicates that there is a clear gradient between the type industry a person works in and the annual income received. 
#
#Overall, World 1 and World 2 have similar unequal distributions of annual income with respect to each industry type.
# Neither world is more "utopian" than the other. 

#%%
# Boxplot: Income vs. Industry
# World 1
sns.boxplot(y='income00', x='industry', data=world1, medianprops=dict(color='#00685B'))
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], ['Leisure/Hospitality', 'Retail', 'Education', 'Health', 'Construction', 'Manufacturing','Professional/Business', 'Finance'])
plt.xticks(rotation=45, ha='right')
plt.title("World 1: Income vs. Industry")
plt.xlabel("Industry")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# World 2
sns.boxplot(y='income00', x='industry', data=world2, medianprops=dict(color='#00685B'))
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], ['Leisure/Hospitality', 'Retail', 'Education', 'Health', 'Construction', 'Manufacturing','Professional/Business', 'Finance'])
plt.xticks(rotation=45, ha='right')
plt.title("World 2: Income vs. Industry")
plt.xlabel("Industry")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()
  

#%% [markdown]
# # Boxplots: Education vs. Gender
#
# The Education vs. Gender boxplot for World 1 and World 2 show a relative equal distribution between males and females and between worlds.
# Both worlds appear to a have the equal median incomes, interquartile ranges, minimum values, maximum values, and the position and number of outliers.
#
# Overall, both worlds have equal distributions of education among males and females.
# Neither world appears to be more "utopian" than the other.

#%%

# Boxplot: Education vs. Gender
# World 1
sns.boxplot(x='gender', y='education', data=world1, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World 1: Education vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()

# World 2
sns.boxplot(x='gender', y='education', data=world2, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World 2: Education vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()


#%% [markdown]
# # Boxplots: Education vs. Ethnicity
#
# The Education vs. Ethnicity boxplot for World 1 and World 2 show a relative equal distribution between each ethnicity type and between worlds.
# Both worlds appear to a have the equal median incomes, interquartile ranges, minimum values, maximum values, and the position and number of outliers between ethnicity types.
#
# Overall, both worlds have equal distributions of education among each ethnicity type.
# Neither world appears to be more "utopian" than the other.

#%%
# Boxplot: Education v. Ethnicity
# World 1
sns.boxplot(x='ethnic', y='education', data=world1, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World 1: Education vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()

# World 2
sns.boxplot(x='ethnic', y='education', data=world2, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World 2: Education vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()


#%% [markdown]
# # Section 4: Scatterplots
#
# The following section below provides scatterplots for relevant the numeric variables in World 1 and World 2. 
# These scatterplots were plotted in order to gain a better understanding of the trends and patterns of the data within each numerical variable.
# Additionally, the scatterplots where colored via a categroical variable in order to better understand the composition of the data between two numerical variables.
#

#%% [markdown]
# # Scatterplot: Income vs. Education by Age
#
# The Income vs. Education by Age scatterplot for World 1 and World 2 look very similar
# Both worlds appear to a have a varied composition of years of education and annual incomes among ages. 
# Interestingly, there does not appear to be any strong patterns or trends in the scatterplot that would clearly indicate that years of education is correlated with annual income.
#
# Overall, both worlds have similar scatterplots of income and education by age.
# Neither world appears to be more "utopian" than the other given these scatterplots.

#%%
# Scatterplot: Income v. Education by Age
# World 1
chart = sns.scatterplot(data=world1, x='education', y='income00', hue='age00')
chart.legend(title='Age', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Education by Age')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

# World 2
chart = sns.scatterplot(data=world2, x='education', y='income00', hue='age00')
chart.legend(title='Age', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Education Length by Age')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

#%% [markdown]
# # Scatterplot: Income vs. Industry by Ethnicity
#
# The Income vs. Industry by Ethnicity scatterplot for World 1 and World 2 look somewhat similar.
# Both worlds appear to a have a varied composition of industry type and annual incomes among ethnicity. 
# However, this scatterplot does display a similar pattern to the Income vs. Industry boxplot above that displays on upward trend between annual income and industry type.
# The finance industry earns the highest annual income, whereas the leisure/hospitality industry earns the lowest annual income. 
#
# Overall, both worlds have similar scatterplots of income and industry by ethnicity.
# Neither world appears to be more "utopian" than the other given these scatterplots.
#%%
# Scatterplot: Income v. Industry by Ethnic
# World1
chart = sns.scatterplot(data=world1, x='industry', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Industry by Ethnicity')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

# World2
chart = sns.scatterplot(data=world2, x='industry', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Ethnicity')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

#%% [markdown]
# # Scatterplot: Income vs. Industry by Ethnicity
#
# The Income vs. Industry by Ethnicity scatterplot for World 1 and World 2 look somewhat similar.
# Both worlds appear to a have a varied composition of industry type and annual incomes among ethnicity. 
# However, this scatterplot does display a similar pattern to the Income vs. Industry boxplot above that displays on upward trend between annual income and industry type.
# The finance industry earns the highest annual income, whereas the leisure/hospitality industry earns the lowest annual income. 
#
# Overall, both worlds have similar scatterplots of income and industry by gender.
# Neither world appears to be more "utopian" than the other given these scatterplots.

#%%
# Scatterplot: Income v. Industry by Gender
# World1
chart = sns.scatterplot(data=world1, x='industry', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Industry by Gender')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

# World2
chart = sns.scatterplot(data=world2, x='industry', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Gender')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()
#%% [markdown]
# # Section 5: Barplots
#
# The following section below provides barplots for relevant the numeric variables in World 1 and World 2. 
# These barplots were plotted in order to gain a better understanding of two variables with the inclusion of a categorical variable.
#
#%% [markdown]
# # Barplot: Income vs. Industry by Gender
#
# The Income vs. Industry by Gender barplot for World 1 and World 2 look similar. 
# Both worlds indicate the males and females that work within each industry recieve relatively equal annual income per industry type.
# In other words, there does not appear to be a drastic annual income gender gap within any indisutry in either World 1 or World 2
#
# Overall, both worlds have similar barplots of income and industry by gender.
# Neither world appears to be more "utopian" than the other given these barplots.

#%%
# Barplot: Income v. Industry by Gender
# World 1
chart = sns.barplot(data=world1, x='industry', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Gender')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

#World 2
chart = sns.barplot(data=world2, x='industry', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Gender')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

#%% [markdown]
# # Barplot: Income vs. Industry by Ethnicity
#
# The Income vs. Industry by Ethnicity barplot for World 1 and World 2 look somewhat similar.
# The finance industry earns the highest annual income, whereas the leisure/hospitality industry earns the lowest annual income. 
# However, there does not appear to be a drastic annual income ethnicity gap within any industry.
# All enthicities recieve a relatively equal annual income within their respected industries.
#
# Overall, both worlds have similar barplots of income and industry by ethnicity.
# Neither world appears to be more "utopian" than the other given these barplots.
#%%
# Barplot: Income v. Industry by Ethnic
# World 1
chart = sns.barplot(data=world1, x='industry', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Industry by Ethnicity')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

# World 2
chart = sns.barplot(data=world2, x='industry', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Ethnicity')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

#%% [markdown]
# # Barplot: Income vs. Marital Status by Gender
#
# The Income vs. Martal Status by Gender barplot for World 1 displays a distinct annual income gender gap within each marital status. 
# This indicates that females recevied less annual income than males in every type of marital status. 
# In World 1, females recieve between $50,000 and $60,000 in annual income, whereas males recieve $60,000 and $70,000 in annual income.
#
# In World 2, females and males recieve relatively equal amounts of annual income within each marital status type.
# Interestingly in World 2, widowed females have a higher annual income than widowed males. 
# 
# Overall the World 1 and World 2 barplots are very different.
# World 1 displays a clear gender gap in annual income whereas World 2 does not.
# Given this barplot, World 2 is more "utopian" than World 1.
#%%
# Barplot: Income v. Marital by Gender
# World 1
chart = sns.barplot(data=world1, x='marital', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Marital Status by Gender')
plt.xlabel('Marital Status')
plt.ylabel('Annual Income ($)')
plt.show()

# World 2
chart = sns.barplot(data=world2, x='marital', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Marital Status by Gender')
plt.xlabel('Marital Status')
plt.ylabel('Annual Income ($)')
plt.show()

#%% [markdown]
# # Barplot: Income vs. Education by Ethnicity
#
# The Income vs. Education by Ethnicity barplot for World 1 displays a clear annual income ethnicity gap within various years of education.
# Ethnicty type 2 consistently recieved a higher annual income of approximately $70,000+ relative to the other ethnicity types.
#
# The World 2 barplot displays a much more equal relationship between annual income, years of education, and ethnicity.
# There does not appear to be a distinct and consistent annual income gap for any ethnicity relative to years of education.
# There is some unequal notable annual income gaps when education equals 8, 9, 10, 11, 19, 21 years, but it is inconsistent.
# 
# Overall, the barplots for World 1 and World 2 are very different.
# World 1 displays a clear annual income ethnicity gap, whereas World 2 does not.
# Given these barplots World 2 is more "utopian" than World 1. 
#%%
# Barplot: Income v. Education by Ethnic
# World 1
chart = sns.barplot(data=world1, x='education', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Education by Ethnicity')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

# World 2
chart = sns.barplot(data=world2, x='education', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Education by Ethnicity')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()


#%% [markdown]
# # Barplot: Income vs. Education by Gender
#
# The Income vs. Education by Gender barplot for World 1 displays a clear annual income gender gap within various years of education.
# Males consistently recieved a higher annual income of approximately between $60,000 and $70,000 relative to females.
#
# The World 2 barplot displays a much more equal relationship between annual income, years of education, and gender.
# There does not appear to be a distinct and consistent annual income gap for any gender relative to years of education.
# There is some notable unequal annual income gaps when education equals 9 and 22 years, but it is inconsistent.
# 
# Overall, the barplots for World 1 and World 2 are very different.
# World 1 displays a clear annual income gender gap, whereas World 2 does not.
# Given these barplots World 2 is more "utopian" than World 1. 
#%%
# Barplot: Income v. Education by Gender
# World1
chart = sns.barplot(data=world1, x='education', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Education by Gender')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

# World2
chart = sns.barplot(data=world2, x='education', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Education by Gender')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

#%% [markdown]
# # Section 6: Conclusion

# In conclusion World 2 is more "utopian" than World 1 because it exhibits more equality than World 1. 
# This is clearly displayed in the last two barplots where there was a clear ethnicity and gender gap related to annual income and years of educations in World 1.
# These barplots are further validated by the initial World 1 boxplots that compared annual income and gender and annual income and ethnicity. 
# The World 1 annual income vs. gender boxplot demonstrated that males have a larger and higher annual income distribution.
# The World 2 annual income vs. ethnicity boxplot demonstrated that ethnicity type 2 and had a larger and higher annual income distribution.
# Overall, it appears that these disparities in World 1 produce an annual income gap among different genders and ethnicities as it relates to years of education.

# %%
