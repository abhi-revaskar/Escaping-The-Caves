#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="01000011001110000101100101010000001101110110111101001100011011110011011001011001"
octs=[]
s=""
c=0
for i in a:
    if c==8:
        octs.append(s)
        c=1
        s=i
    else:
        s+=i
        c+=1
octs.append(s)


# In[2]:


dec=[]
for i in octs:
    dec.append(int(i,2))


# In[3]:


password=""
for i in dec:
    password+=(chr(i))
    
print("Password is:",password)


# In[ ]:




