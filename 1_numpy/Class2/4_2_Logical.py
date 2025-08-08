import numpy as np

prices = np.array([50,45,25,20,35])
budget = 30
#check if atleast one item to purchase with budget
print('items with in budget available ',prices <= budget, np.any(prices <= budget))

print('can buy all items with budget ', prices <= budget, np.all(prices <= budget))

a = np.arange(1,13).reshape(3,4)
print('do we have any value a > 5 is: ', np.any(a>5))
print('do we have all values a > 5 is: ', np.all(a>5))

print('apply discount where price > 30: ', np.where(prices > 30, prices * 0.9, prices))


bp = np.array([120, 150, 135, 160, 175])
print('patients at high risk: ', np.where(bp > 140, 'High Risk', 'Normal'))
# print('bp with risktype: ', np.where(bp > 140, bp+' High Risk', bp+' Normal'))

temp =np.arange(1,13).reshape(3,4)
print('temps where > 7 are: ', np.where(temp > 7, 1, temp))
