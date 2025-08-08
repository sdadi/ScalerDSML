import pandas as pd

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
