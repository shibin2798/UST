#!/usr/bin/env python
# coding: utf-8

# In[80]:


import numpy as np
import pandas as pd


# #### a. Read data from csv file fire department of New York City (FDNY)

# In[81]:


data=pd.read_csv("FDNY.csv")


# #### b. View content of the data

# In[82]:


display(data)


# #### c. View fist five records

# In[83]:


data.head()


# #### d. Skip the first row from dataset

# In[87]:


data=pd.read_csv("FDNY.csv", skiprows=1)
data


# #### e. View first five records from fixed dataset

# In[85]:


data.head(5)


# #### f. Show statistics of the dataset

# In[88]:


data.describe()


# #### g. Display columns of the dataset

# In[53]:


data.columns


# #### h. Show datatypes of each columns

# In[54]:


data.dtypes


# #### i. View index of dataset
# 

# In[66]:


data.index


# #### j. Find the total number of fire department facilities in New York city
# 

# In[76]:


data['FacilityName'].unique().size


# #### k. View FDNY information for each borough.
# 

# In[63]:


data.groupby(['Borough']).describe()


# #### l. Find the total number of fire department facilities in each borough. (use groupby)

# In[67]:


data.groupby(['Borough']).size()


# #### m. Find the total number of fire department facilities in Manhattan (use groupby)

# In[91]:


data_manhattan=data.groupby('Borough').get_group('Manhattan')
data_manhattan

#OR

data[data['Borough'] == 'Manhattan']


# #### n. Clean the dataset and drop null/nan value.
# 

# In[79]:


data.dropna(inplace = True)
data

