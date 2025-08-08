import pandas as pd

data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000.0, 28000.0, 25000.0, 44000.0]
}

df = pd.DataFrame(data)
result = df.groupby('gender')['income'].mean()
print('Q1 gener-wise average income:\n',result)
print('Q1 gender-wise avg income df:\n',result.to_frame())

data = {
    'roll_no': [1, 2, 1, 3, 1, 3, 3, 3, 2, 2, 1, 2],
    'subject': ['NN', 'DL', 'ML', 'Prob', 'DL', 'ML', 'DL', 'NN', 'NN', 'Prob', 'Prob', 'ML'],
    'marks': [97, 63, 63, 71, 64, 90, 66, 46, 74, 62, 94, 67]
}

df = pd.DataFrame(data)
print('Q2 subject-wise highest marks with roll number:\n',df.groupby('subject')['marks'].max().reset_index())
max_marks = df.groupby('subject')['marks'].max().to_frame()
# max_marks = max_marks.reset_index()
print(max_marks.merge(df,on=['subject','marks'],how='inner'))

data = {
    'cust_id': [101, 102, 103, 104],
    'name': ['rick', 'morty', 'pickle', 'jerry'],
}

df = pd.DataFrame(data)
print('Q7 df.isin([101,102,120]):\n', df.isin([101,102,120]))
print('Q7 df.isin({cust_id: [101, 102]}):\n', df.isin({'cust_id': [101, 102]}))
print('Q7 df.isin(df.cust_id):\n',df.isin(df.cust_id))
# print('Q7 df.name.isin(rick)',df.name.isin('rick')) # wont' work

