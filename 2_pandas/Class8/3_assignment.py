import numpy as np
import pandas as pd
import os as os

os.system('cls')
# Q1 melt/pivot to find the average score of each student across all subjects
data = pd.DataFrame({
    'Student ID':[1,1,1,2,2,2],
    'Subject':['Mathematics','Physics','Chemistry','Mathematics','Physics','Chemistry'],
    'Score':[85,78,92,72,80,88]
})
print(data)
data_melt = pd.pivot(data,index=['Student ID'],columns='Subject',values='Score')
print('melt data of students:\n',data_melt)
data_melt['avg'] = data_melt.mean(axis=1)
print('final data with avg:\n',data_melt)


df = pd.DataFrame({
  "Accessories": ["Laptop", "Laptop", "Ipad", "Ipad", "Tablet", "Laptop"],
  "customer": ["Andrew", "Andrew", "Tom", "Andrew", "Tobey", "Peter"],
  "quantity": [1, 2, 2, 3, 1, 2],
})
# df.fillna()

# print(pd.pivot(df,index=['Accessories'],columns='customer',values='quantity'))
print(df.groupby(['Accessories','customer']).quantity.sum())

# Q8. Location Divide

df = pd.DataFrame({'City\tState': ["Kolkata\tWest Bengal", "Chennai\tTamil Nadu", "Hyderabad\tTelengana", "Bangalore\tKarnataka"]})
print(df)
list = df['City\tState'].str.split('\t',expand=True)
print(list)
# df.columns = ['City','State']
df = list.columns=['City','State']
print(type(list))

#  Q9 Get Data atributes
df = pd.DataFrame({
    'RID':[56, 92, 29, 93, 55, 32],
'RDate':['2021-01-01', '2021-02-12', '2021-04-16', '2021-01-22', '2021-01-15', '2021-02-26']
})

print('original df:\n',df)
df['RDate'] = pd.to_datetime(df['RDate'])
df['RMonth'] = df['RDate'].dt.month
df['RYear'] = df['RDate'].dt.year
df['RDay'] = df['RDate'].dt.day
print('final df with new attributes:\n',df)