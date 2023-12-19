import datetime
import time

print("datetime.date")
date1 = datetime.date(2021, 5, 12)  # Type datetime.date, printed as "2021-05-12"
date2 = date1 + datetime.timedelta(days=5)  # Type datetime.date, printed as "2021-05-17"
date3 = datetime.date.today()  # Type datetime.date 
for date in [date1, date2, date3]:
    print(type(date), date)

print("datetime.datetime")
dt1 = datetime.datetime(2021, 5, 21, 12, 0, 0)  # Type datetime.datetime, printed as "2021-05-21 12:00:00"
dt2 = dt1 + datetime.timedelta(days=1, seconds=30, minutes=10, hours=1)  # Type datetime.datetime, printed as "2021-05-22 13:10:30
dt3 = datetime.datetime.now()  # Type datetime.datetime, printed as "2023-10-06 14:41:07.285696"
for dt in [dt1, dt2, dt3]:
    print(type(dt), dt)

print("\nTo and from timestamps (can also be used on datetime.date)")
dt4 = datetime.datetime.now()
time.sleep(1)
dt5 = datetime.datetime.now()
print(dt4, dt4.timestamp(), datetime.datetime.fromtimestamp(dt4.timestamp()))
print(dt5, dt5.timestamp(), datetime.datetime.fromtimestamp(int(dt5.timestamp())))


print("\nTimedelta")
dt6 = datetime.datetime.now()
td = datetime.timedelta(weeks=1, days=0, hours=0, minutes=0, seconds=0, milliseconds=0)
print(f"Now: {dt6}")
print(f"A week from now: {dt6 + td}")


print("That was fun!")
