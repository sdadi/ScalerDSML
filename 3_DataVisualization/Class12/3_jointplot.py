import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")
data = pd.read_csv(os.path.join(assets_path,"final_vg.csv"))
#https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/021/299/original/final_vg1_-_final_vg_%281%29.csv?1670840166
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
print('input data for all top3 Publisher, Genre and Platform:\n',top3data)

sns.jointplot(data=top3data,x='NA_Sales',y='EU_Sales',hue='Genre',kind='scatter')
plt.title('Joint plot between NA_Sales and EU_Sales')
# sns.jointplot(data=top3data,x='NA_Sales',y='EU_Sales',hue='Genre',kind='hex')
plt.show()

x = np.random.randn(10000,2)
print('shape of x:', x.shape)

print('scatter plot of x[:,0] and x[:,1]\n',x[:,1])
plt.title('scatter plot of x[:,0] and x[:,1]')
plt.scatter(x[:,0],x[:,1])
plt.show()

plt.title('joint plot of x[:,0] and x[:,1]')
sns.jointplot(x=x[:,0],y=x[:,1])
plt.title('joint plot of x[:,0] and x[:,1] of kind hex')
sns.jointplot(x=x[:,0],y=x[:,1],kind='hex')
plt.show()