#ex1
from datetime import date, timedelta

datetime = date.today() - timedelta(5)
print('Today :',date.today())
print('5 days before:',datetime)

#ex2
from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#ex3

from datetime import datetime

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)

#ex4
from datetime import datetime
date1_input = input()
date2_input = input()
date1 = datetime.strptime(date1_input)
date2 = datetime.strptime(date2_input)

time_difference = date2 - date1
difference_in_seconds = time_difference.total_seconds()

print("Difference between two dates in seconds:", difference_in_seconds)

