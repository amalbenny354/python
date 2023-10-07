#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
x=np.array([1,2,3,4,5])
print(x)
print(type(x))
print(x.shape)


# In[2]:


y=np.array([[1,2],[3,2]])
print(y)
print(type(y))
print(y.shape)


# In[8]:


z=np.array([[3+4j,5+1j]])
print(z)
print(type(z))
print(z.shape)


# In[18]:


h=np.zeros((2,4))
print(h)


# In[19]:


print(h.shape)


# In[27]:


j=np.ones((2,3), dtype=int)
print(j)


# In[29]:


n=np.eye(3)
print(n)


# In[31]:


s=np.arange(12)
print(s)


# In[33]:


w=np.arange(2,7)
print(w)


# In[35]:


q=np.arange(2,17,3)
print(q)


# In[36]:


f=np.linspace(1,5,7)
print(f)


# In[38]:


m=np.random.random((5,6))
print(m)


# In[41]:


k=np.random.random((3,6))
print(k.reshape(2,3,3))


# In[43]:


x=np.arange(12)
print(x)
print(x[4])


# In[44]:


print(x[-1])


# In[45]:


x.resize(3,4)
print(x)


# In[46]:


print(x[-1,-1])


# In[49]:


print(x[1][3])


# In[51]:


g=np.arange(1,36)
print(g)
print(g[:5])


# In[52]:


print(g[12:])


# In[53]:


print(g[5:9])


# In[54]:


print(g[:-5])


# In[55]:


print(g[-7:])


# In[56]:


print(g[4:-6])


# In[57]:


print(g[::3])


# In[62]:


y=g.reshape((7,5))
print(y)


# In[63]:


print(y[::3])


# In[64]:


print(y[:3,:3])


# In[66]:


print(y[2:-1,1:-1])


# In[67]:


print(y[:,:3])


# In[68]:


print(y[:,:-1])


# In[69]:


print(y[::2,::2])


# In[70]:


print(y)


# In[71]:


print(y[1::2])


# In[77]:


a=np.arange(1,6)
b=np.arange(6,11)
print(a)
print(b)
print(a-b)
print(a+b)
print(a/b)
print(a*b)


# In[78]:


print(a>3)


# In[79]:


a=np.arange(0,4).reshape((2,2))
print(a)


# In[87]:


b=np.eye(2,2)
print(b)


# In[84]:


print(a*b)


# In[85]:


print(np.arange(1,10).reshape(3,3))


# In[88]:


print(np.dot(a,b))


# In[12]:


import numpy as np
x = np.arange(1,10).reshape(3,3)
print(x)


# In[13]:


print(x.sum())


# In[16]:


print(x.sum(axis=0))


# In[17]:


print(x.sum(axis=1))


# In[20]:


m=np.arange(1,19).reshape(3,3,2)
print(m)


# In[21]:


print(m.sum(axis=0))


# In[22]:


print(m.sum(axis=1))


# In[25]:


k=np.arange(1,10).reshape(3,3)
print(k)

print(k.max())


# In[26]:


print(k.max(axis=0))


# In[27]:


print(k.max(axis=1))


# In[28]:


print(k.transpose())

