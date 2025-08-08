import numpy as np
import pandas as pd

# https://colab.research.google.com/drive/18brilAKh6Z_1JRoj0QAMkcF43wn4Uuox?usp=sharing#scrollTo=pj3F7wi6P95h

df = pd.read_csv('..\mckinsey.csv')
print('# of rows in df: ',len(df))
print('last row data is :',df.iloc[-1])
df.loc[len(df)] = ['India', 2024, 140,'Asia',70,700]
print('add a new row at last',len(df), '\n', df.iloc[-1])

df.iloc[len(df)-1] = ['India', 2025, 140,'Asia',70,750]
print('updates row if index exists with iloc',len(df), '\n', df.iloc[-1])

#adding duplicate rows

df.loc[len(df)] = ['India', 2024, 140,'Asia',70,700]
df.loc[len(df)] = ['India', 2024, 140,'Asia',70,700]
df.loc[len(df)] = ['India', 2024, 140,'Asia',70,700]


print('see the duplciate rows using tail: ',df.tail(5))
print('see the duplciate rows using iloc: ',df.iloc[-1,-5])

#drop the duplicate rows
print('df after remove the duplicate rows by their index:',df.drop([1705,1706,1707]))
# print('df remove duplicate rows: ',df.duplicated())
print('show the duplicate rows only using df.duplicated():', df[df.duplicated()])
# print('remove duplicates using df.drop_duplicates: ', df.drop_duplicates())
# print('remove duplicates using df.drop_duplicates: ', df.drop_duplicates(keep='False',inplace=True))# first, last, False default:first

# df.loc[df.last_valid_index()+1] = ['India', 2026, 140,'Asia',70,800]
# print('new row index after drop duplicates(keep=false)',df.tail(5))

#question
data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
        'C': ['small', 'large', 'large', 'small', 'small', 'large', 'large', 'small'],
        'D': [1, 2, 2, 3, 3, 4, 5, 6]
        }

temp = pd.DataFrame(data)

print('duplicate count in dataset from the above question is: ',sum(temp.duplicated(subset=['A', 'B'])))