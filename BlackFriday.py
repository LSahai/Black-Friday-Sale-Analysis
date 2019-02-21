#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib import pyplot


# In[31]:


ap = pd.read_csv("F:/Semester 2nd/Multi Variate/Project/Blackfriday.csv")
ap.head(10)


# In[32]:


ap.info()


# In[33]:


ap.isnull().sum()


# In[35]:


ap.columns


# In[36]:


ap.sort_values('User_ID').head(10)
ap['User_ID'].value_counts().count() 


# In[41]:


ap['Gender'].unique()


# In[42]:


plt.subplot(1,2,1)
sns.countplot(ap['Gender']) #attendance

m_purchase = ap.groupby(['Gender'])['Purchase'].sum()
plt.subplot(1,2,2)
sns.barplot(m_purchase.index, m_purchase.values) #dollar value


# In[43]:


sns.countplot(ap['Marital_Status'])


# In[44]:


sns.countplot(ap['Gender'], hue = ap['Marital_Status'])


# In[45]:


sns.countplot(ap['Stay_In_Current_City_Years'])


# In[46]:


sns.countplot(ap['City_Category'])


# In[47]:


sns.countplot(ap['Occupation'])


# In[48]:


sns.countplot(ap['Age'])


# In[49]:


sns.countplot(ap['Product_Category_1'])


# In[50]:


sns.countplot(ap['Product_Category_2'])


# In[51]:


sns.countplot(ap['Product_Category_3'])


# In[52]:


fig1, ax1 = plt.subplots(figsize=(12,7))
sns.countplot(ap['Age'],hue=ap['Gender'])

def plot(group,column,plot):
    ax=plt.figure(figsize=(12,6))
    ap.groupby(group)[column].sum().sort_values().plot(plot)
plot('Age','Purchase','bar')


# In[70]:


# Bar charts - show median instead of mean of total amount of purchase by each characteristic
import numpy as np
fig5, axes = plt.subplots(3,2,figsize=(20,16))

fig5.suptitle('Median Amount of Purchase by Customer Groups', fontsize = 16, y = 0.93)

sns.barplot(x='Gender', y='Tot_Purchase', data = ap_customer, estimator = np.median, ci = None, ax = axes[0][0])
sns.barplot(x='Age', y='Tot_Purchase', data = ap_customer, estimator = np.median, ci = None, 
            ax = axes[0][1], order = ['0-17', '18-25', '26-35', '36-45', '46-50', '51-55', '55+'])
sns.barplot(x='Occupation', y='Tot_Purchase', data = ap_customer, estimator = np.median, ci = None, ax = axes[1][0])
sns.barplot(x='City_Category', y='Tot_Purchase', data = ap_customer, estimator = np.median, 
            ci = None, ax = axes[1][1], order = ('A', 'B', 'C'))
sns.barplot(x='Stay_In_Current_City_Years', y='Tot_Purchase', data = ap_customer, estimator = np.median, 
            ci = None, ax = axes[2][0], order = ('0', '1', '2', '3', '4+'))
sns.barplot(x='Marital_Status', y='Tot_Purchase', data = ap_customer, estimator = np.median, ci = None, ax = axes[2][1])

for ax in fig5.axes:
    plt.sca(ax)
    plt.ylabel('Median Total Amount of Purchase (/Thousand $)')
 
plt.savefig('fig5')


# In[ ]:




