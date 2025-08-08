import numpy as np
import pandas as pd
import os as os

movies = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"movies.csv"))
directors = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"directors.csv"))
# print(movies)
# print(directors)

movies = movies.merge(directors,left_on='director_id',right_on='id',how='left')
print(movies)
#filter risky movies from our data:
# - budget is higher than avg revenue of directors other movies
def director_risk(x):
    x['risky'] = x['budget'] - x['revenue'].mean() >= 0
    return x

data_risky = movies.groupby('director_name').apply(director_risk)
print(data_risky)
print('counts of risky', data_risky['risky'].value_counts())
print('risky movies :\n',data_risky[data_risky['risky'] == True])

# find most productive director
print('most productive director: \n',movies.groupby('director_name')['title'].count().sort_values(ascending=False))
movies_agg =movies.groupby('director_name')[['year','title']].agg({'year':['min','max'],'title':'count'})
print('aggregates of the director:\n',movies_agg)
print('multi index of movies_agg:\n',movies_agg.columns)
print('show the year specific data :\n',movies_agg['year'])
print('show the year min data:\n',movies_agg['year']['min'])
print('show the year title count:\n',movies_agg['title']['count'])

movies_agg.columns = ['year_min','year_max','title_count']
print('convert multi-leve to single-level index by override the columns:\n', movies_agg)
movies_agg.reset_index(inplace=True)
print('flattened movies data:\n',movies_agg)
movies_agg['active_years'] = movies_agg['year_max'] - movies_agg['year_min']
movies_agg['avg_movies-per_year'] = movies_agg['title_count']/movies_agg['active_years']
print('average movies per year :\n',movies_agg)
print('avg movies sorted by ',movies_agg.sort_values(by='avg_movies-per_year',ascending=False,inplace=True))

