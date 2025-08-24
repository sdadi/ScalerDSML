import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")
data = pd.read_csv(os.path.join(assets_path,"final_vg.csv"))
#https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/021/299/original/final_vg1_-_final_vg_%281%29.csv?1670840166
# clear_console()
os.system('cls')

top3pub = data['Publisher'].value_counts().iloc[:3]
top3gen = data['Genre'].value_counts().iloc[:3]
top3platf = data['Platform'].value_counts().iloc[:3]
print('top3 genre',top3gen.index)
print('top3 platform',top3platf.index)

top3data = data[
    (data['Publisher'].isin(top3pub.index)) &
    (data['Platform'].isin(top3platf.index)) &
    (data['Genre'].isin(top3gen.index))
]

#sub plots
plt.figure(figsize=(9,6))
plt.subplot(2,3,1)
sns.scatterplot(data=top3data,x='NA_Sales',y='EU_Sales', color='red')
plt.subplot(2,3,3)
sns.scatterplot(data=top3data,x='NA_Sales',y='Other_Sales', color='blue')
plt.subplot(2,3,4)
sns.scatterplot(data=top3data,x='NA_Sales',y='Global_Sales', color='green')
plt.subplot(2,3,6)
sns.scatterplot(data=top3data,x='NA_Sales',y='JP_Sales')
plt.subplot(1,3,2)
sns.countplot(data=top3data,x='Publisher', hue='Genre')
plt.xticks(rotation=45)
plt.show()