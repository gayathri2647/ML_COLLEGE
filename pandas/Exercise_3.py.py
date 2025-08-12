#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


df = pd.read_csv("D:\Anuradha\mercedesbenz.csv")


# In[6]:


df    # To display the data available in dataframe


# In[7]:


df.head()    # To display the top 5 rows in a csv file


# In[8]:


df.info()    # To print information about the DataFrame


# In[9]:


df.describe()    # To display the description of the data in the DataFrame

"""
If the DataFrame contains numerical data, the description contains these information for each column:

count - The number of not-empty values.
mean - The average (mean) value.
std - The standard deviation.
min - the minimum value.
25% - The 25% percentile*.
50% - The 50% percentile*.
75% - The 75% percentile*.
max - the maximum value.
"""


# In[10]:


import numpy as np


# In[11]:


df1 = np.arange(20).reshape(5,4)


# In[12]:


df1


# In[14]:


df1 = pd.DataFrame(df1)
df1


# In[15]:


df1 = pd.DataFrame(np.arange(20).reshape(5,4),["Row1","Row2","Row3","Row4","Row5"],["Column1","Column2","Column3","Column4"])
df1


# In[5]:


import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.arange(20).reshape(5,4),index = ["Row1","Row2","Row3","Row4","Row5"],columns = ["Column1","Column2","Column3","Column4"])
# Mentioning the parameter name such as index and columns.
df1


# In[17]:


df1.info()


# In[18]:


df1.describe()


# In[19]:


df1.to_csv("Test1.csv")     #  To write a pandas DataFrame to a CSV file
df1


# In[21]:


df2 = pd.read_csv("Test1.csv")
df2


# In[22]:


df2.info()


# In[23]:


df2.describe()


# In[25]:


df2["Column1"].unique()   #  To find the unique elements of an array and returns these unique elements as a sorted array.


# In[26]:


df2["Column1"].value_counts()  # Return a Series containing counts of unique values


# In[29]:


# Open the Test1.csv file. Convert all ',' separators as ';'

df2 = pd.read_csv("Test1.csv",sep=';')   #  if the csv file contains ; as separator, mention the sep parameter
df2


# In[30]:


df1


# In[31]:


df


# In[32]:


df['X0'].value_counts()


# In[33]:


df['y']


# In[34]:


df['y']<100


# In[35]:


df[df['y']<100]    # Observe the difference between this one and previous one


# In[36]:


df.corr()   #  To find the pairwise correlation of all columns. Any NaN values are automatically excluded.  


# In[3]:


#  To illustrate Not-a-number values
import numpy as np
data = [[1,2,3],[4,5,np.nan],[6,7,np.nan],[np.nan,np.nan,np.nan]]
data


# In[5]:


import pandas as pd
df3 = pd.DataFrame(data)  # Converting a matrix into data frame
df3


# In[41]:


df3


# In[6]:


df3.dropna(axis=0)   # Row 1,2,3 are having NaN. So it will return row 1 only. 
# axis = 0 represents row (x axis)


# In[7]:


df3.dropna(axis=1)   # All columns are having NaN. So it will return row heading only. 
# axis = 1 represents column (y axis)


# In[43]:


df3


# In[44]:


df3.dropna()   # All NaN values will be dropped


# In[45]:


df3


# In[46]:


df3.dropna(axis=1)  # All columns are having NaN. So it will return row heading only. axis = 1 represents column (y axis)


# In[22]:


df3


# In[ ]:


# isna() and notna() methods in pandas. Observe the function prototype of both methods


# In[20]:


pd.isna(df3)  #  It is a boolean function that looks for the missing values 
# and returns TRUE where it detects a missing value.


# In[21]:


pd.isna(df3[2])


# In[24]:


df3[2].notna()   #  The notna () function returns TRUE, if the data is free from missing values 
# else it returns FALSE (if NA/NaN values are encountered).


# In[26]:


# The fillna () method replaces the NULL values with a specified value.
df3.fillna('Missing')


# In[27]:


df3


# In[ ]:


#  Observe the difference between dropna() and fillna() methods


# In[9]:


df4 = pd.DataFrame(np.random.randn(5,4)) 
df4
# randn() is used to create an array of specified shape and fills it with random values 
# as per standard normal distribution.
# Execute the code again and again . Observe the random values generated


# In[49]:


df4 = pd.DataFrame(np.random.randn(5,3))
df4


# In[11]:


print(np.random.randn(5))


# In[10]:


df4 = pd.DataFrame(np.random.randn(5))
df4


# In[54]:


df4 = pd.DataFrame(np.random.randn(5,3),['a','c','e','f','h'],["One","Two","Three"])
df4


# In[55]:


# reindex() Example
# Pandas dataframe.reindex() function conform DataFrame to new index with optional filling logic, 
# placing NA/NaN in locations having no value in the previous index.

# Example 1 for reindex()
df5 = df4.reindex(['a','b','c','d','e','f','g','h'])
df5


# In[12]:


# Converting dictionary into data frame
df = pd.DataFrame({"A":[1, 5, 3, 4, 2],
                   "B":[3, 2, 4, 3, 4],
                   "C":[2, 2, 7, 3, 4],
                   "D":[4, 3, 6, 12, 7]},
                   index =["first", "second", "third", "fourth", "fifth"])
  
# Print the dataframe
df


# In[13]:


# Example 2 for reindex()
# reindexing with new index values
df.reindex(["first", "dues", "trois", "fourth", "fifth"])  
# Here new indices 'dues', 'trios' will be created with NaN values


# In[14]:


# Example 3 for reindex()
# Filling the missing values by 100
df.reindex(["first", "dues", "trois", "fourth", "fifth"], fill_value = 100)


# In[18]:


# Example 3 for reindex()
# Using reindex() function to reindex the column axis
# Creating the dataframe from dictionary
df1 = pd.DataFrame({"A":[1, 5, 3, 4, 2],
                    "B":[3, 2, 4, 3, 4],
                    "C":[2, 2, 7, 3, 4],
                    "D":[4, 3, 6, 12, 7]})
df1


# In[17]:


# reindexing the column axis with
# old and new index values
df.reindex(columns =["A", "B", "D", "E"])


# In[19]:


# Filling the new index with some values
# reindex the columns
# fill the missing values by 25
df.reindex(columns =["A", "B", "D", "E"], fill_value = 25)

