import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"final_vg.csv"))
#https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/021/299/original/final_vg1_-_final_vg_%281%29.csv?1670840166
print(data.head())
print(len(data),data.size)

x_val = [0,1,2,3,4,5]
y_val = [2,5,4,6,5,9]

plt.plot(x_val,y_val)
# plt.show() #basic graph display without details

plt.title('profit over time')
plt.xlabel('time')
plt.ylabel('profit in Cr')
# plt.show() #shows graph with labels for x,y axis and title

print('genre from the data is ', data['Genre'].unique())
print('count of Genre',data['Genre'].nunique())
print('value counts for each Gener',data['Genre'].value_counts())

#line chart using graphs
x_val = data['Genre'].value_counts().index
y_val = data['Genre'].value_counts().values
# plt.plot(x_val,y_val)
# plt.show()

#bar chart
# plt.bar(x_val,y_val)
plt.title('genre vs count')
plt.xlabel('genre')
plt.ylabel('count')
# plt.show()

#how to provide more customization
plt.figure(figsize=(10,5))
plt.bar(x_val,y_val)
plt.title('genre vs count')
plt.xlabel('genre')
plt.ylabel('count')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
# plt.show()


#seaborn
plt.figure(figsize=(8,5))
plt.title('sea born title1 genre vs counts')
names = data['Genre'].value_counts().index
names = names.sort_values()
print('sorted names:',names)
# sns.countplot(data=data,x='Genre',order=data['Genre'].value_counts().index)
sns.countplot(data=data,x='Genre',order=names)
# plt.show()

print('uniuqe years', data['Year'].nunique())
plt.title('year count plot')
sns.countplot(data=data,x='Year',order=data['Year'].sort_values())
#too big x-axis chart
# plt.show()

#when lot of unique values, use Histogram instead of Barplot
print('min and max years', data['Year'].min(), data['Year'].max())

plt.hist(data['Year'],bins=15)
plt.title('histogram of Year count with bins 15')
plt.xlabel('Year')
plt.ylabel('Count')
plt.figure(figsize=(10,5))
# plt.show()

# kde(kernel density estimation) or (density) plot which is a continuous probability density curve
# smoothened version of histogram
sns.kdeplot(data['Year'])
# plt.show()

# box-plot or 5-point summary of numerical data
print('describe Global_Sales column data:',data['Global_Sales'].describe())
sns.boxplot(data=data,y='Global_Sales')
plt.show()