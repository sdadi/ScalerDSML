import numpy as np
import pandas as pd
import os as os

movies = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"movies.csv"))
directors = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"directors.csv"))
movies = movies.merge(directors,left_on='director_id',right_on='id',how='inner')
print(movies.head())

#Question 1: What is the total span of years covered by the movies dataset
print('min and max year from dataset', (movies['year'].max()- movies['year'].min()))

#Question 2: select correct snippet that gives release date in Day, Month , Year format
movies['release_date'] = movies['day'] +'-'+movies['month']+'-'+ movies['year'].astype('str')
print('Thursday-Dec-2009 format data:\n', movies['release_date'])

#Question 3: percentage of male directors
print('all count, male count:', len(movies), len(movies[movies['gender'] == 'Male']), len(movies[movies['gender'] == 'Female']))
print('perncentage using mask -> includes null value rows:\n', (len(movies[movies['gender'] == 'Male'])/len(movies)))
print('percentage of male directors - considers non-null values:\n',movies['gender'].value_counts(normalize=True)*100)

# Question 4:how many different movies directed in the year 2010
print('movies in 2010:', len(movies[movies['year'] == 2010]), movies[movies['year'] == 2010]['title'].nunique(), sum(movies['year']==2010))

# Question 5: how many directors since 2010(inclusive)
print('directors since 2010 inclusive:', (movies[movies['year'] >= 2010]['director_id'].nunique()))

# Question 7: display the name of the director Spider-Man 3 movies
print('director of Spider-Man 3 movie is:\n', movies[movies['title'] == 'Spider-Man 3']['director_name'])

#Question 8: how many movies directed by James Cameron betwee 2005 and 2010
print('James cameron movies count between 2005 - 2010:\n', movies[(movies['year'] >= 2005) & (movies['year'] <= 2010) & (movies['director_name'] == 'James Cameron')])
def solve(director_name, start_year, end_year):
    movies_name = []
    result = movies[(movies['year'] >= start_year) & (movies['year'] <= end_year) & (movies['director_name'] == director_name)]
    movies_name.append((director_name,result))
    return movies_name

print('for specific director:\n', solve('Gore Verbinski', 2005, 2010))

# Question 9: amont top 10 most popular movies, which is 2nd hight vote_avg
top10_popular = movies.sort_values(by=['popularity'],ascending=False).head(10)
print('top 10 popular movies, 2nd hightst vote_avg:\n', top10_popular.sort_values(by='vote_average',ascending=False).head(2).iloc[1]['title'])

# Question 10: how many movies of top 10 popular in top 10 rated
top10_rated = movies.sort_values(by='vote_average',ascending=False).head(10)
print(top10_popular.merge(top10_rated,how='inner',on='title'))

# Question 10: which year did Christopher Nolan produced most number of movies?
print('Christopher Nolan most number of movies year:\n', movies[movies['director_name'] == 'Christopher Nolan']['year'].value_counts())
print('christopher most movies in year:\n', movies[movies['director_name'] == 'Christopher Nolan'].groupby('year')['title'].count())

#for every director?
print('every director count:\n', movies.groupby(['director_name','year'])['title'].count().sort_values(ascending=False))

# Question 11: which decade most movies are produced?

bins = [1950,1960,1970,1980,1990,2000,2010,2020]
labels = ['1','2','3','4','5','6','7']
movies['year_bucket'] = pd.cut(movies['year'],bins=bins,labels=labels)
print('decadge with most movies:\n',movies['year_bucket'].value_counts().index[0])

# within decade most number of movies, top 5 contributing directors


# display movies of only those yeares where number of movies produced more than 70