#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


df = pd.read_csv('C:\Anuradha\gapminder-FiveYearData.csv')  #  read_csv file to open the file given


# In[6]:


df    # To display the data in the csv file


# In[7]:


# Display the first 5 rows
df.head()


# In[8]:


# Display the last 5 rows
df.tail()


# In[9]:


# Display the no.of rows & Columns
df.shape


# In[10]

# Display the column names
print(df.columns)


# In[11]:


# Display the datatype of each column
df.dtypes


# In[12]:


# Display more information about data
df.info()


# In[13]:


# To fetch the values in 'country' column only
ctry = df['country']


# In[14]:


# Display the values in 'country' column
ctry


# In[15]:


# Display the top 5 rows in country column
ctry.head()


# In[16]:


# Display the last 5 records in country column
ctry.tail()


# In[17]:


# Display top 10 records in country column
ctry.head(n=10)


# In[18]:


# Display the last 10 records in country column
ctry.tail(n=10)


# In[19]:


# Display the last record in country column
ctry.tail(n=1)


# In[20]:


# Fetching more than one column
subset = df[['country','continent','year']]
subset


# In[21]:


# By using the above 

# Write code to Display top 5 records
# Write code to Display top 20 records
# Write code to Display last 5 records
# Write code to Display last 15 records
# Write code to Display first record
# Write code to Display last record


# In[23]:


# Fetching more than one column
subset = df['country','continent','year']      #  Observe the error. To access more than one column, use [[   ]]
subset


# In[ ]:


#######  use of loc & iloc in pandas    ######


# In[ ]:


#######  use of loc in pandas    ######


# In[29]:


# Display the 1st row
df.loc[0]


# In[27]:


# Display the 100th row
df.loc[99]


# In[28]:


# Display the 1000th row
df.loc[999]


# In[30]:


# Display 1st, 100th and 1000th row
df.loc[[0,99,999]]


# In[32]:


#######  use of iloc (integer location) in pandas    ######


# In[33]:


# Display the second row
df.iloc[1]


# In[34]:


# Display the 100th row
df.iloc[99]


# In[35]:


# Display the last row using -1 as index  .   
df.iloc[-1]


# In[36]:


#  Try to pass -1 in loc and observe the error.   -1 can be passed in iloc only
df.loc[-1]


# In[37]:


# Display 1st, 100th and 1000th row
df.iloc[[0,99,999]]


# In[41]:


###### Using loc & iloc, fetch the specific rows and columns   ########

# Syntax   :   df.loc[row_range,column_range]  .   
# While using loc, the coulmn name should be mentioned 
# whereas in iloc, the index of column name should be mentioned

subset = df.loc[0:99,['country','year']]        
subset


# In[42]:


subset = df.loc[:,['country','year']]     
subset


# In[43]:


# Using loc , write a code to display first 500 rows of country column


# In[45]:


subset = df.iloc[:,[1,3,5]]     #  Observe here the column indices are given in stead of column names
subset


# In[46]:


subset = df.iloc[:,[2,4,-1]]     #  Observe here the index of last column is given as -1
subset


# In[47]:


subset = df.iloc[:,:]     #  Observe the output
subset


# In[48]:


######  Applying the comparison operators and logical operators in loc and iloc    ######


# In[51]:


df.loc[df.lifeExp>=60]


# In[53]:


# df.loc[(df.lifeExp>=60) & (df.country == 'Albania')]  . This statement too will give the output

subset = df.loc[(df.lifeExp>=60) & (df.country == 'Albania')]
subset


# In[54]:


subset.shape


# In[55]:


subset.columns


# In[56]:


subset.dtypes


# In[57]:


subset.head()


# In[58]:


subset.tail()


# In[59]:


subset.info()


# In[10]:


df.loc[(df.lifeExp>=60) , ['country','pop','lifeExp']]


# In[62]:


# update the values
df.loc[(df.country == 'Albania'),['pop']] = 100000


# In[63]:


df


# In[13]:


# Cretae a range of integers from 0 to 4
srange = list(range(5))
srange


# In[14]:


# Subsetting columns by range
subset = df.iloc[:,srange]
subset


# In[15]:


##### Subsetting rows and columns  ####
#  Using loc
df.loc[42,'country']


# In[17]:


##### Subsetting rows and columns  ####
#  Using iloc
df.iloc[42,0]


# In[18]:


##### Subsetting multiple rows and columns  ####
#  Using loc
df.loc[[0,99,999],['country','lifeExp']]


# In[21]:


# Display range of rows using loc
df.loc[10:13,['country','lifeExp']]
###  df.loc[10:13,[0,3,5]]      #  Remove the comment entry & check the answer. 


# In[22]:


##### Subsetting multiple rows and columns  ####
#  Using iloc

df.iloc[[0,99,999],[0,3,5]]


# In[23]:


##### What was the average life expectency , for each yaer in our data?????    #####
df.groupby('year')['lifeExp']


# In[24]:


##### What was the average life expectency , for each yaer in our data?????    #####
df.groupby('year')['lifeExp'].mean()


# In[25]:


#####  Creating a stacked table using groupby command   #####
multi_gp = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
multi_gp


# In[26]:


#####   Flatten he data frame   using reset_index  function

flat = multi_gp.reset_index()
flat


# In[27]:


#####  Grouped frequency counts   #####
# use nunique to get counts of unique values 
df.groupby('continent')['country'].nunique()


# In[ ]:




