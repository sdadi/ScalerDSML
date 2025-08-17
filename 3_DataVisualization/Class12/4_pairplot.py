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

# sns.countplot(data=top3data,x='Genre',hue='Publisher')
# plt.show()

# sns.countplot(data=top3data,x='Genre',hue='Platform')
# plt.show()

#pair wise comparison works for numeric only
# sns.pairplot(data=top3data)
# plt.show()

data_corr = top3data.corr(numeric_only=True)
print('data correlation:\n',data_corr)

plt.colormaps()
sns.heatmap(data=data_corr,annot=True,cmap='BuGn_r')
plt.show()