#!/usr/bin/env python
# coding: utf-8

# In[2]:


#####        Reading JSON data      ######

### Convert a JSON (Java Script Object Notation) from the string into Panda DataFrame 

### # json is a combination of key - value pairs as below. It is like a dictionary in python


# In[2]:


import pandas as pd


# In[23]:


data = '{"emp_id": {"Sree":"101"}, "email":{"Sree": "sree@gmail.com"}, "position":{"Sree": "Team Lead"}}'
pd.read_json(data)


# In[ ]:


'''
# Orient is one of the parameter used with read_json(). 
# The set of possible values for orient parameter are index, columns, records, split, values. 
# By default, it takes columns value.


'split' : dict like {index -> [index], columns -> [columns], data -> [values]}

'records' : list like [{column -> value}, ... , {column -> value}]

'index' : dict like {index -> {column -> value}}

'columns' : dict like {column -> {index -> value}}

'values' : just the values array
'''


# In[25]:



# Column oriented JSON string into data frame
data = '{"emp_id": {"Sree":"101","Promod":"102"}, "email":{"Sree": "sree@gmail.com","Promod":"Promod@gmail.com"}, "position":{"Sree": "Team Lead","Promod":"Senior Engineer"}}'
pd.read_json(data,orient='columns')


# In[25]:


json_data ='''{ 
   "index":["Employee_1","Employee_2","Employee_3"],
   "columns":["Id","Name","Age","Department"],
   "data":[["101","Sree","32","Development"],
   ["102","Santhosh","45","Testing"],
   ["103","Pramod","56","Talent Acquistion"]]
   }'''
 
df= pd.read_json(json_data,orient='split')
df

# Refer the syntax given above for using split orientation 


# In[21]:


json_data ='''[{ "id": "101", "Name": "Emily","Age":22 ,"Department" : "HR" },
    { "id": "102", "Name": "Charles","Age":22,"Department" : "IT"},
    { "id": "103", "Name": "George","Age":21,"Department" : "Finance"},
    { "id": "104", "Name": "Emma","Age":23,"Department" : "HR"}]'''
 
df= pd.read_json(json_data,orient='records')
df

# Here input is a JSON string that stores the data as a dictionary of values with another list. 
# Such input can be reserved by ‘records’ orientation. 
# We would convert the JSON string containing four key-value pairs in 4 rows to Pandas Dataframe.


# In[12]:


# Here the input is JSON string containing data in a dictionary of values 
# surrounded by a dictionary with a key as an index, 
# we would be using the ‘index’ orientation.

json_data='''{"employee-1": {"id": "101", "Name": "Emily","Age":22 ,"Department" : "HR" },
  "employee-2": { "id": "102", "Name": "Charles","Age":22,"Department" : "IT"},
  "employee-3":  { "id": "103", "Name": "George","Age":21,"Department" : "Finance"},
    "employee-4": { "id": "104", "Name": "Emma","Age":23,"Department" : "HR"}}'''
             
df= pd.read_json(json_data,orient='index')
df


# In[18]:


json_data='''{"employee-1": {"id": "101", "Name": "Emily","Age":22 ,"Department" : "HR" },
  "employee-2": { "id": "102", "Name": "Charles","Age":22,"Department" : "IT"},
  "employee-3":  { "id": "103", "Name": "George","Age":21,"Department" : "Finance"},
    "employee-4": { "id": "104", "Name": "Emma","Age":23,"Department" : "HR"}}'''
             
df= pd.read_json(json_data,orient='columns')
df

# When orient = columns the column indices will be the column in the data frame.
# Here the column name id, name,age, and department are the indices.


# In[26]:


json_data='''[
    [ "101","Emily",22 ,"HR" ],
    [ "102","Charles",22,"IT" ],
    [ "103","George",21, "Finance" ],
    [ "104", "Emma",23,"HR" ]
]
'''
df = pd.read_json(json_data,orient='values')
df

# The four key-values paired data have their column and row by default starting with 0. 


# In[3]:


df = pd.read_csv("D:\Anuradha\wine.data",header=None)
df
# The file wine.data is in json format.
# Observe the output by removing header parameter.


# In[ ]:


### Convert json to csv


# In[4]:


df.to_csv('wine.csv')   # Check the files list whether wine.csv file is created.


# In[5]:


df


# In[34]:


df.head()


# In[6]:


# Convert csv into json format
df.to_json()


# In[35]:


# Convert json to different json formats


# In[36]:


df.to_json(orient="index")


# In[38]:


df.to_json(orient="records")


# In[39]:


df.to_json(orient="columns")


# In[40]:


df.to_json(orient="split")


# In[41]:


df.to_json(orient="values")


# In[ ]:


### Another simple example to illustrate the orient


# In[23]:



data = '{"emp_id": {"Sree":"101"}, "email":{"Sree": "sree@gmail.com"}, "position":{"Sree": "Team Lead"}}'
df1 = pd.read_json(data)


# In[10]:


df1.to_json()


# In[25]:


df1


# In[27]:


df1.to_json(orient="records")


# In[28]:


df1.to_json(orient="columns")


# In[29]:


df1.to_json(orient="index")


# In[30]:


df1.to_json(orient="split")


# In[31]:


df1.to_json(orient="values")


# In[32]:


#####        Reading HTML content      ######
#####        It is just like web scraping    #####
#####        Web scraping is an automatic method to obtain large amounts of data from websites   #####


# In[38]:


url = 'file:///D:/Anuradha/Staff%20Details.htm'
df2 = pd.read_html(url)


# In[39]:


df2


# In[40]:


type(df2)


# In[42]:


df2[0]


# In[58]:


url1 = 'https://en.wikipedia.org/wiki/Mobile_country_code'
df3 = pd.read_html(url1)


# In[59]:


type(df3)


# In[44]:


df3


# In[45]:


df3[0]   # As it is a list, display the value in 0th index


# In[60]:


url1 = 'https://en.wikipedia.org/wiki/Mobile_country_code'
df3 = pd.read_html(url1,match='Country',header=0)  
df3[0]

#  match parameter(string/reg expr)   -  The set of tables containing text matching this regex or string will be returned.


# In[48]:


url1 = 'https://en.wikipedia.org/wiki/Mobile_country_code'
df3 = pd.read_html(url1,match='Mobile network codes',header=0)
df3[0]


# In[49]:


url2 = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
df3 = pd.read_html(url2)
df3[0]


# In[50]:


##### Reading Excel Files   #####


# In[53]:


df4 = pd.read_excel('D:\Anuradha\Staff_Details.xlsx')
df4


# In[55]:


df4.head()


# In[57]:


df4 = pd.read_excel('D:\Anuradha\Staff_Details.xlsx',header=None)
df4


# In[ ]:




