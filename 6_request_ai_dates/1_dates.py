from datetime import datetime, timedelta, timezone

now = datetime.now()
print(type(now), now, sep=" | ") # <class 'datetime.datetime'> | 2025-12-12 08:58:25.726936

specific_date = datetime(2025, 12, 12, 0, 0, 1)
print(specific_date) # 2025-12-12 00:00:01

# ? Format dates
format_date = now.strftime("%d/%m/%Y")
print(format_date) # 12/12/2025

# ? Operations
yesterday = datetime.now() - timedelta(days=1)
print(yesterday) # 2025-12-11 09:09:07.481883
tomorrow = datetime.now() + timedelta(days=1)
print(tomorrow) # 2025-12-13 09:09:07.498213
noon_yesterday = datetime.now() - timedelta(days=0.5)
print(noon_yesterday) # 2025-12-11 21:10:10.011145

year = now.year
print(year) # 2025

date1 = datetime.now()
date2 = datetime(2025, 5, 15)
diff = date2 - date1
print(type(diff), diff, sep=" | ") # <class 'datetime.timedelta'> | -212 days, 14:44:36.976278
