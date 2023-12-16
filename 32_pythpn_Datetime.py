import datetime as dt

x = dt.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%a"))

# creating the date objects - you can use datetime() for creating the date
import datetime

x = datetime.datetime(2022, 5, 16)
print(x)
