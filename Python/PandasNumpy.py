import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean, array

## https://habr.com/ru/articles/468295/
## WRITE SOLUTIONS 15 TASKS!!! 


df = pd.read_excel('./xlsx/Persons.xlsx')

xs = df['id']
xy = df['income'] // 1000

avg = df.groupby(["country"])["income"].mean().reset_index()
mx = df.groupby(["country"])["income"].max().reset_index()

incomes = avg['income'].round() // 1000
maxIncomes = mx['income'].round().tolist()
countries = avg["country"].tolist()

needs = df.loc[df.income >= mean(xy)].sort_values(by=["income"])

fig, (ac1, ac2) = plt.subplots(2, 2, figsize=(9, 7))

ax1 = ac1[0]
ax1.bar(xs, xy)
ax1.set_xlabel('Persons')
ax1.set_ylabel('Income, 1000$')
ax1.set_title('INCOMES')

ax2 = ac2[0]
ax2.barh(countries, incomes, height=0.3, color='#eb7d34')
ax2.set_xlabel('Income, 1000$')
ax2.set_ylabel('Counries')
ax2.axvline(x=mean(incomes), color='#1eb020', linestyle='--', label='Average')
ax2.text(mean(incomes) + 0.5, len(countries) - 0.5, f'Average: {mean(incomes)}', color='#1eb020')
ax2.set_title('INCOMES')


ax3 = ac1[1]
patches, texts, autotexts = ax3.pie(maxIncomes, labels=countries, explode=[0, 0, 0.15, 0, 0], autopct='%1.1f%%', startangle=90)
ax3.axis('equal')
ax3.set_title('MAX INCOME')

russiaPatchPie = patches[2]
russiaPatchPie.set_edgecolor('black')

ax4 = ac2[1]
ax4.plot([i for i in range(len(needs))], needs.income // 1000, '#9370DB', )
ax4.set_ylabel('Income, 1000$.')
ax4.set_title('≥ AVERAGE INCOME IN ORDER') 

for a in [ax1, ax2, ax4] :
    a.grid(alpha=0.5)
    a.set_axisbelow(True)
fig.suptitle('INCOME OF 2024 YEAR')

plt.subplots_adjust(hspace=0.3)
plt.show()  