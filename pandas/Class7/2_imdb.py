import numpy as np
import pandas as pd
import os as os

movies = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"movies.csv"))
directors = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"directors.csv"))

print(movies.head())
print(directors.head())

movies = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"movies.csv"),index_col=0)
directors = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"directors.csv"),index_col=0)

print('specifying index col explicitly:\n', movies.head())
movies = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"movies.csv"),index_col='id')
print('specifying id col as index_col:\n',movies.head())


print('unique directors in movies:',movies['director_id'].nunique())
print('unique directs in directors:',directors['id'].nunique())
movies = movies.merge(directors,left_on='director_id',right_on='id',how='left')
print('merged movies and directors:\n',movies.head())
# print('missing director in directors:\n',np.sum(movies[(movies['director_name'] != NaN)))
print('missing directors:', movies['director_id'].isin(directors['id']).value_counts())

# print('drop repeated cols after merge:\n',movies.drop(['director_id','id_y'],axis=1,inplace=True))

#encode gender as 0-> M and 1 -> F using apply
def encode_gender(data):
    if data == 'Male':
        return 0
    else:
        return 1
    
movies['gender'] = movies['gender'].apply(encode_gender)
print('encoded gender data:\n', movies.head())

movies['overall-summation'] = movies[['revenue','budget']].apply(np.sum,axis=1)
def profit_check(x):
    return x['revenue'] - x['budget']
movies['profit'] = movies[['revenue','budget']].apply(profit_check,axis=1)
print('suming the revenue and budge \n',movies.head())

#grouping
print('number of groups:',movies.groupby('director_name').ngroups)

print('get group:\n', movies.groupby('director_name').get_group('Christopher Nolan'))

print('find the count of movies of each direc,\n',movies.groupby('director_name')['title'].count())

print('min year and max year for every director:\n',movies.groupby('director_name')['year'].aggregate(['min','max']))
print('min year for every director:\n',movies.groupby('director_name')['year'].min())
print('max year for every director:\n',movies.groupby('director_name')['year'].max())

#Quiz 2
# print('average rating of each employee:\n',movies.groupby('emp_id')['monthly_rating'].mean())
director_budget = movies.groupby('director_name')['budget'].max().reset_index()
high_budget_dir_names = director_budget[director_budget['budget'] > 100000000]['director_name']
print('high budge director -> atleast one movie budget 100M \n', high_budget_dir_names)

print('movies data of high budget data:\n',movies[movies['director_name'].isin(high_budget_dir_names)])

#group based filtering for above  use case
print('high budget movies in single line query:\n', movies.groupby('director_name').filter(lambda x: x['budget'].max() > 100000000))