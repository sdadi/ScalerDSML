import numpy as np
import pandas as pd
import os as os
import matplotlib.pyplot as plt
import seaborn as sns

assets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "assets")
data = pd.read_csv(os.path.join(assets_path,"titanic_big.csv"))
#https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/021/299/original/final_vg1_-_final_vg_%281%29.csv?1670840166
os.system('cls')
print('highesh mean fare:\n',data.groupby('embark_town')['fare'].mean())
exit()
sns.boxplot(data=data,x='alone',y='age',hue='survived')
plt.show()

# Q2 telco customers churning
telco = pd.read_csv(os.path.join(assets_path,"telco_customer_churning.csv"))
print(telco)
plt.figure(figsize=(9,6))
plt.subplot(1,2,1)
sns.boxplot(data=telco,x='PaymentMethod',y='MonthlyCharges',hue='Churn')
plt.subplot(1,2,2)
sns.boxplot(data=telco,x='Contract',y='MonthlyCharges',hue='Churn')
plt.show()
