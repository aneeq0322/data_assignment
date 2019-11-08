#!/usr/bin/env python
# coding: utf-8

# 
# 
# ### Step 1. Import the necessary libraries

# In[62]:


import pandas as pd


# ### Step 2. Import the dataset Euro_2012_stats_TEAM

# ### Step 3. Assign it to a variable called euro12.

# In[213]:


euro=pd.read_csv('Euro_2012_stats_TEAM.csv')
euro12=pd.DataFrame(euro)
euro12


# ### Step 4. Select only the Goal column.

# In[281]:


euro_goals=euro12[['Team','Goals']]
euro_goals


# ### Step 5. How many team participated in the Euro2012?

# In[91]:


euro_goals=euro_goals.dropna()            #dropna() is use to ignore nal values from given data 
len(euro_goals)


# ### Step 6. What is the number of columns in the dataset?

# In[10]:


len(euro12.columns)


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[12]:


euro_team=euro12[['Team','Yellow Cards','Red Cards']]
disciplane=euro_team.dropna()
disciplane


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[97]:


#sort values as ascending
print(disciplane.sort_values('Red Cards'),"\n")       #name.sort_values("Team", inplace = True) 
#sort values as decending
print(disciplane.sort_values('Yellow Cards',ascending=False))


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[48]:


mean_of_yellowcards=disciplane_yellowcards.mean()
print("mean of yellow cards=",+mean_of_yellowcards)


# ### Step 10. Filter teams that scored more than 6 goals

# In[103]:


filter_team=euro_goals.where(euro['Goals']>6)  #DataFrame.where(cond, other=nan, inplace=False, axis=None, 
                                                #level=None, errors=’raise’, try_cast=False, raise_on_error=None)
                                               
print(filter_team)                             
x=filter_team.dropna()
print('\n',x)                                                #Parameters:
                                                #cond: One or more condition to check data frame for.
                                                #other: Replace rows which don’t satisfy the condition with user defined object,
                                                #Default is NaN
                                                #inplace: Boolean value, Makes changes in data frame itself if True
                                                #axis: axis to check( row or columns)


# ### Step 11. Select the teams that start with G

# In[137]:


teams=list(euro_goals['Team'])
for a in teams:
    if a[0]=='G' or a[0]=='g':
        print("name of team which start from 'G' in euro12 is",a)
    
    


# ### Step 12. Select the first 7 columns

# In[142]:


a=euro12.iloc[:,:7]
print(a)


# ### Step 13. Select all columns except the last 3.

# In[148]:


b=len(euro.columns)-3
c=euro12.iloc[:,:b]
print(c)


# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[208]:


teams=euro12[['Team','Shooting Accuracy']]

a=teams.loc[(teams.Team=='England') | (teams.Team=='Italy') | (teams.Team=='Russia')]  # use in loc '|' instead of 'or','&'
                                                                                         #instead of 'and'
print(a) 


# ### Step 15. Use apply method on Goal Column to make a new column called Performance, using following conditions
# 
# 1. If Goals are less than or equal to 2, peformance is **Below Avg**
# 2. If Goals are more than 2 and less than or equal to 5, peformance is **Average**
# 3. If Goals are more than 5 and less than or equal to 10, peformance is **Above Average**
# 4. If Goals are more than 10 then peformance is **Excellent**

# In[287]:


#print(euro_goals)
euro_goals.loc[euro_goals.Goals <=2,'Performance']='Below Avg'
euro_goals.loc[(euro_goals.Goals >2) & (euro_goals.Goals<=5),'Performance']='Average'
euro_goals.loc[(euro_goals.Goals >5) & (euro_goals.Goals<=10),'Performance']='Above Average'
euro_goals.loc[(euro_goals.Goals >10),'Performance']='Excellent'
print(euro_goals)
euro_goals.to_csv("performanceblock.csv")
    


# In[ ]:




