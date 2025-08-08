import numpy as np
import pandas as pd
import os as os

data = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"pfizer_1.csv"))

data_melt = pd.melt(data,id_vars=['Date','Parameter','Drug_Name'],var_name='time',value_name='reading')

data_tidy = data_melt.pivot(index=['Date','time','Drug_Name'],
                columns='Parameter'
                ,values='reading')
data_tidy.reset_index(inplace=True)

print(data_tidy['Drug_Name'])
print('type of Drug_Name:\n',type(data_tidy['Drug_Name']), type(data_tidy['Drug_Name'].str))

def extract_year(date):
    return date[2]

print('year part :\n',data_tidy['Date'].str.split('-').apply(extract_year).astype('int'))

#datetimes method
data_tidy['timestamp'] = data_tidy['Date']+ ' '+data_tidy['time']
print('data_time', data_tidy)

data_tidy['timestamp'] = pd.to_datetime(data_tidy['timestamp'])
print('after timestamp col type changed to datetime:\n',data_tidy.info())

print('get hours data:\n',data_tidy['timestamp'].dt.day_name(),data_tidy['timestamp'].dt.month_name())