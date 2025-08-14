import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv(os.path.join(os.path.dirname(os.getcwd()),"final_vg.csv"))
#https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/021/299/original/final_vg1_-_final_vg_%281%29.csv?1670840166
# clear_console()
os.system('cls')

top3pub = data['Publisher'].value_counts().iloc[:3]
top3gen = data['Genre'].value_counts().iloc[:3]
top3platf = data['Platform'].value_counts().iloc[:3]

top3data = data[
    (data['Publisher'].isin(top3pub.index)) &
    (data['Platform'].isin(top3platf.index)) &
    (data['Genre'].isin(top3gen.index))
]

sns.scatterplot(data=top3data,x='NA_Sales',y='EU_Sales')
plt.show()

#bifurcate(heu) based on publisher
# sns.scatterplot(data=top3data,x='NA_Sales',y='EU_Sales')
sns.scatterplot(data=top3data,x='NA_Sales',y='EU_Sales',hue='Publisher')
plt.show()

#bifurcate(heu) based on Genre
# sns.scatterplot(data=top3data,x='NA_Sales',y='EU_Sales')
sns.scatterplot(data=top3data,x='NA_Sales',y='EU_Sales',hue='Genre')
plt.show()

# sns.boxplot(data=top3data,y='Global_Sales')
# sns.boxplot(data=top3data,y='Global_Sales',hue='Genre')
sns.boxplot(data=top3data,y='Global_Sales',hue='Publisher')
plt.show()

#multi variate plots
sns.boxplot(data=top3data,y='Global_Sales',x='Publisher',hue='Genre')
plt.show()

#average Global Sales from each Publisher
sns.barplot(data=top3data,x='Publisher',y='Global_Sales')
plt.show()

#average Global sales of each Publisher and Genre
sns.barplot(data=top3data,x='Publisher',y='Global_Sales',hue='Genre')
plt.show()

sns.scatterplot(data=top3data,x='NA_Sales',y='EU_Sales',hue='Rank',size='Rank')
plt.show()