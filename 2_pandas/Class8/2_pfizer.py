import numpy as np
import pandas as pd
import os as os

data = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"pfizer_1.csv"))
print('shape of the pfizer: ',data.shape)
print('data info of pfizer:\n',data.info())
print('pfizer data:\n',data.head())

#structure the data into more readable format using Time columns to rows (NOT transpose)
data_melt = pd.melt(data,id_vars=['Date','Parameter','Drug_Name'])
print('raw melt data:\n',data_melt)
data_melt = pd.melt(data,id_vars=['Date','Parameter','Drug_Name'],var_name='time',value_name='reading')
print('shape after pd.melt():\n',data_melt)

# #opposite of melting is pivoting -> goes back to original data
data_pivot = data_melt.pivot(index=['Date','Drug_Name','Parameter'],
                columns='time',
                values='reading').reset_index()
print('pivoted data:\n',data_pivot)

# convert the Parameter pivot to Temperature and Pressure columns
data_tidy = data_melt.pivot(index=['Date','time','Drug_Name'],
                columns='Parameter'
                ,values='reading')
data_tidy.reset_index(inplace=True)
print('pivoted data for temperature and pressure:\n',data_tidy)

#bin'ning or buckets for data
data_tidy['Temperature'].min()
data_tidy['Temperature'].max()

temp_points = [5,20,35,50,60] #helpful in visualization
temp_labels = ['low','medium','high','very_high']
data_tidy['temp_cat'] = pd.cut(data_tidy['Temperature'],bins=temp_points,labels=temp_labels)
print('temp category data:\n',data_tidy)
print('category counts:\n', data_tidy['temp_cat'].value_counts())

print('sample of numericals columns with None:\n', pd.Series([1,np.nan,2,None]))
print('sample of non-numericals columns with Nan:\n', pd.Series(['Hi',np.nan,'Hello',None]))

print('check how many null values in the data.isna():\n',data.isna())
print('check how many null values in the data.isnull() same as data.isna():\n',data.isnull())
print('how many values are null for each column:\n',data.isna().sum())
print('row wise missing values:\n',data.isna().sum(axis=1))

print('drop the rows null values, leaves very minimal data which is not good:\n', data.dropna())#default axis=0
print('drop the cols null values, leaves very minimal data which is not good:\n', data.dropna(axis=1))

#write back the clean data to file
data_tidy.to_csv(os.path.join(os.path.dirname(os.getcwd()),"pfizer_data_tidy.csv"),index=False)

# other option is data imputation => replace constant(like 0), mean, median, custom