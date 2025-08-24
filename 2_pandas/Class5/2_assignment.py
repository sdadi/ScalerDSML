import numpy as np
import pandas as pd
import os as os

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")
df = pd.read_csv(os.path.join(assets_path,"mckinsey.csv"))
os.system('cls')
#Q1 first 20 rows
print('first 20 rows using df.head(20) and df.iloc[:20]:',df.head(20),df.iloc[:20])

#Q2 
print('unique() on df:', df.nunique())

#Q3 extract data in specified columns order
df_tips = pd.read_csv(os.path.join(assets_path,"tips.csv"))
print('first 2 rows:\n', df_tips.head(2))
print(df_tips.columns)
print('extract the mentioned columns in the order: time, total_bill, tip',pd.DataFrame(df_tips,columns=['time','total_bill','tip']))
# df_with_cols = df_tips[['time','total_bill','tip']]
print('extract the mentioned columns in the order: [time, total_bill, tip]\n',df_tips[['time','total_bill','tip']])
print('extract the mentioned columns in the order: loc[:,[time, total_bill, tip]]\n',df_tips.loc[:,['time','total_bill','tip']])
print('extract the mentioned columns in the order: iloc[:,0:2]\n',df_tips.iloc[:,0:2]) #not correct as it gives total_bill,tip only

#Q4 df.loc[:2,"total_bill":"day"]
print('print 2 rows with 3 columns :',df_tips.loc[:2,'total_bill':'day'])
df_cars = pd.read_csv(os.path.join(assets_path,"mtcars.csv"))
# print(df_cars)
#setting model as indexing column
df_cars.set_index("model",inplace=True)
print('print 2,3,4, rows and 4,5 columns:', df_cars.iloc[1:5,3:5])
# print(df_cars.iloc[1:4,3:4])
# print(df_cars.loc[1:5,3:5])
# print(df_cars.loc[1:6,3:6])

#Q1.1 print all rows of 'disp'

print('printing all rows of disp col: ', df_cars['disp'],df_cars.loc[:,'disp'])
# print('printing all rows of disp col: slicing works only with int for iloc like df_cars.iloc[:,2:3] ', df_cars.iloc[:,'disp'])

#Q1.2
# print('option-a: fails as rows has 2 col data only ',pd.DataFrame([[1, 2], ["Ram", "Shyam"], ["IT", "Ops"]], columns = ["emp_id", "name", "dept"]))
print('option-b: ', pd.DataFrame([[1, "Ram", "IT"], [2, "Shyam", "Ops"]], columns = ["emp_id", "name", "dept"]))
# print('option-c: invalid df construct: row data should be 2D',pd.DataFrame([1,'Ram', 'IT'],columns=['emp_id','name','dept']))
print('option-d: ',pd.DataFrame({'emp_id':[1, 2], 'name': ['Ram', 'Shyam'], 'dept':['IT', 'Ops']}))
