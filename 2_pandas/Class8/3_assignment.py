import numpy as np
import pandas as pd

data = pd.DataFrame({
    'Student ID':[1,1,1,2,2,2],
    'Subject':['Mathematics','Physics','Chemistry','Mathematics','Physics','Chemistry'],
    'Score':[85,78,92,72,80,88]
})
print(data)
data_melt = pd.melt(data,id_vars=['Student ID'],var_name='Subject',value_name='Score')
print('melt data of students:\n',data_melt)