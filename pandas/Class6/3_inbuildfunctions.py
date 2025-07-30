import numpy as np
import pandas as pd

df = pd.read_csv('..\mckinsey.csv')

print('avg/mean of life_exp: \n', df['life_exp'].mean(),df['life_exp'].min(),df['life_exp'].max())
le = df['life_exp']
print('avg/mean of life_exp: \n', le.mean(),le.min(),le.max())

print('sort values by life_exp :\n',df.sort_values(by=['life_exp']))
print('sort values by life_exp by DESC:\n',df.sort_values(by=['life_exp'],ascending=False))
print('sort values by continent, life_exp: \n', df.sort_values(by=['continent','life_exp']))

print('sort with mix of ASC, DESC: \n',df.sort_values(by=['year','life_exp'],ascending=[False,True]))

temp = df.sort_values(by=['year','life_exp'],ascending=[False,True])
# temp = temp.reset_index(drop=True,inplace=True)
print('indexes after sort: \n', temp)


#concatenation
users = pd.DataFrame({
    'userid':[1,2,3],
    'name':['satish','sudanvi','sarvika']
})
msgs = pd.DataFrame({
    'userid':[1,1,2,4],
    'msg':['hmm','ok','haha','great']
})

print('concatenating the users and msgs:\n',pd.concat([users,msgs]))