#!/usr/bin/env python
# coding: utf-8

# In[3]:


cipher="59 6f 75 20 73 65 65 20 61 20 47 6f 6c 64 2d 42 75 67 20 69 6e 20 6f 6e 65 20 63 6f 72 6e 65 72 2e 20 49 74 20 69 73 20 74 68 65 20 6b 65 79 20 74 6f 20 61 20 74 72 65 61 73 75 72 65 20 66 6f 75 6e 64 20 62 79"
dec=[]
for i in cipher.split(" "):
    dec.append(int(i,16))
    
message=""
for i in dec:
    message+=chr(i)
print("The decrypted message is:",message)


# In[ ]:




