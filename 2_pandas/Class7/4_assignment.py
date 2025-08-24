import pandas as pd
import os as os

os.system('cls')
# Q2 gender wise average income
data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000.0, 28000.0, 25000.0, 44000.0]
}

df = pd.DataFrame(data)
print('gender wise average income:\n',df.groupby('gender')['income'].mean())

# Q3 subject wise hightes marks with roll number
data = {
    'roll_no': [1, 2, 1, 3, 1, 3, 3, 3, 2, 2, 1, 2],
    'subject': ['NN', 'DL', 'ML', 'Prob', 'DL', 'ML', 'DL', 'NN', 'NN', 'Prob', 'Prob', 'ML'],
    'marks': [97, 63, 63, 71, 64, 90, 66, 46, 74, 62, 94, 67]
}

df = pd.DataFrame(data)
max_marks = df.groupby('subject')['marks'].max()
max_marks = max_marks.reset_index() # reset index to make subject a column
print('max_marks after reset index:\n',max_marks)
print('subject wise highest marks with roll number using max_marks with merge:\n',pd.merge(df,max_marks,on=['subject','marks'],how='inner'))
print('subject wise highest marks with roll number:\n',df.loc[df.groupby('subject')['marks'].idxmax()])

data = pd.DataFrame({'name':["Ram","Shyam","Mukesh","Suresh"],'age':[10,18,60,50]})
print(data)
def age_category(x):
    if x < 18:
        return 'kid'
    elif x >=18 and x <=50:
        return 'adult'
    else:
        return 'senior'
data['age'] = data['age'].apply(age_category)
print(data)



data = {
    'name': ['Luffy', 'Chopper', 'Zoro', 'Sanji'],
    'marks': [15, 89, 33, 32]
}

df = pd.DataFrame(data)
print('marks greater than or equal to constant:\n',df[df['marks'] >= 33]['name'])
