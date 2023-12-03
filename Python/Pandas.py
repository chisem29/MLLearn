import pandas as pd

#создание списка типа int[]
arr = pd.array([1, 2, 3, 2, 5, "2", None, True, False, 1, 0])
print(pd.DataFrame(arr.unique()))

#DArrow

#TimeStamp

#с помощью timestamp мы можем в опр. формате получить заданную дату

print(pd.Timestamp(year=2023, month=11, day=29, hour=20, minute=52).timetuple()) 

#Period

print(pd.Period("2023", "D").to_timestamp().now())