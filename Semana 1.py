#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header = None)


# In[6]:


df.head(5)


# In[13]:


headers=["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "lenght", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price" ]


# In[14]:


df.columns=headers


# In[16]:


df.head(5)


# In[20]:


path="C:/Users/Utilizador/Desktop/automobile.csv"

df.to_csv(path)


# In[ ]:




