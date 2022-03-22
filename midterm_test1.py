# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

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

#%%
"""
1. Summary statistics of all the variables (mean, mode, median, #observations, max/min, std. dev, variance)
2. Histograms of each variable per world
    - overlay kernel density plot
3. For related variables, ethnic X income boxplot  vs. ethnic X education vs. gender X income
4. education X income
    - Scatter plots with linear regression/best fit line
    
** If they are not equal, then it is not a utopia
"""
#%%
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
#%%
#Histograms of each variable per world
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
# # Boxplots: Income vs. Gender
#
# The Income vs. Gender boxplot for World 1 shows that men have a higher medain annual income, a larger interquatile range for annual income, and a higher maximum value for annual income relative to women.
# This indicates that men in World 1 within the annual income distribution of data make more money than women. Additionlly, the female boxplot plot in World 1 has a large number of large outliers above the maximum value, indicating that the higher salary range approximately above $120,000 is uncommon in the distrubution of annual income among females.
# 
#
#%%
# Boxplots per world

# Boxplots Income vs. Gender
# World 1
sns.boxplot(x='gender', y='income00', data=world1, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World 1: Income vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# World2
sns.boxplot(x='gender', y='income00', data=world2, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World 2: Income vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# Boxplot: Income vs. Ethnicity
# World1
sns.boxplot(x='ethnic', y='income00', data=world1, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World1: Income vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# World2
sns.boxplot(x='ethnic', y='income00', data=world2, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World2: Income vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# Boxplot: Income vs. Marital
# World1
sns.boxplot(x='marital', y='income00', data=world1, palette=['#F7E654', '#F0AB00', '#5482AB', '#00B0CA'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1, 2, 3], ['Never-Married', 'Married', 'Divorced', 'Widowed'])
plt.title("World1: Income vs. Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# World2
sns.boxplot(x='marital', y='income00', data=world2, palette=['#F7E654', '#F0AB00', '#5482AB', '#00B0CA'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1, 2, 3], ['Never-Married', 'Married', 'Divorced', 'Widowed'])
plt.title("World2: Income vs. Marital Status")
plt.xlabel("Marital Status")
plt.ylabel("Annual Income ($)")
plt.subplots_adjust(left=0.15)
plt.show()

# Boxplot: Education vs. Gender
# World1
sns.boxplot(x='gender', y='education', data=world1, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World1: Education vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()

# World2
sns.boxplot(x='gender', y='education', data=world2, palette=['#F7E654', '#F0AB00'], medianprops=dict(color='#00685B'))
plt.xticks([0, 1], ['Female', 'Male'])
plt.title("World2: Education vs. Gender")
plt.xlabel("Gender")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()


# Boxplot: education v. Ethnicity
# World1
sns.boxplot(x='ethnic', y='education', data=world1, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World1: Education vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()

# World2
sns.boxplot(x='ethnic', y='education', data=world2, palette=['#F7E654', '#F0AB00', '#5482AB'], medianprops=dict(color='#00685B'))
plt.title("World2: Education vs. Ethnicity")
plt.xlabel("Ethnicity")
plt.ylabel("Education (years)")
plt.subplots_adjust(left=0.15)
plt.show()
#%%
# The following are scatterplots and barplots

# Scatterplot: Income v. Education by Age
# World1
chart = sns.scatterplot(data=world1, x='education', y='income00', hue='age00')
chart.legend(title='Age', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Education by Age')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

# World2
chart = sns.scatterplot(data=world2, x='education', y='income00', hue='age00')
chart.legend(title='Age', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Education Length by Age')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

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

# Barplot: Income v. Industry by Gender
# World1
chart = sns.barplot(data=world1, x='industry', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Gender')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

#World2
chart = sns.barplot(data=world2, x='industry', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Gender')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

# Barplot: Income v. Industry by Ethnic
# World1
chart = sns.barplot(data=world1, x='industry', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Industry by Ethnicity')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

# World2
chart = sns.barplot(data=world2, x='industry', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Industry by Ethnicity')
plt.xlabel('Industry')
plt.ylabel('Annual Income ($)')
plt.show()

# Barplot: Income v. Marital by Gender
# World1
chart = sns.barplot(data=world1, x='marital', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Marital Status by Gender')
plt.xlabel('Marital Status')
plt.ylabel('Annual Income ($)')
plt.show()

# World2
chart = sns.barplot(data=world2, x='marital', y='income00', hue='gender')
chart.legend(title='Gender', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Marital Status by Gender')
plt.xlabel('Marital Status')
plt.ylabel('Annual Income ($)')
plt.show()

# Barplot: Income v. Education by Ethnic
# World1
chart = sns.barplot(data=world1, x='education', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 1: Income vs. Education by Ethnicity')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

# World2
chart = sns.barplot(data=world2, x='education', y='income00', hue='ethnic')
chart.legend(title='Ethnicity', loc='upper left', bbox_to_anchor=(1.05, 1.0))
plt.title('World 2: Income vs. Education by Ethnicity')
plt.xlabel('Education (years)')
plt.ylabel('Annual Income ($)')
plt.show()

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
#%%
