import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")

os.system('cls')


data = pd.read_csv(os.path.join(assets_path,"final_vg.csv"))
#https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/021/299/original/final_vg1_-_final_vg_%281%29.csv?1670840166
print(data.head())
print('shape of the data:\n',data.shape)

# #bivariate analysis
# print('unique games available:\n', data['Name'].nunique())

# print('most popular games using value_counts():\n', data['Name'].value_counts())
# print('most popular games using group by:\n', data.groupby('Name'))
# # print('most popular games:\n', data['Name'].value_counts())

# ih = data[data['Name'] == 'Ice Hockey']
# print('get all games with Ice Hockey: \n', ih)

# # year versus NA_Sales
# sns.lineplot(data=ih,x='Year',y='NA_Sales')
# plt.title('Bivariate plot using Year wise sales for NA_Sales')
# plt.xlim(1995, 2010) # narrow down for  specific data range
# plt.xticks(range(1995,2010,3)) # how may ticks the year range in the plot
# plt.show()

# #second popular game
# bh = data.iloc[np.where(data['Name'] == 'Baseball')]
# sns.lineplot(data=bh,x='Year',y='NA_Sales')
# plt.show()

# # line plots together => plotting of multiple plots in single image
# sns.lineplot(data=ih,x='Year',y='NA_Sales',color='red', label='Ice Hockey')
# sns.lineplot(data=bh,x='Year',y='NA_Sales',color='green', label='Baseball')
# plt.legend(loc='lower left',frameon=False) # other location is upper left, upper right, lower right
# plt.show()

# # NN (numerical numerical) combination
# #scatter plot
# sns.scatterplot(data=data,x='Rank',y='Global_Sales')
# plt.title('Scatter plot')
# plt.show()

# # reversing the x and y 
# sns.scatterplot(data=data,y='Rank',x='Global_Sales')
# plt.title('Scatter plot with x and y interchanged')
# plt.show()

#CC (character character ) combination
top3pub = data['Publisher'].value_counts().iloc[:3]
print('top 3 publisher:\n',top3pub.index)
print('top 3 publisher:\n',top3pub.values)

top3gen = data['Genre'].value_counts().iloc[:3]
top3platf = data['Platform'].value_counts().iloc[:3]
print('top3 genre',top3gen.index)
print('top3 platform',top3platf.index)

# top3data = data[(data['Publisher'].isin(top3pub)) & ((data['Platform'].isin(top3platf))) & ((data['Genre'].isin(top3gen)))]
top3data = data[
    (data['Publisher'].isin(top3pub.index)) &
    (data['Platform'].isin(top3platf.index)) &
    (data['Genre'].isin(top3gen.index))
]
print('top3 publisher, genre, platform', top3data)

# sns.countplot(data=top3data,x='Publisher') #univariate 
sns.countplot(data=top3data,x='Publisher',hue='Genre') #bivariate also called Dodge bar graph
# plt.show()

#analysis on Global Sales
sns.boxplot(data=top3data,y='Global_Sales', x='Genre')
# plt.show()

#kdeplot
sns.kdeplot(data=top3data,x='Global_Sales',hue='Publisher')
# plt.show()

#each of my Publisher show avg global Sales
print('top3data publisher --indexes --',top3data['Publisher'])
print('each publisher avg ',top3data[top3data['Publisher'].values == 'Namco Bandai Games']['Global_sales'].mean())
# sns.barplot(data=top3data,x='Publisher', y='Global_Sales') #default shows mean Global Sales
sns.barplot(data=top3data,x='Publisher', y='Global_Sales',estimator=np.mean)
plt.show()
