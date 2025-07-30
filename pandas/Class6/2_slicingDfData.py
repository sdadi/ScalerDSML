import numpy as np
import pandas as pd

# https://colab.research.google.com/drive/18brilAKh6Z_1JRoj0QAMkcF43wn4Uuox?usp=sharing#scrollTo=pj3F7wi6P95h

df = pd.read_csv('..\mckinsey.csv')

print('iloc and loc are same initially', [df.loc[1],df.iloc[1]])

print('view first 3 rows with 2 columns like works with iloc only df.iloc[0:4,1:3] \n',df.iloc[0:4,1:3])
print('view first 3 rows with 2 columns with loc df.loc[0:4,[col1:col5]]', df.loc[0:4,['year','continent']])
print('view first 3 rows with 2 columns with loc df.loc[0:4,"year":"continent"]\n', df.loc[0:4,'year':'continent'])
print('view with stepsize using iloc df.iloc[0:4:2,1:4]:\n',df.iloc[0:4:2,1:4])

print('homework ', df.loc[0:4,'year':'continent':2])