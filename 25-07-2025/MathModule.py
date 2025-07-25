import math

print(math.sqrt(16))
print(math.pow(2,3))
print(math.pi)

import datetime as d

today = d.date.today()
print("Today's date is: ",today)

now = d.datetime.now()
print("Current time is: ",now.strftime("%H:%M:%S"))