import pandas as pd

#создание списка типа int[]

dt = pd.DataFrame({"A" : [1, 2, 3], "B" : [1, 2, 3]}, index=["row1", "row2"])

print(dt[dt["A"]>2])
#DArrow

#TimeStamp
 
#с помощью timestamp мы можем в опр. формате получить заданную дату

print(pd.Timestamp(year=2023, month=11, day=29, hour=20, minute=52).timetuple()) 

#Period

print(pd.Period("2023", "D").to_timestamp().now())