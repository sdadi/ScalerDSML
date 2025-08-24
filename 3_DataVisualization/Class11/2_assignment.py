import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")

#Q1  impact of age and gender on the chances of survival
titanic = pd.read_csv(os.path.join(assets_path,"titanic.csv"))
males = titanic.loc[titanic['sex'] == 'male']
sns.boxplot(data=males,x='age',y='survived')
print('male data :\n',males)
female = titanic.loc[titanic['sex'] == 'female']
print('female data :\n',female)
sns.barplot(data=males,x='survived',y='age',estimator=np.mean)
plt.show()
sns.boxplot(data=titanic,x='sex',y='age',hue='survived')
plt.show()

#Q2 which advertisement source is responsible for how much of the sales  using bar plot
sid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
source = ['Website', 'Poster 4', 'Website', 'Website', 'Poster 4', 'Poster 2', 'Email', 'Website', 'Email', 'Poster 2']
prof = [143.39,230.89,118.64,72.09,98.09,230.89,180.34,146.69, 122.34, 143.39]

df = pd.DataFrame({'Sale ID': sid, 'Source': source, 'Profit':prof})
source_data = df['Source'].value_counts().index
print('source data index:',source_data)
prof_data = df['Profit'].value_counts().index
print('profit data index',prof_data)

sns.barplot(data=df,x='Source',y='Profit',estimator=np.mean)
plt.show()


#Q3 profit against selling price using lineplot
sid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
sp = [479.99, 1249.99, 649.99, 399.99, 699.99, 1249.99, 1349.99, 999.99, 649.99, 479.99, 1349.99, 1249.99, 649.99, 649.99, 999.99, 399.99, 699.99, 999.99, 399.99, 649.99] 
profit = [143.39, 230.89, 118.64, 72.09, 98.09, 230.89, 180.34, 146.69, 122.34, 143.39, 180.34, 230.89, 122.34, 118.64, 146.69, 72.09, 98.09, 146.69, 72.09, 122.34]

df = pd.DataFrame({'Sale ID':sid,'Selling Price':sp,'Profit':profit})

sns.lineplot(data=df,x='Selling Price',y='Profit',color='red')
plt.show()