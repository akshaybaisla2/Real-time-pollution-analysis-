#!/usr/bin/env python
# coding: utf-8

# # Real time pollution analysis
# 
# #  api : http://api.waqi.info/
# # api key: 2d4c9cb7049e7c6d411f900167d3bbf5d410e5d5

# In[2]:


import requests


# In[3]:


#requesting api
name = 'India'
url = 'http://api.waqi.info/feed/' + name + '/?token='
api_key = '2d4c9cb7049e7c6d411f900167d3bbf5d410e5d5'


# In[4]:


main_url = url + api_key
r = requests.get(main_url)
data = r.json()
data


# # EDA

# In[5]:


#extracting smaller 'data' dictionary from data(json)
main_url = url + api_key
r = requests.get(main_url)
data = r.json()['data']
data


# In[9]:


#Extracting AQI
aqi = data['aqi']
print("Aqi of india is=" ,aqi)


# In[13]:


#Extracting pollutants
iaqi = data['iaqi']
print(" Pollutants: ", iaqi)


# In[14]:


for i in iaqi.items():
    print(i[0],':',i[1]['v'])


# In[15]:


#Deleting some pollutants
del iaqi['t']
del iaqi['w']


# In[20]:


del iaqi['p']
del iaqi['wg']


# In[21]:


iaqi


# In[19]:


for i in iaqi.items():
    print(i[0],':',i[1]['v'])


# In[25]:


dew = iaqi.get('dew')
o3 = iaqi.get('o3')
so2 = iaqi.get('so2')
pm10 = iaqi.get('pm10')
pm25 = iaqi.get('pm25')
co= iaqi.get('co')
h= iaqi.get('h')



print(f'{name} AQI :',aqi,'\n')
print('Individual Air quality')
print('Dew :',dew)
print('ozone :',o3)
print('sulphur di-oxide :',so2)
print('pm10 :',pm10)
print('pm2.5 :',pm25)
print('carbon monoxide :',co)
print('hydrogen :', h)


# # Plotting graphs/charts to better analyse the pollutants data

# In[42]:


#pollutant graph/chart

import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


pollutants = [i for i in iaqi]
values = [i['v'] for i in iaqi.values()]


# In[36]:


print(pollutants)


# In[37]:


print(values)


# In[59]:


from matplotlib import pyplot as plt

# bar plot
plt.bar(pollutants,values,label="concentration",width=.9)

plt.legend()
plt.xlabel('pollutants')
plt.ylabel('concentration')
plt.title('Different pollutants concentration')

plt.show()


# # Analysis: As clear with output pm2.5 with highest concentration is the dominant pollutant 

# In[65]:


#plotting the pollutant data with the help of bar chart

pollutants = [i for i in iaqi]
values = [i['v'] for i in iaqi.values()]


# Exploding the first slice
explode = [0 for i in pollutants]
mx = values.index(max(values))  # explode 1st slice
explode[mx] = 0.1

# Plot a pie chart
plt.figure(figsize=(8,6))
plt.pie(values, labels=pollutants,explode=explode,autopct='%1.1f%%', shadow=True)

plt.title('Air pollutants and their probable amount in atmosphere [India]')

plt.axis('equal')
plt.show()


# # showing INDIA AQI on world map using cartopy

# In[82]:


import cartopy.crs as ccrs


# In[83]:


geo = data['city']['geo']

fig = plt.figure(figsize=(12,10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

plt.scatter(geo[1],geo[0],color='blue')
plt.text(geo[1] + 3,geo[0]-2,f'{name} AQI \n    {aqi}',color='red')

plt.show()

