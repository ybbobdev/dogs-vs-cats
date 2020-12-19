#!/usr/bin/env python
# coding: utf-8

import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
import pickle


# In[12]:


DIRECTORY = '/Users/Bob/Development/ybbobdev/dogs-vs-cats'
CATREGOIES = ['cat','dog']


# In[22]:


IMG_SIZE = 100

data = []

for category in CATREGOIES:
    folder = os.path.join(DIRECTORY,category)
    label = CATREGOIES.index(category)
    for img in os.listdir(folder):
        img_path = os.path.join(folder, img)
        img_arr = cv2.imread(img_path)
        cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
        data.append([img_arr, label])


# In[21]:


len(data)


# In[23]:


random.shuffle(data)


# In[25]:


x = []
y = []

for features,labels in data:
    x.append(features)
    y.append(labels)


# In[28]:


x = np.array(x, dtype=object)
y = np.array(y, dtype=object)


# In[29]:


len(x)


# In[30]:


len(y)


# In[31]:


pickle.dump(x, open('x.pkl', 'wb'))
pickle.dump(y, open('y.pkl', 'wb'))


# In[ ]:




