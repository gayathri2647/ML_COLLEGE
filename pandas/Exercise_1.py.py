#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Importing pandas library
import pandas as pd
import numpy as np


# In[10]:


df=pd.DataFrame(np.arange(0,20).reshape(5,4),['Row1','Row2','Row3','Row4','Row5'],["Column1","Column2","Column3","Column4"])


# In[11]:


df.head()    #  To display the data frame


# In[50]:


df  #  To display the data frame


# In[ ]:


# There are 2 methods available to fetch the values in a data frame.  1) loc   2)  iloc
#  loc   -   will return the data series
#  iloc  -   will return the data frame


# In[ ]:


# Code to display the values in rows using loc


# In[12]:


df.loc['Row1']


# In[39]:


type(df.loc['Row1'])


# In[41]:


df['Column1']


# In[42]:


type(df['Column1'])


# In[ ]:


df['Row1']     # Find out the answer


# In[ ]:


df.loc['Column1']   #  Find out the answer


# In[44]:


df.isnull()   #  To check the is there any null values


# In[45]:


df.isnull().sum()    # To find the count of null values in each column


# In[46]:


df['Column1'].unique()    # To display the unique values in column1


# In[48]:


df['Column1'].value_counts()   # To display the count of unique values in column1


# In[ ]:


df['Column2','Column3']    # Find out the answer


# In[49]:


df[['Column2','Column3']]    #  To display more than one column


# In[19]:


df.iloc[:,:]


# In[20]:


df.iloc[0:2,0:2]


# In[21]:


type(df.iloc[0:2,0:2])


# In[29]:


df.iloc[2:4,1:4]


# In[30]:


df.iloc[0:2,0:2]


# In[31]:


type(df.iloc[0:2,0:2])


# In[32]:


type(df.iloc[0:2,0])


# In[17]:


df


# In[18]:


df.to_csv("Test1.csv")    # Convert the data frame into csv file


# In[34]:


df.iloc[:,:].values  # Convert the data frame into an array


# In[35]:


type(df.iloc[:,:].values)  


# In[36]:


df.iloc[:,:].values.shape


# In[37]:


df['Column1']


# In[ ]:




