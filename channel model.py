#!/usr/bin/env python
# coding: utf-8

# In[266]:


import numpy as np


# In[267]:


k=2
n = 10
p = np.arange(-(n-1)/2,(n+1)/2,1,dtype=float)      
spat_freq = np.zeros(n, )
U= np.zeros((n,n),dtype=np.complex_)
h_nlos1= np.zeros((n,k),dtype=np.complex_)
h_nlos2= np.zeros((n,k),dtype=np.complex_)
h= np.zeros((n,k),dtype=np.complex_)


# In[268]:


for ig in range(0,n):
    spat_freq[ig] = ((ig+1-(n+1)/2))
    for num in range(0,n):
        U[num][ig] = np.exp(-1j*2*np.pi*p[num]*(spat_freq[ig]/n))/np.sqrt(n)


# In[269]:


theta_user = -0.5*np.random.random_sample(k)
mul_angle1 = -0.5*np.random.random_sample(k)
mul_angle2 = -0.5*np.random.random_sample(k)


# In[270]:


los = (1/np.sqrt(2))*(np.random.randn(k)+1j*np.random.randn(k))
nlos1=  (np.sqrt(0.1))*(1/np.sqrt(2))*(np.random.randn(k)+1j*np.random.randn(k))
nlos2 = (np.sqrt(0.1))*(1/np.sqrt(2))*(np.random.randn(k)+1j*np.random.randn(k))


# In[271]:


for ig in range(0,k):
    for ro in range(0,n):
        h_nlos1[ro][ig] = nlos1[ig]*0.5*np.exp(-1j*2*np.pi*p[ro]*mul_angle1[ig])
        h_nlos2[ro][ig] = nlos2[ig]*0.5*np.exp(-1j*2*np.pi*p[ro]*mul_angle2[ig])
        h[ro][ig] = los[ig]*0.5*np.exp(-1j*2*np.pi*p[ro]*theta_user[ig])


# In[272]:


H = np.transpose(np.conjugate(U))@(h+h_nlos1+h_nlos2)


# In[273]:


abs(H)


# In[ ]:





# In[ ]:




