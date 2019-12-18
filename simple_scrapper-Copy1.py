#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


url = 'https://www.pagina12.com.ar/'


# In[3]:


p12 = requests.get(url)


# In[4]:


p12.status_code


# In[5]:


print(p12.text)


# In[6]:


p12.content


# In[7]:


p12.headers


# In[9]:


p12.request.headers


# In[10]:


p12.request.method


# In[12]:


p12.request.url


# In[13]:


from bs4 import BeautifulSoup


# In[14]:


s = BeautifulSoup(p12.text, 'lxml')


# In[15]:


type(s)


# In[17]:


print(s.prettify())


# In[19]:


s.find('ul', attrs={'class':'hot-sections'}).find_all('li')


# In[20]:


secciones = s.find('ul', attrs={'class':'hot-sections'}).find_all('li')


# In[21]:


secciones


# In[22]:


seccion = secciones[0]


# In[23]:


seccion


# In[24]:


seccion.find('a')


# In[25]:


seccion.a


# In[26]:


seccion..get('href')


# In[27]:


seccion.a.get('href')


# In[28]:


seccion.a.get_text()


# In[29]:


seccion.a.get('href')


# In[30]:


links_secciones = [seccion.a.get('href') for seccion in secciones]


# In[31]:


links_secciones


# In[32]:


sec = requests.get(links_secciones[0])


# In[33]:


sec


# In[34]:


s_seccion = BeautifulSoup(sec.text, 'lxml')


# In[35]:


print(s_seccion.prettify())


# In[38]:


featured_article = s_seccion.find('div', attrs={'class':'featured-article__container'})


# In[37]:


featured_article


# In[39]:


featured_article


# In[40]:


featured_article.a.get('href')


# In[41]:


article_list = s_seccion.find('ul', attrs={'class':'article-list'})


# In[42]:


article_list


# In[43]:


r = requests.get(url)


# In[44]:


r.status_code


# In[45]:


if r.status_code == 200:


# In[46]:


if r.status_code == 200:
    #Prosesamos la respuesta
else:
    #Informamos el error


# In[47]:


lista_notas


# In[48]:


url_nota = https://www.pagina12.com.ar/236404-sergio-maldonado-se-va-a-hacer-justicia-cuando-se-sepa-que-l


# In[49]:


url_nota = 'https://www.pagina12.com.ar/236404-sergio-maldonado-se-va-a-hacer-justicia-cuando-se-sepa-que-l'


# In[51]:


try:
    nota = requests.get(url_nota)
    if nota.status_code == 200:
        s_nota =  BeautifulSoup(nota.text, 'lxml')
        #Extraer titulo
        titulo = s_nota.find('div', attr={'class':'article-tittle'})
        print(titulo.text)
except Exception as e:
    print('Error:')
    print(e)
    print('\n')


# In[52]:


s_nota


# In[53]:


try:
    nota = requests.get(url_nota)
    if nota.status_code == 200:
        s_nota =  BeautifulSoup(nota.text, 'lxml')
        #Extraer titulo
        titulo = s_nota.find('div', attr={'class':'article-tittle'})
        print(titulo.text)
except Exception as e:
    print('Error:')
    print(e)
    print('\n')


# In[54]:


lista_notas

