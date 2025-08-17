import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")
os.system('cls')
titanic = pd.read_csv(os.path.join(assets_path,"titanic.csv"))
print(titanic)

#Q1 Given a pandas dataframe named "titanic", it contains duplicate rows and columns.
print('keep first Transpose drop duplicates: \n', titanic.T.drop_duplicates(keep='first'))
print('keep first drop duplicates: \n',titanic.drop_duplicates(keep='first'))
print('keep last drop duplicates: \n',titanic.drop_duplicates(keep='last'))
print('duplicates : \n', titanic[titanic.duplicated()])

#Q2 Return the name of person having the highest income.
incomes_data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000, 28000, 25000, 44000]
}

incomes = pd.DataFrame(incomes_data)
print(incomes)
# print('show first row of data: \n', incomes.iloc[0])
# print('show last row of data:\n',incomes.iloc[-1])
print('single line logic', incomes[incomes['income'] == incomes['income'].max()]['name'])
print('row with max income:-- ', incomes.loc[incomes['income'].idxmax()])
print('name with max income:-- ', incomes.loc[incomes['income'].idxmax()]['name'])
print('Name of person having the highest income:-- ',incomes.sort_values('income',ascending=False)['name'][0])

#Q3 population density order 
data = {
    'city': ['Alaska', 'Texas', 'California', 'New York'],
    'area': [1723337, 695662, 423967, 783000],
    'population': [700000, 26448193, 38332521, 19651127]
}

df = pd.DataFrame(data)
print('population data:\n',df)
print(df['population']/df['area'])
df['density'] = df['population']/df['area']
print(df.sort_values('density'))

#Q4 series of male name in age 23-30
data = {
    'name': ['Mark', 'Ramilla', 'Deb', 'Laxman'],
    'profession': ['dev', 'mle', 'mle', 'hr'],
    'gender': ['male', 'female', 'male', 'male'],
    'age': [21, 20, 30, 27],
    'review': ['need improvement', 'Can be improved', 'Scope of improvement', 'Great'],
    'rating': [10, 5, 7, 9]
}

df = pd.DataFrame(data)
df = df[(df['gender'] == 'male')]#filter male
print('names in age group 23 to 30:\n',df[(df['age'] >=23) & (df['age'] <=30)])

#Q6 concatenate and drop a row
out = 4
df = pd.DataFrame({
    'name':['a','b','c'],
    'age':[12,15,18]
})
data = [['d',20], ['e',21],['f',22]]
data_df = pd.DataFrame(data,columns=["name","age"])
    
# Step 2 : As mentioned in the question appending/concatenating df and data_df 
df=pd.concat([df,data_df],ignore_index=True)

# Remove the out index row 
df=df.drop(index=out)
print('after concate and drop row e:\n', df)

#Q8 merge cust and orders
df1 = pd.DataFrame({
    'cust_id': [101, 102, 103, 104],
    'name': ['rick', 'morty', 'pickle', 'jerry']})

df2 = pd.DataFrame({
    'order_id': ['OR1', 'OR3', 'OR23', 'OR42'],
    'cust_id': [102, 105, 101, 102],
    'amount': [1200, 650, 120, 989]})

print('merged data is:\n', pd.merge(df1,df2,left_on='cust_id',right_on='cust_id',how='inner'))

#Q1.5 merge
df1 = pd.DataFrame({'name': ['Jack','Ryan','Chris','Sam'],
'rank': [1, 2, 3, 4]})
df2 = pd.DataFrame({'name': ['Ryan', 'Sam', 'Chris', 'Jack'],
'rank': [3, 1, 4, 2]})

print('after merging 2 df:\n',pd.merge(df1, df2, on="name"))

# Q7. Concat and drop
df1 = pd.DataFrame({
                    'A':[1,2,3,4],
                    'B':[11,22,33,44],
                    'C':[111,222,333,444]},index=['first','second','third','fourth'])
# df1.set_index('colname',inplace=True)

df2 =pd.DataFrame({
    'D':['a','b','c','d'],
    'E':['aa','bb','cc','dd'],
    'F':['aaa','bbb','ccc','ddd']
},index=['fourth','fifth','sixth','seventh'])
# df2.set_index('colname')
df3=pd.concat([df1,df2]) 

#Block a
df4=df3.drop(["fourth"])  
print('initial df4:\n',df4)
#Block b
df4 = df3.reset_index().drop_duplicates(subset='index', keep='last')     
print(df4)     
df4 = df4.set_index('index').sort_index()

#Block c
df3.loc['fourth','A']*2

print('final :\n',df3)


df = pd.DataFrame({
    'Year':[1970,1972,1985,1988,1999,2001,2012],
    'Country':['USA','Eng','Germany','France','USA','Germany','Eng'],
    'Spending_USD':[224.840,215.110,263.930,267.430,890.770,1013.340,3114.683],
    'Life_Expectancy':[71.3,72.7,75.8,77.2,80.1,80.6,82.3]
})

year_bins = [1969,1980,1990,2000,2010,2020]
year_labels = [ '(1969, 1980]', '(1980, 1990]', '(1990, 2000]', '(2000, 2010]', '(2010, 2021]']
df['Year'] = pd.cut(df['Year'],bins=year_bins,labels=year_labels)
# result = 
result = pd.DataFrame(df.groupby('Year')['Spending_USD'].mean().round(3))
result.rename(columns={'Spending_USD':'avg_expenditure'},inplace=True)
print('final df for yearly spending:\n',result)

# Q5. Create Pivot

sales_data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'Region': ['East', 'West', 'East', 'West'],
    'Product': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
}

df = pd.DataFrame(sales_data)

pivot_table = df.pivot_table(index='Region',values='Sales',aggfunc='sum',fill_value=0)
# result = pivot_table.sort_index(axis=0).sort_index(axis=1)
# result = pd.pivot_table(df, index='Region', aggfunc='sum')
# df = pd.pivot(df,index=['Region'],columns='Sales')
print(pivot_table)