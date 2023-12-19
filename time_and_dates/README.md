# How to datetime

## The purpose
...  
Bruk ISO-8601.

## How does it work?
...  

## Useful commands
Dates:
datetime.datetime is generally preferable over date, since date does not support timezones.  
```
import datetime
date1 = datetime.date(2021, 5, 12)  # Type datetime.date, printed as "2021-05-12"
date2 = date1 + datetime.timedelta(days=5)  # Type datetime.date, printed as "2021-05-17"
date3 = datetime.date.today()  # Type datetime.date 
```
Datetimes:
```
import datetime
dt1 = datetime.datetime(2021, 5, 21, 12, 0, 0)  # Type datetime.datetime, printed as "2021-05-21 12:00:00"
dt2 = dt1 + datetime.timedelta(days=1, seconds=30, minutes=10, hours=1)  # Type datetime.datetime, printed as "2021-05-22 13:10:30
dt3 = datetime.datetime.now()  # Type datetime.datetime, printed as "2023-10-06 14:41:07.285696"
```
To and from strings
```
dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
date = dt.date()  # After using strp to create a datetime.datetime object 
dt_str = datetime.datetime.strftime(dt_obj, '%Y-%m-%d %H:%M:%S')
```

When working with data which is should be convertable to text, during storage or 
```
dt = datetime(2023, 11, 22, 12, 20, 00)
assert dt == datetime.fromisoformat(dt.isoformat())
```
You may also (de)serialize to JSON.


## Useful links
[Description](https://www.cisco.com)  
[strftime.org specification](https://strftime.org)  


