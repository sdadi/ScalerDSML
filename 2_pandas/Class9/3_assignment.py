import numpy as np
import pandas as pd
import os as os

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")
movies = pd.read_csv(os.path.join(assets_path,"movies1.csv"))
directors = pd.read_csv(os.path.join(assets_path,"directors1.csv"))
data = movies.merge(directors,left_on='director_id',right_on='id',how='inner')
os.system('cls')

# Q1. Number of Years
print('How many years of data in movies dataset: ',movies['year'].nunique())

# Q2. DMY Snippet
print('DMY snippte:\n',movies['day']+'-'+movies['month']+'-'+movies['year'].astype('str'))

# Q3. Male percentage
print('Q4. Movies Direction --- ',directors['gender'].value_counts(normalize=True)*100)

print('Q5. Movies - How many different directors have directed a movie since 2010 (inclusive)?', movies[movies['year'] >= 2010]['director_id'].nunique())

print('Q7 -------------')
print('Q7 using query',data.query("title == 'Spider-Man 3'").get('director_name'))
print('Q7 using loc',data.loc[data["title"] == "Spider-Man 3", "director_name"])
print('Q7 using value_counts',data[data["title"] == "Spider-Man 3"]["director_name"].value_counts())
print('Q7 using iloc',directors[directors['id'] == data[data['title'] == 'Spider-Man 3']['director_id'].iloc[0]]['director_name'])

print('Q8 james cameron between 2005 and 2010', data[(data['director_name'] == 'James Cameron') & (data['year'] >= 2005) & (data['year'] <= 2010)])

# Q9. Vote Average
top10popular = data.sort_values(by='popularity',ascending=False).head(10)
print('Among the top 10 most popular movies, which movie has the 2nd highest vote_average:\n',top10popular.sort_values(by='vote_average',ascending=False).head(2).iloc[1]['title'])


# Top 10 popular amont Top 10 Rated
top10rated = data.sort_values(by='vote_average',ascending=False).head(10)
print('top 10 popular movies are also among top 10 rated (vote_avg):\n',top10popular.merge(top10rated,on='title')['title'])

# print('revenue per budge',data['revenue']/data['budget'])

print(' year did Christopher Nolan produce the most number of movies',data[data['director_name'] == 'Christopher Nolan']['year'].unique())

bins = [1950,1960,1970,1980,1990,2000,2010,2020]
labels = ['1950-60','1960-70','1970-80','1980-90','1990-2000','2000-10','2010-20']
data['decade'] = pd.cut(movies['year'],bins=bins,labels=labels)
# print(data['decade'].value_counts())
print('decade most movies were made',data['decade'].value_counts().index[0])

decade_most_movies = data['decade'].value_counts().index[0]
print('decade with most movies',decade_most_movies)
decade_dir_counts = data[data['decade'] == decade_most_movies].groupby(['director_name']).size().reset_index(name='movie_count')
# decade_dir_counts = data[data['decade'] == decade_most_movies]['director_name'].value_counts().head(10)
# topdirectoer = data.sort_values(by='decade',ascending=False)['director_name'].value_counts()
# print('top director in each decade:\n',decade_dir_counts.loc[decade_dir_counts.groupby('decade')['movie_count'].idxmax()])
# print('---- :\n',decade_dir_counts.sort_values('movie_count',ascending=False))
print('director coutns:\n',data[data['decade'] == decade_most_movies]['director_name'].value_counts())

def get_decade(year):
    return (year//10)*10
data['decade'] = data['year'].apply(get_decade)
decade_most_movies = data['decade'].value_counts().index[0]
print('decade ',data[data['decade'] == decade_most_movies]['director_name'].value_counts().head(10))
print('decade list',data['director_name'].value_counts().head())

# years = data['year'].value_counts()
# print('years movies produced are more than 70:\n',years[years >= 70].index)
