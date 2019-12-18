#!/usr/bin/env python
# coding: utf-8

# In[1]:


url = https://www.latam.com/es_un/apps/personas/booking?fecha1_dia=14&fecha1_anomes=2019-12&auAvailability=1&ida_vuelta=ida&vuelos_origen=Buenos%20Aires&from_city1=BUE&vuelos_destino=Madrid&to_city1=MAD&flex=1&vuelos_fecha_salida_ddmmaaaa=13/12/2019&cabina=Y&nadults=1&nchildren=0&ninfants=0&cod_promo=&stopover_outbound_days=0&stopover_inbound_days=0&application=#/


# In[2]:


url = 'https://www.latam.com/es_un/apps/personas/booking?fecha1_dia=14&fecha1_anomes=2019-12&auAvailability=1&ida_vuelta=ida&vuelos_origen=Buenos%20Aires&from_city1=BUE&vuelos_destino=Madrid&to_city1=MAD&flex=1&vuelos_fecha_salida_ddmmaaaa=13/12/2019&cabina=Y&nadults=1&nchildren=0&ninfants=0&cod_promo=&stopover_outbound_days=0&stopover_inbound_days=0&application=#/'


# In[3]:


import requests


# In[4]:


from bs4 import BeautifulSoup


# In[6]:


r= requests.get(url)


# In[7]:


r.status_code


# In[8]:


s = BeautifulSoup(r.text, 'lxml')


# In[9]:


print(s.prettify())


# In[10]:


from selenium import webdriver


# In[13]:


driver = webdriver.Chrome(executable_path='/chromedriver')


# In[19]:


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='C:/Users/jadamson/Downloads/chromedriver_win32v78/chromedriver', options=options)


# In[20]:


driver.get(url)


# In[23]:


vuelos = driver.find_elements_by_xpath('//li[@class="flight"]')


# In[24]:


vuelos


# In[25]:


vuelo = vuelos[0]


# In[26]:


vuelo


# In[31]:


vuelo.find_element_by_xpath('.//div[@class="arrival"]/time').get_attribute('datetime')


# In[32]:


btn_escalas = vuelo.find_element_by_xpath('.//div[@class="flight-summary-stops-description"]/button')


# In[33]:


btn_escalas


# In[34]:


btn_escalas.click()


# In[36]:


sementos = vuelo.find_elements_by_xpath('//div[@class="segments-graph"]/div[@class"segments-graph-segment"]')


# In[ ]:




