# https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python

# A general rule. 
# Ask the user for his local time and timezone.
# Always convert to UTC, store and do all processing in it, then convert to local time upon presentation.
# Remember - A "Z" in the timestamp means Zulu (UTC). 

import datetime
import pytz

# print(pytz.all_timezones) # "Europe/Oslo" is one of them

print("datetime (tz naive) ")
dt_naive = datetime.datetime.now()  # Naive
print(dt_naive.isoformat())  # ISO 8601 format
print(dt_naive.tzinfo)
print("")

timezone_oslo = pytz.timezone("Europe/Oslo")  # Define a timezone
timezone_utc = pytz.timezone("UTC")  # Define a timezone

print("datetime (tz aware)")
dt_aware = datetime.datetime.now(tz=timezone_oslo)  # Aware - alternative 1 from scratch
print(dt_aware.isoformat(), dt_aware.tzinfo)
dt_aware = timezone_oslo.localize(dt_naive)  # Aware - alternative 2 from naive datetime. aware = localize(naive)
print(dt_aware.isoformat(), dt_aware.tzinfo)
print("")

print("Oslo --> UTC --> Oslo")  # Same point in time, but converted to another timezone
time_now_oslo = datetime.datetime.now(tz=timezone_oslo)
print(time_now_oslo.isoformat())
time_now_utc = time_now_oslo.astimezone(timezone_utc)  # aware = astimezone(aware)
print(time_now_utc.isoformat())
time_now_utc = time_now_utc.astimezone(timezone_oslo)
print(time_now_oslo.isoformat())
print("")

print("These are the same:")
print(time_now_utc == time_now_oslo)  # Compare
print(time_now_utc - time_now_oslo)  # Diff
print("")

print("That was fun.")




