#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dm6103 as dm

# Part I
titanic = dm.api_dsLand('Titanic', 'id')

# Part II
nfl = dm.api_dsLand('nfl2008_fga')
nfl.dropna(inplace=True)

#%% [markdown]

# # Part I  
# Titanic dataset - statsmodels
# 
# | Variable | Definition | Key/Notes  |  
# | ---- | ---- | ---- |   
# | survival | Survived or not | 0 = No, 1 = Yes |  
# | pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd |  
# | sex | Gender / Sex |  |  
# | age | Age in years |  |  
# | sibsp | # of siblings / spouses on the Titanic |  |  
# | parch | # of parents / children on the Titanic |  |  
# | ticket | Ticket number (for superstitious ones) |  |  
# | fare | Passenger fare |  |  
# | embarked | Port of Embarkation | C: Cherbourg, Q: Queenstown, S: Southampton  |  
# 
#%%
# ## Question 1  
# With the Titanic dataset, perform some summary visualizations:  
# 
# ### a. Histogram on age. Maybe a stacked histogram on age with male-female as two series if possible
sns.set_palette('Set3')
chart = sns.histplot(data=titanic, x='age', hue='sex', multiple='stack')
chart.legend_.set_title('Gender')
chart.legend_.texts[0].set_text('Male')
chart.legend_.texts[1].set_text('Female')
plt.title('Age on the Titanic by Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# ### b. proportion summary of male-female, survived-dead
sns.set_palette('Set3')
chart = sns.countplot(data=titanic, x='sex', hue='survived')
chart.legend_.set_title('Survival')
chart.legend_.texts[0].set_text('Died')
chart.legend_.texts[1].set_text('Survived')
plt.title('Gender on the Titanic by Survival')
plt.xlabel('Gender')
plt.xticks([0, 1], ['Male', 'Female'])
plt.ylabel('Count')
plt.show()

# ### c. pie chart for “Ticketclass”
pclass_counts = titanic.pclass.value_counts()
pclass_data = [pclass_counts[1], pclass_counts[2], pclass_counts[3]]
sns.set_palette('Set3')
plt.pie(pclass_data, labels=['1st Class', '2nd Class', '3rd Class'], autopct='%0.0f%%')
plt.title('Ticket Class on the Titanic')
plt.show()

# ### d. A single visualization chart that shows info of survival, age, pclass, and sex.
chart = sns.catplot(data=titanic, y='age', x='pclass', hue='sex', col='survived', kind='violin', split=True, cut=0)
chart._legend.set_title('Gender')
chart._legend.texts[0].set_text('Male')
chart._legend.texts[1].set_text('Female')
chart.set_titles()
col_titles = chart.axes.flatten()
col_titles[0].set_title('Titanic Passengers who Died')
col_titles[1].set_title('Titanic Passengers who Survived')
plt.subplots_adjust(top=0.88)
plt.suptitle('Age vs. Ticket Class by Gender and Survival', fontweight='bold')
chart.set_xlabels('Ticket Class')
plt.xticks([0, 1, 2], ['1st Class', '2nd Class', '3rd Class'])
chart.set_ylabels('Age')
plt.show()
#%%
# ## Question 2  
# Build a logistic regression model for survival using the statsmodels library. As we did before, include the features that you find plausible. Make sure categorical variables are use properly. If the coefficient(s) turns out insignificant, drop it and re-build.  
import statsmodels.api as sm
from statsmodels.formula.api import glm

#surviv_model1 = glm(formula='survived ~ C(pclass)+sex+age+C(sibsp)+C(parch)+ticket+fare+C(embarked)', data=titanic, family=sm.families.Binomial())
surviv_model1 = glm(formula='survived ~ pclass+sex+age+sibsp+parch+ticket+fare+embarked', data=titanic, family=sm.families.Binomial())
surviv_model1_Fit = surviv_model1.fit()
print( surviv_model1_Fit.summary() )

# ## Question 3  
# Interpret your result. What are the factors and how do they affect the chance of survival (or the survival odds ratio)? What is the predicted probability of survival for a 30-year-old female with a second class ticket, no siblings, 3 parents/children on the trip? Use whatever variables that are relevant in your model.  

# The following results indicate that passengers that were young, women, had a higher ticket class, had a lower number of siblings, had a lower number of parents, and had a higher passenger fare, had a higher chance of survival.



# ## Question 4  
# Try three different cut-off values at 0.3, 0.5, and 0.7. What are the a) Total accuracy of the model b) The precision of the model (average for 0 and 1), and c) the recall rate of the model (average for 0 and 1)




#%%[markdown]
# # Part II  
# NFL field goal dataset - SciKitLearn
# 
# | Variable | Definition | Key/Notes  |  
# | ---- | ---- | ---- |   
# | AwayTeam | Name of visiting team | |  
# | HomeTeam | Name of home team | |  
# | qtr | quarter | 1, 2, 3, 4 |  
# | min | Time: minutes in the game |  |  
# | sec | Time: seconds in the game |  |  
# | kickteam | Name of kicking team |  |  
# | distance | Distance of the kick, from goal post (yards) |  |  
# | timerem | Time remaining in game (seconds) |  |  
# | GOOD | Whether the kick is good or no good | If not GOOD: |  
# | Missed | If the kick misses the mark | either Missed |  
# | Blocked | If the kick is blocked by the defense | or blocked |  
# 
#%% 
# ## Question 5  
# With the nfl dataset, perform some summary visualizations.
# name vs total min played
# create total_min column
nfl['total_min'] = nfl['min'] + (nfl['sec'] / 60)
nfl.head()

players = nfl.groupby('name').agg(['sum']).reset_index()
players.plot(x='name', y='total_min', kind='bar', legend=False, width=1, edgecolor='white', figsize=(12, 8))
plt.title('Total Minutes Played per Player')
plt.xlabel('Name')
plt.ylabel('Minutes')
plt.subplots_adjust(bottom=.3)
plt.show()

#%%
# ## Question 6  
# Using the SciKitLearn library, build a logistic regression model overall (not individual team or kicker) to predict the chances of a successful field goal. What variables do you have in your model? 
# 
# ## Question 7  
# Someone has a feeling that home teams are more relaxed and have a friendly crowd, they should kick better field goals. Can you build two different models, one for all home teams, and one for road teams, of their chances of making a successful field goal?
# 
# ## Question 8    
# From what you found, do home teams and road teams have different chances of making a successful field goal? If one does, is that true for all distances, or only with a certain range?
# 


# %%
# titanic.dropna()


# %%
