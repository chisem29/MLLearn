import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import functionsActive.BinaryStep as bs

#TimeStamp

d = pd.read_excel("./xlsx/Test1.xlsx")
d.plot()
#с помощью timestamp мы можем в опр. формате получить заданную дату

print(pd.Timestamp(year=2023, month=11, day=29, hour=20, minute=52).timetuple()) 

#Period

print(pd.Period("2024", "A").to_timestamp().now())

dt = pd.DataFrame([[1, 3], [2, 6], [4, 4], [5, 6]], index=[i for i in range(1, 5)], columns=["A", "B"])

dt[["A"]] = dt[["A"]].astype(float)

dt[["A"]] = dt[["A"]].apply(lambda x : x + np.random.randint(1, 10) / 10)

dt = dt.sort_values(by=["A"])

print(dt.loc[[1]])

nn = np.array([1, 2, 3, 4, 5])

nn *= 2

print(np.linspace(0.1, 4, 9))

print(np.array([nn for i in range(3)]).trace()) # сумаа диагонали

print(np.shape([[nn for i in range(3)] for y in range(2)]))

print(np.exp([1.0, 2.0, 3.0])/sum(np.exp([1.0, 2.0, 3.0]))) # HOW????????????????? IT IS SOFTMAX

df = pd.DataFrame({
    14 : [bs.binaryStep(i) for i in np.arange(-1000, 1001)],
    88 : [1 if (i == -1000) else 0 if (i == 1000) else 0.5 for i in np.arange(-1000, 1001)],
    19 : [1 if not bs.binaryStep(i) else 0 for i in np.arange(-1000, 1001)],
    39 : [0 if (i == -1000) else 1 if (i == 1000) else 0.5 for i in np.arange(-1000, 1001)]
}) # Graphic Pashalko shhhhh!!!!

plt.show()
