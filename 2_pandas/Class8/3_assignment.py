import numpy as np
import pandas as pd

data = pd.DataFrame({
    'Student ID':[1,1,1,2,2,2],
    'Subject':['Mathematics','Physics','Chemistry','Mathematics','Physics','Chemistry'],
    'Score':[85,78,92,72,80,88]
})
print(data)
data_melt = pd.pivot(data,index=['Student ID'],columns='Subject',values='Score')
print('melt data of students:\n',data_melt)



df = pd.DataFrame({
  "Accessories": ["Laptop", "Laptop", "Ipad", "Ipad", "Tablet", "Laptop"],
  "customer": ["Andrew", "Andrew", "Tom", "Andrew", "Tobey", "Peter"],
  "quantity": [1, 2, 2, 3, 1, 2],
})
df.fillna()

# print(pd.pivot(df,index=['Accessories'],columns='customer',values='quantity'))
print(df.groupby(['Accessories','customer']).quantity.sum())