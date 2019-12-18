#!/usr/bin/env python
# coding: utf-8

# In[3]:


url_base = 'https://api.spotify.com/v1'


# In[4]:


url


# In[10]:


ep_artist = '/artists/{artist_id}'


# In[7]:


id_im = '6mdiAmATAx73kdxrNrnlao'


# In[12]:


url_base+ep_artist.format(artist_id=id_im)


# In[13]:


import requests


# In[14]:


r = requests.get(url_base+ep_artist.format(artist_id=id_im))


# In[15]:


r.status_code


# In[16]:


r.json()


# In[ ]:




