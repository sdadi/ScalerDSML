import numpy as np
import pandas as pd

#concatenation
users = pd.DataFrame({
    'userid':[1,2,3],
    'name':['satish','sudanvi','sarvika']
})
msgs = pd.DataFrame({
    'userid':[1,1,2,4],
    'msg':['hmm','ok','haha','great']
})

print('concatenating the users and msgs:\n',pd.concat([users,msgs]))#default axis=0
print('concatenating the users and msgs:\n',pd.concat([users,msgs],axis=1))

#joins
print('merge users and msgs:', users.merge(msgs)) #default inner join
print('inner join using merg and on=', users.merge(msgs,on='userid'))

print('left join of users with msgs :\n',users.merge(msgs,on='userid',how='left'))
print('right join of users and msgs:\n',users.merge(msgs,on='userid',how='right'))
print('full join of users with msgs:\n', users.merge(msgs,on='userid',how='outer'))

users.rename(columns={'userid':'uid'},inplace=True)

print('join on diff col name:\n',users.merge(msgs,left_on='uid',right_on='userid',how='left'))