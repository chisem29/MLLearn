import pandas as pd
import numpy as np

#создание списка типа int[]

#DArrow

#TimeStamp
 
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

print(np.array([nn for i in range(3)]).trace()) # сумаа диагонали

print([1,2,3, 0, 0, 0][:3]+[2, 5, 6][:3])