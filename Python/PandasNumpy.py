import pandas as pd
import matplotlib.pyplot as plt
from numpy import random

plt.subplot(2, 2, 1)
plt.bar(list('abcdefghjk'.upper()), [random.randint(10, 50) * 1000 for i in range(10)], color="orange")
plt.title("Salary")

plt.subplot(2, 2, 2)
plt.bar(list('abcdefghjk'.upper()), [random.randint(1, 10) * 10 for i in range(10)], color="green")
plt.title("RateLike")

plt.subplot(2, 2, 3)
plt.pie([35, 25, 25, 15], labels = ["Apples", "Bananas", "Cherries", "Dates"], explode=[0, 0, 0, 0.2])
plt.show() 

plt.suptitle("TOP-10 SALARIES")

plt.show()

# Дальше только хуже