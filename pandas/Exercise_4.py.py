#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Reading from different data sources using pandas
### Exploring different parameters in read_csv method


# In[6]:


from io import StringIO,BytesIO


# In[10]:


data = ('col1,col2,col3\n''x,y,1\n''a,b,2\n''c,d,3')    # Assigning string


# In[11]:


data


# In[7]:


type(data)


# In[8]:


import pandas as pd


# In[12]:


pd.read_csv(StringIO(data))


# In[20]:


df = pd.read_csv(StringIO(data),usecols = ['col1','col3'])


# In[21]:


df


# In[13]:


df = pd.read_csv(StringIO(data),usecols = lambda x: x.upper() in ['COL1','COL3'])


# In[14]:


df


# In[15]:


df.to_csv('Test2.csv')


# In[17]:


data1 = ('a,b,c,d\n''1,2,3,4\n''5,6,7,8\n''9,10,11')  
# Oserve there is only 3 values in last row. The last value will be filled as NaN, by default
data1


# In[18]:


print(data1)


# In[27]:


df = pd.read_csv(StringIO(data1))
df


# In[28]:


df.info()   #  Why the datatype is float64?


# In[29]:


df = pd.read_csv(StringIO(data1),dtype=object)   #  To change the datatype of all columns. 
# Object type represents the string
df


# In[30]:


df.info()


# In[24]:


df['a']    #  To fetch the column


# In[25]:


df['a'][1]


# In[26]:


df.loc[1]  #  To fetch the row


# In[31]:


df = pd.read_csv(StringIO(data1),dtype=int)   #  To change the datatype of all columns into int. 
df   # Why the output is an error?


# In[32]:


# To rectify the above error.

data1 = ('a,b,c,d\n''1,2,3,4\n''5,6,7,8\n''9,10,11,12')  
# the value 12 is added in the last row
data1


# In[34]:


df = pd.read_csv(StringIO(data1))
df


# In[35]:


df.info() # Observe the datatype of all columns


# In[36]:


df = pd.read_csv(StringIO(data1),dtype=int)   #  To change the datatype of all columns into int. 
df 

### Observe the difference between int / int32 / int64. Write the difference in notebook


# In[37]:


df.info()


# In[38]:


df = pd.read_csv(StringIO(data1),dtype=float)   #  To change the datatype of all columns into float. 
df


# In[39]:


df.info()


# In[46]:


import numpy as np
df = pd.read_csv(StringIO(data1),dtype = {'b':int,'c':np.float64,'d':np.int64})
# Converting the data types of 3 columns with different data type.
df


# In[47]:


df.info()


# In[48]:


df.dtypes # To display the data type of all columns


# In[50]:


type(df['a'])


# In[57]:


type(df['a'][0])


# In[59]:


data = ('index,a,b,c\n''4,apple,bat,5.7\n''8,orange,cow,10')
data


# In[60]:


print(data)


# In[62]:


pd.read_csv(StringIO(data))


# In[61]:


pd.read_csv(StringIO(data),index_col=0) # Making the 0th column as index
# index_col is to allow you to set which columns to be used as the index of the dataframe


# In[63]:


pd.read_csv(StringIO(data),index_col=1)  # Making the 1st column as index


# In[ ]:


# Change the index_col = 0 / 1 / 2 / 3 and observe the ouput


# In[3]:


import pandas as pd
data = ('a,b,c\n''4,apple,bat,\n''8,orange,cow,')
print(data)


# In[4]:


# Find out the answer for the below.
pd.read_csv(data)  #  Why does it display error?


# In[7]:


pd.read_csv(StringIO(data))   #  4 , 8 are considered as indices and for C, NaN will be taken


# In[71]:


pd.read_csv(StringIO(data),index_col=False) 
# index_col=False can be used to force pandas to not use the first column as the index
# Observe the difference between this code and previous code.


# In[8]:


### Combining usecols and index_col
data = ('a,b,c\n''4,apple,bat,\n''8,orange,cow,')


# In[10]:


pd.read_csv(StringIO(data),usecols=['b','c'],index_col=False)


# In[11]:


### Quoting and escape characters
data = 'a,b\n"hello, \\"Bob\\",nice to see you",5'


# In[12]:


data


# In[13]:


pd.read_csv(StringIO(data),escapechar='\\')


# In[ ]:




