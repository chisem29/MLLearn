import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FixedFormatter, IndexLocator

## https://habr.com/ru/articles/468295/
## WRITE SOLUTIONS 15 TASKS!!! 
df = pd.DataFrame([[pd.Timestamp('10-03-16') ,774.25,776.065002,769.5,772.559998], 
                   [pd.Timestamp('10-04-16'), 776.030029,778.710022,772.890015,776.429993], 
                   [pd.Timestamp('10-05-16'), 779.309998,782.070007,775.650024,776.469971], 
                   [pd.Timestamp('10-06-16'), 779,780.47998,775.539978,776.859985], 
                   [pd.Timestamp('10-07-16'), 779.659973,779.659973,770.75,775.080017]], 
                   columns=['Date','Open','High','Low','Close'])

df['Date'] = df['Date'].dt.day
d = df.plot(linewidth=2, marker='o', figsize=[7, 4])
d.grid(which='major')

d.yaxis.set_major_locator(MultipleLocator(10))
d.xaxis.set_major_locator(IndexLocator(1, 0))
d.xaxis.set_major_formatter(FixedFormatter(df['Date']))

d.set(ylim=(750, 800))

d.set_xlabel('Days', fontdict={"size":12})
d.set_ylabel('Income', fontdict={"size":12})

d.legend(['Open','High','Low','Close'])

plt.show() 

