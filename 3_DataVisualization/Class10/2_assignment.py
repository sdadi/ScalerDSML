import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

# assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")

os.system('cls')

# Q1  countplot() of the 'Source' column
typ = ['Desktop', 'Laptop', 'Tablet', 'Desktop', 'Desktop', 'Desktop', 'Desktop', 'Desktop', 'Laptop', 'Laptop', 'Tablet', 'Tablet', 'Laptop', 'Laptop', 'Tablet', 'Laptop', 'Laptop', 'Tablet', 'Tablet', 'Desktop']
src = ['Poster 1', 'Poster 4', 'Poster 4', 'Email', 'Poster 4', 'Poster 2', 'Poster 1', 'Poster 3', 'Poster 4', 'Poster 4', 'Poster 3', 'Poster 3', 'Website', 'Poster 3', 'Poster 2', 'Poster 1', 'Website', 'Website', 'Poster 1', 'Poster 3']
df = pd.DataFrame({'Product Type': typ, 'Source': src})
# sns.countplot(data=df,x='Source')
# plt.show()

# Q2 Interpret the number of cereals for different amounts of protein available in any cereal using a bar graph
protein_list = [4, 3, 4, 4, 2, 2, 2, 3, 2, 3, 1, 6, 1, 3, 1, 2, 2, 1, 1, 3, 3, 2, 2, 2, 2, 1, 3, 3, 3, 1, 2, 1, 3, 3, 3, 1, 3, 1, 2, 3, 2, 4, 2, 4, 4, 4, 3, 2, 2, 3, 3, 3, 3, 3, 1, 2, 4, 5, 3, 3, 2, 1, 2, 2, 3, 3, 2, 6, 2, 2, 3, 3, 2, 1, 3, 3, 2]
print(len(protein_list))
x,y = np.unique(protein_list,return_counts=True)
# print(np.unique(protein_list,return_counts=True))
plt.xlabel('Protein amount in grams')
plt.ylabel('Number of cereals')
plt.title('Protein comparison')
bars = plt.bar(x,y,color='g')
plt.show()

# Q3 KDE by Year
saleid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sp = [479.99, 1249.99, 649.99, 399.99, 699.99, 1249.99, 1349.99, 999.99, 649.99, 479.99, 1349.99, 1249.99, 649.99, 649.99, 999.99, 399.99, 699.99, 999.99, 399.99, 649.99]
year = [2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2019, 2019, 2019, 2019, 2019]
df = pd.DataFrame({'Sale ID':saleid,'Selling Price':sp,'Year':year})
sns.kdeplot(data=df,x='Year',color='red')
plt.show()

# Q4. Correct interpretation
