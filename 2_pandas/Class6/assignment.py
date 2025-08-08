import numpy as np
import pandas as pd
import os as os

titanic = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"titanic.csv"))
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