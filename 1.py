import keyword
import calendar
import datetime

print(keyword.kwlist)
print(calendar.month(2024,3))

now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)
