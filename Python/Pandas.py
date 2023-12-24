import pandas as pd

#создание списка типа int[]

dt = pd.DataFrame({"A" : [1, 2, 3, 2], "B" : [1, 4, 2, 3]}, columns=["A", "B"], index=["1", "2", "3", "4"])
print(dt.sort_values(by="A"))
#DArrow
pd.Series().to_st
#TimeStamp
 
#с помощью timestamp мы можем в опр. формате получить заданную дату

print(pd.Timestamp(year=2023, month=11, day=29, hour=20, minute=52).timetuple()) 

#Period

print(pd.Period("2023", "D").to_timestamp().now())