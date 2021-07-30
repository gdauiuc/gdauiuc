#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 - Data Preparation Basics
# ## Segment 1 - Filtering and selecting data

# In[1]:


import numpy as np
import pandas as pd

from pandas import Series, DataFrame
#use shift + return to retrieve data


# ### Selecting and retrieving data
# You can write an index value in two forms.
# - Label index or 
# - Integer index

# In[2]:


series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6','row 7', 'row 8'])
series_obj


# In[3]:


series_obj['row 7']


# In[4]:


series_obj[[0, 7]]


# In[5]:


np.random.seed(25) #create data frame object
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row 1', 'row 2', 'row 3', 'row 4','row 5','row 6'],
                   columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
DF_obj


# In[6]:


DF_obj.loc[['row 2', 'row 5'], ['column 5', 'column 2']]


# ### Data slicing
# You can use slicing to select and return a slice of several values from a data set. Slicing uses index values so you can use the same square brackets when doing data slicing.
# 
# How slicing differs, however, is that with slicing you pass in two index values that are separated by a colon. The index value on the left side of the colon should be the first value you want to select. On the right side of the colon, you write the index value for the last value you want to retrieve. When you execute the code, the indexer then simply finds the first record and the last record and returns every record in between them. 

# In[7]:


series_obj['row 3': 'row 7']


# ### Comparing with scalars
# Now we're going to talk about comparison operators and scalar values. Just in case you don't know that a scalar value is, it's basically just a single numerical value. You can use comparison operators like greater than or less than to return true/false values for all records to indicate how each element compares to a scalar value.

# In[8]:


DF_obj < .2


# ### Filtering with scalars

# In[9]:


series_obj[series_obj > 6]


# ### Setting values with scalars

# In[10]:


series_obj['row 1', 'row 5', 'row 8'] = 8
series_obj


# Filtering and selecting using Pandas is one of the most fundamental things you'll do in data analysis. Make sure you know how to use indexing to select and retrieve records.

# ## Segment 2 - Treating missing values

# ### Figuring out what data is missing

# In[11]:


missing = np.nan

series_obj = Series(['row 1', 'row 2', missing, 'row 4', 'row 5', 'row 6', missing, 'row 8'])
series_obj


# In[12]:


series_obj.isnull()


# ### Filling in for missing values

# In[13]:


np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6))
DF_obj


# In[14]:


DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing
DF_obj


# In[15]:


filled_DF = DF_obj.fillna(0) #fill the missing values with 0
filled_DF


# In[16]:


filled_DF = DF_obj.fillna({0: 0.1, 5:1.25}) #column 0 filled with 0.1 and column 5 filled with 1.25
filled_DF


# In[17]:


fill_DF = DF_obj.fillna(method='ffill') #filled with last value
fill_DF


# ### Counting missing values

# In[18]:


np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape(6,6))
DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing
DF_obj


# In[19]:


DF_obj.isnull().sum() #count null value in the dataframe


# ### Filtering out missing values

# In[20]:


DF_no_NaN = DF_obj.dropna() #one row with no null value
DF_no_NaN


# In[21]:


DF_no_NaN = DF_obj.dropna(axis=1) #drop the column
DF_no_NaN


# ## Segment 3 - Removing duplicates

# ### Removing duplicates

# In[22]:


DF_obj= DataFrame({'column 1':[1,1,2,2,3,3,3],
                   'column 2':['a', 'a','b', 'b', 'c', 'c', 'c'],
                   'column 3':['A', 'A', 'B', 'B', 'C', 'C', 'C']})
DF_obj


# In[23]:


DF_obj.duplicated() #find if it is duplicated from the previous row


# In[24]:


DF_obj.drop_duplicates()


# In[25]:


DF_obj= DataFrame({'column 1':[1,1,2,2,3,3,3],
                   'column 2':['a', 'a','b', 'b', 'c', 'c', 'c'],
                   'column 3':['A', 'A', 'B', 'B', 'C', 'D', 'C']})
DF_obj


# In[26]:


DF_obj.drop_duplicates(['column 3'])


# ## Segment 4 - Concatenating and transforming data

# In[27]:


DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_obj


# In[28]:


DF_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
DF_obj_2


# ### Concatenating data

# In[29]:


pd.concat([DF_obj, DF_obj_2], axis=1)


# In[30]:


pd.concat([DF_obj, DF_obj_2]) #add it through row


# ### Transforming data
# #### Dropping data

# In[31]:


DF_obj.drop([0, 2]) #drop row


# In[32]:


DF_obj.drop([0, 2], axis=1)


# ### Adding data

# In[33]:


series_obj = Series(np.arange(6))
series_obj.name = "added_variable"
series_obj


# In[34]:


variable_added = DataFrame.join(DF_obj, series_obj)
variable_added


# In[35]:


added_datatable = variable_added.append(variable_added, ignore_index=False)
added_datatable


# In[36]:


added_datatable = variable_added.append(variable_added, ignore_index=True)
added_datatable


# ### Sorting data

# In[37]:


DF_sorted = DF_obj.sort_values(by=(5), ascending=[False])
DF_sorted


# ## Segment 5 - Grouping and data aggregation
# ### Grouping data by column index
