#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install openai')


# In[2]:


import json
import openai
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[3]:


with open('GPT_SECRET_KEY.json') as f:
    data = json.load(f)


# In[4]:


openai.api_key = data["API_KEY"]


# In[5]:


from gpt import GPT
from gpt import Example


# In[6]:


gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)


# In[7]:


df = pd.DataFrame({"Gender": ["boy", "boy", "boy", "boy", "boy",
                         "girl", "girl", "girl", "girl"],
                   "Division": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "Marks": [50, 55, 67, 85, 44, 84, 65, 56, 87]})


# In[8]:


df


# # Adding Examples for GPT Model

# In[9]:


gpt.add_example(Example('How many unique values in Division Column?', 
                        'df["Division"].nunique()'))


# In[10]:


gpt.add_example(Example('Find the Division of boy who scored 55 marks', 
                        'df.loc[(df.loc[:, "Gender"] == "boy") & (df.loc[:, "Marks"] == 55), "Division"]'))


# In[11]:


gpt.add_example(Example('Find the average Marks scored by Girls', 
                        'np.mean(df.loc[(df.loc[:, "Gender"] == "girl"), "Marks"])'))


# In[ ]:





# # Example 1

# In[12]:


prompt = "Display Division of girl who scored maximum marks"


# In[13]:


gpt.get_top_reply(prompt)


# In[14]:


response = gpt.get_top_reply(prompt)
print(response)
modified_response = response.split("output: ")[-1].strip('\n')
eval(modified_response)


# # Example 2

# In[15]:


prompt = "Find the median Marks scored by Boys"


# In[16]:


response = gpt.get_top_reply(prompt)
print(response)
modified_response = response.split("output: ")[-1].strip('\n')
eval(modified_response)


# # Matplotlib

# In[ ]:





# In[17]:


df = pd.read_csv("iris.csv")


# In[18]:


df.head()


# In[19]:


gpt.add_example(Example('Plot Scatter Plot between Sepal Length & Sepal Width', 
                        "plt.scatter(df['sepal_length'], df['sepal_width'])"))


# In[20]:


gpt.add_example(Example('Plot Bar Plot of Species', 
                        "sns.countplot('species',data=df)"))


# In[21]:


gpt.add_example(Example('Plot a Joint Plot between Sepal Length & Petal Length', 
                        "sns.jointplot(x='sepal_length',y='petal_length',data=df)"))


# In[22]:


gpt.add_example(Example('Show me the histogram of Petal Length', 
                        "plt.hist(df['petal_length'])"))


# In[ ]:





# # Example 3

# In[23]:


prompt = "Show me the scatter plot between petal length and sepal width"


# In[24]:


response = gpt.get_top_reply(prompt)
print(response)
modified_response = response.split("output: ")[-1].strip('\n')
eval(modified_response)


# # Example 4

# In[25]:


prompt = "Show me the Joint Plot between Petal Length & Petal Length"


# In[26]:


response = gpt.get_top_reply(prompt)
print(response)
modified_response = response.split("output: ")[-1].strip('\n')
eval(modified_response)


# # Example 5

# In[27]:


prompt = "Show me the Distribution of Sepal Length"


# In[28]:


response = gpt.get_top_reply(prompt)
print(response)
modified_response = response.split("output: ")[-1].strip('\n')
eval(modified_response)


# In[ ]:




