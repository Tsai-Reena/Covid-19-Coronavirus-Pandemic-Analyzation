#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Data Preperation

# In[2]:


df = pd.read_csv("COVID-19 Coronavirus.csv", encoding='windows-1252')


# In[3]:


pd.DataFrame(df.head())


# In[4]:


print(f'Shape of the dataset is : {df.shape}') 


# In[5]:


df.info()


# In[6]:


df.describe()


# ### 1. Missing Value Processing

# In[7]:


# 填補缺失值

df['Population'].fillna(value=df['Population'].mean(), inplace=True)
df['Total Cases'].fillna(value=df['Total Cases'].mean(), inplace=True)
df['Total Deaths'].fillna(value=df['Total Deaths'].mean(), inplace=True)
df['Tot Cases//1M pop'].fillna(value=df['Tot Cases//1M pop'].mean(), inplace=True)
df['Tot Deaths/1M pop'].fillna(value=df['Tot Deaths/1M pop'].mean(), inplace=True)
df['Death percentage'].fillna(value=df['Death percentage'].mean(), inplace=True)
df.head()


# In[8]:


df.isna().sum()


# In[9]:


df=df.drop('Other names', axis=1)


# ### 2. Data Scaling

# In[10]:


from sklearn.preprocessing import MinMaxScaler


# In[11]:


data = np.transpose(df[['Population', 'Total Cases', 'Total Deaths', 'Tot Cases//1M pop', 
                        'Tot Deaths/1M pop', 'Death percentage']])


# In[12]:


col = df['Continent']
data.columns = col
index = data.index
data


# In[13]:


from sklearn import preprocessing
x_scale = preprocessing.scale(data)
x_scale


# In[14]:


data = pd.DataFrame(x_scale)
data.head()


# In[15]:


data.columns = col


# In[16]:


data.index = index
data


# In[17]:


data = data.transpose()
data


# ## Data Visualization

# In[18]:


cases_per_continent = data.groupby('Continent').sum()
cases_per_continent


# In[19]:


data.reset_index(inplace = True)
data


# In[20]:


# Matplotlib scatter plot with different hues : x= Country, y = population

# filter data down to only one Country, as all population values are equal for a Country.
temp_data = df[['Country', 'Population']].drop_duplicates(subset="Country", keep="first")

# sort data for plotting, based on ascending population
temp_data.sort_values('Population', inplace=True)

# Initiate figure and plot
fig, ax = plt.subplots(figsize = (40,15))
plt.scatter(x='Country', y='Population', data=temp_data, c=temp_data.index, cmap="rainbow")

# Axis and formatting
ax.set_title("Scatterplot to show the population (log-scale) of different countries", fontsize = 20)
ax.set_xticklabels(temp_data['Country'], rotation = 90)
ax.set_xlabel("Country", fontsize = 20)
ax.set_ylabel("Population (Log-scale)", fontsize = 20)
ax.set_yscale("log")

plt.margins(x=0.01)


# In[21]:


plt.figure(figsize=(20,8))
plt.bar(df['Continent'], df['Population'],color='red',alpha=1)


# In[22]:


columns1 = ['Population', 'Total Cases', 'Total Deaths']
columns2 = ['Tot Cases//1M pop', 'Tot Deaths/1M pop', 'Death percentage']
continents = ['Asia', 'Europe', 'Africa', 'Latin America and the Caribbean', 'Oceania', 'Northern America']

for column in columns1:
    mean = []
    for continent in continents:
        mean.append(df.loc[df['Continent'] == continent, [column]].sum())
    mean = np.array(mean)
    mean = np.reshape(mean, 6)
#     print(mean)
    plt.figure(figsize=(20,8))
    plt.bar(continents, mean, color='red', alpha=1)
    plt.ylabel(column, fontsize = 20)
    plt.xlabel("Continent", fontsize = 20)
    plt.title(f'6 continents per {column}', fontsize = 20)
    plt.show()
    
for column in columns2:
    mean = []
    for continent in continents:
        mean.append(df.loc[df['Continent'] == continent, [column]].mean())
    mean = np.array(mean)
    mean = np.reshape(mean, 6)
#     print(mean)
    plt.figure(figsize=(20,8))
    plt.bar(continents, mean, color='red', alpha=1)
    plt.ylabel(column, fontsize = 20)
    plt.xlabel("Continent", fontsize = 20)
    plt.title(f'6 continents per {column}', fontsize = 20)
    plt.show()


# In[23]:


#Scatter Plot
plt.scatter(data["Population"], data["Death percentage"])

plt.title("Country Population and COVID Death Percentage")
plt.xlabel("Population")
plt.ylabel("Death Percent")
plt.show()


# In[24]:


# Boxplot
plt.boxplot(df["Death percentage"])

plt.title("COVID Death Percentages")
plt.show()

