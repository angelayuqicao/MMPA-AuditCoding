#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import read_csv
filename = "FY2014.csv"
dataset1 = read_csv (filename,encoding = "ISO-8859-1")


# In[2]:


names = ['AgenNo','AgenName','ChLName','ChFIni','Descr','Amt','Ven','TranDate','PoDate','MCC']


# In[3]:


dataset1 = read_csv(filename,header=0,names = names,encoding = "ISO-8859-1")


# In[4]:


dataset1['TranDate'] = pd. to_datetime(dataset1['TranDate'], format = '%m/%d/%Y %H:%M')


# In[5]:


dataset1['PoDate'] = pd. to_datetime(dataset1['PoDate'], format = '%m/%d/%Y %H:%M')


# In[6]:


dataset1['Amt'] = dataset1['Amt'].replace('$','')


# In[7]:


dataset1['Amt'] = dataset1['Amt'].replace(',','')


# In[8]:


dataset1['Amt'] = dataset1['Amt'].replace('(','-')


# In[9]:


dataset1['Amt'] = dataset1['Amt'].replace(')','')


# In[10]:


dataset1['Amt'] = dataset1['Amt'].astype(float)


# In[11]:


dataset1['AgenName'] = dataset1['AgenName'].str.strip()


# In[12]:


dataset1['ChLName'] = dataset1['ChLName'].str.strip()


# In[13]:


dataset1['ChFIni'] = dataset1['ChFIni'].str.strip()


# In[14]:


dataset1['Descr'] = dataset1['Descr'].str.strip()


# In[15]:


dataset1['Ven'] = dataset1['Ven'].str.strip()


# In[16]:


dataset1['MCC'] = dataset1['MCC'].str.strip()


# In[17]:


import pandas as pd
from pandas import read_csv
filename = "FY2015.csv"
dataset2 = read_csv (filename,encoding = "ISO-8859-1")


# In[18]:


names = ['AgenNo','AgenName','ChLName','ChFIni','Descr','Amt','Ven','TranDate','PoDate','MCC']


# In[19]:


dataset2 = read_csv(filename,header=0,names = names,encoding = "ISO-8859-1")


# In[20]:


dataset2['TranDate'] = pd. to_datetime(dataset2['TranDate'], format = '%m/%d/%Y %H:%M')


# In[21]:


dataset2['PoDate'] = pd. to_datetime(dataset2['PoDate'], format = '%m/%d/%Y %H:%M')


# In[22]:


dataset2['Amt'] = dataset2['Amt'].str.replace('$','')


# In[23]:


dataset2['Amt'] = dataset2['Amt'].str.replace(',','')


# In[24]:


dataset2['Amt'] = dataset2['Amt'].str.replace(')','')


# In[25]:


dataset2['Amt'] = dataset2['Amt'].str.replace('(','-')


# In[26]:


dataset2['Amt'] = dataset2['Amt'].astype(float)


# In[27]:


dataset2['AgenName'] = dataset2['AgenName'].str.strip()


# In[28]:


dataset2['ChLName'] = dataset2['ChLName'].str.strip()


# In[29]:


dataset2['ChFIni'] = dataset2['ChFIni'].str.strip()


# In[30]:


dataset2['Descr'] = dataset2['Descr'].str.strip()


# In[31]:


dataset2['Ven'] = dataset2['Ven'].str.strip()


# In[32]:


dataset2['MCC'] = dataset2['MCC'].str.strip()


# In[33]:


dataset = pd.concat([dataset1,dataset2])


# # Dataset Information

# In[34]:


dataset['Amt'].sum()


# In[35]:


dataset.head()


# In[36]:


dataset.info()


# In[37]:


from_OSU = dataset.AgenName == 'OKLAHOMA STATE UNIVERSITY'


# In[38]:


in_2014 = dataset.TranDate.dt.year == 2014


# In[39]:


OSU_2014 = dataset[from_OSU & in_2014]


# In[40]:


OSU_2014.info()


# # Test 1

# In[41]:


display_OSU_2014 = OSU_2014[['ChLName','ChFIni','Descr','Amt','Ven','TranDate','PoDate','MCC']]


# In[42]:


atleast5000 = display_OSU_2014.Amt > 5000


# In[43]:


atleast5000_df = display_OSU_2014[atleast5000]


# In[44]:


tran5000=atleast5000_df.sort_values('Amt',ascending=False)


# In[45]:


tran5000


# In[46]:


tran5000.shape


# # Test 2

# In[47]:


d2_OSU_2014 = OSU_2014[['ChLName','ChFIni','Amt']]


# In[48]:


by_employee=d2_OSU_2014.groupby(['ChLName','ChFIni'])


# In[49]:


total_by_employee=d2_OSU_2014.groupby(['ChLName','ChFIni']).sum()


# In[50]:


atleast50000y = total_by_employee.Amt > 50000


# In[51]:


atleast50000y_df = total_by_employee[atleast50000y]


# In[52]:


year50000=atleast50000y_df.sort_values('Amt',ascending=False)


# In[53]:


year50000


# In[54]:


year50000.shape


# # Test 3

# In[55]:


d3_OSU_2014 = OSU_2014[['ChLName','ChFIni','Amt','TranDate']]


# In[56]:


d3_OSU_2014['TranDate'] = d3_OSU_2014['TranDate'].dt.month


# In[57]:


d3_OSU_2014.rename(columns = {'TranDate':'TranMonth'},inplace = True)


# In[58]:


mtotal_by_employee = d3_OSU_2014.groupby(['TranMonth','ChLName','ChFIni']).sum()


# In[59]:


atleast10000m = mtotal_by_employee.Amt > 10000


# In[60]:


atleast10000m_df = mtotal_by_employee[atleast10000m]


# In[61]:


month10000=atleast10000m_df.sort_values(['TranMonth','Amt'],ascending=[True,False])


# In[62]:


month10000


# In[63]:


month10000.shape


# # Test 4

# In[64]:


dtran = OSU_2014


# In[65]:


dtran = dtran.assign(count_tran = 1)


# In[66]:


splittran = dtran.groupby(['ChLName','ChFIni','Ven','TranDate'])[['count_tran','Amt']].sum()


# In[67]:


atleast1tran = splittran.count_tran>1


# In[68]:


atleast5000 = splittran.Amt>5000


# In[69]:


atleast5000d_df = splittran[atleast1tran & atleast5000]


# In[70]:


day5000=atleast5000d_df.sort_values(['TranDate'])


# In[71]:


day5000


# In[72]:


day5000.shape


# # Test 5

# In[73]:


frequency = day5000.groupby(['ChLName','ChFIni'])['count_tran'].count().sort_values(ascending = False)


# In[74]:


frequency = pd.DataFrame(frequency)


# In[75]:


frequency


# In[76]:


frequency.shape


# In[ ]:




