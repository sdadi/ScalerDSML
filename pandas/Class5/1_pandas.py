import pandas as pd

df = pd.read_csv('..\mckinsey.csv') #df is a variable of type dataframe
# print(df) # prints entire table data of CSV file
print(type(df)) #<class 'pandas.core.frame.DataFrame'> is similar to a Table with Rows, Columns or 2D matrix

# Columns are also called as Features/Attributes/Series
# Rows also called as Data Point/Records/Observations/Measures

print(type(df['country']))  #type is <class 'pandas.core.series.Series'> Series is similar to 1D array
# Collection of Series is a Data Frame

#top 5 rows
print(df.head()) # top 5 rows by default
print(df.head(3))

#bottom rows
print('last or bottom 5 default: ',df.tail())
print(df.tail(3))

# 
print('of rows and columns?: is ',df.shape)

#basic operation on columns

#add new column
print('columns in dataframe using columns: ',df.columns)
print('columns in dataframe using keys(): ',df.keys())

#access a single column
print('single column accessing: ', df['country'])
print('show only 3 rows of country column:', df['country'].head(3))

#access multiple columns
print('access multiple columns :',df[['country','life_exp']].head(2))

print('unique countries in the entire file: ', df['country'].unique())
print('count of unique countries: ',len(df['country'].unique()))
print('numbr of unique countries using nunique: ', df['country'].nunique())

print('frequency of each country: default is DESC order',df['country'].value_counts())
print('alternative way of accessing column directly by colname: ', df.country)# not recommended due to spacing in col name, reserved keywords,

# update the column name
print('rename the column name using .rename(): ', df.rename(columns={'country':'Country','population':'Population'},inplace=False))
# df = df.rename(columns={'country':'Country','population':'Population'}) # to replace actual data or use df.rename(inplace:true)
print('after renaming column: ',df)
print('change the col name using axis: ', df.rename({'population':'Population'},axis=1))

#delete a column
print('delete a column continent',df.drop(columns=['continent'],axis=1))# use ,inplace=True for original change

#create a new column
df['validTill'] = df['year']+7
df['gdp'] = df['gdp_cap']*df['population']
print('adding valid till year for 7 years: ', df)
df['new_col'] = None
df['Own'] = [i for i in range(len(df))]
print('adding empty column: ', df)
df.drop(columns=['gdp','validTill','new_col','Own'],inplace=True)
print('dropping new columns: ', df)


print('Given a dataframe consisting of 5 cols to drop 3rd column from start is:', df.drop(df.columns[-3],axis=1))

#basic operations on rows
df.index = list(range(1,df.shape[0]+1))
print('overwrite the indexes starting with 1', df)

#explicit(user defined => visible to us) and implicit(internal => 0 based) indexes
# Indexing uses column name, Slicing uses rows

#string indices
sample = df.head()


sample.index = ['a','b','c','d','e']
print('str indices of sample', sample)

print('iloc[-1] should return ',df.iloc[[-1,-2]])

print('multiple indexes at same time using df.iloc[[0,3,1,1]]', df.iloc[[0,3,1,1]])

temp = df.set_index('country')
print('country set as index: ',temp)
print('only data of Afganistan using df.loc[Afganistan]', temp.loc['Afghanistan'])
# temp.loc['Afghanistan'] is same as df.loc[df['country']=='Afghanistan']

print('temp.iloc[3] for custm indexing column as country', temp.iloc[3])

