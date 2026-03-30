from datetime import date

my_date = date(2026, 1, 6)
print(my_date)

print(my_date.day)
print(my_date.month)
print(my_date.year)

print(my_date.isocalendar())

from datetime import time

my_time = time(21, 59)
print(my_time)

print(my_time.hour)
print(my_time.minute)
print(my_time.second)


from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(current_time)