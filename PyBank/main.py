#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv("budget_data.csv")


# In[4]:


data


# In[5]:


#total month
total_month = data.shape[0]


# In[7]:


#The net total amount of Profit/Losses over the entire period.
total_amount = data['Profit/Losses'].sum()


# In[23]:


#The average of the changes in Profit/Losses over the entire period.
data['day_shift'] = data['Profit/Losses'].shift(1)
data['change'] = data['Profit/Losses'] - data.day_shift
average = data['change'].mean()


# In[43]:


#The greatest increase in profits (date and amount) over the entire period.

#data.set_index("Date", inplace = True)
great_increase = data['change'].idxmax()
increase = data.loc[great_increase,'change']


# In[48]:


#The greatest decrease in losses (date and amount) over the entire period.
great_loss = data['change'].idxmin()
loss = data.loc[great_loss,'change']


# In[54]:


print('Financial Analysis')
print(f"Total Months: {total_month}")
print(f"Total: ${total_amount}")
print(f"Average  Change: ${average}")
print(f"Greatest Increase in Profits: {great_increase} (${increase})")
print(f"Greatest Decrease in Profits: {great_loss} (${loss})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




