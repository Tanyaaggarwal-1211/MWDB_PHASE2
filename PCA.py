#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.image as mplib 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


# In[12]:


img = mplib.imread("Pictures/Set1/image-1.png")
print(img.shape)
plt.imshow(img)


# In[22]:


img_r = np.reshape(img, (64,64))


# In[23]:


print(img_r.shape)


# In[24]:


pca = PCA(32).fit(img_r) 
img_transformed = pca.transform(img_r) 
print(img_transformed.shape)
print(np.sum(pca.explained_variance_ratio_) )


# In[30]:


temp = pca.inverse_transform(img_transformed) 
print(temp.shape)
temp = np.reshape(temp, (64,64) )  #need to check the compressed dimensions
print(temp.shape) 
plt.imshow(temp)


# In[ ]:




