import datetime

date1 = datetime.date(2021, 5, 12)  # Type datetime.date, printed as "2021-05-12"
date2 = date1 + datetime.timedelta(days=5)  # Type datetime.date, printed as "2021-05-17"
date3 = datetime.date.today()  # Type datetime.date 
for date in [date1, date2, date3]:
    print(type(date), date)

dt1 = datetime.datetime(2021, 5, 21, 12, 0, 0)  # Type datetime.datetime, printed as "2021-05-21 12:00:00"
dt2 = dt1 + datetime.timedelta(days=1, seconds=30, minutes=10, hours=1)  # Type datetime.datetime, printed as "2021-05-22 13:10:30
dt3 = datetime.datetime.now()  # Type datetime.datetime, printed as "2023-10-06 14:41:07.285696"
for dt in [dt1, dt2, dt3]:
    print(type(dt), dt)

print("That was fun!")
