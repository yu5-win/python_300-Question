# 241
import numpy
import os
import datetime

# print(datetime.datetime.now())

# 242
# print(type(datetime.datetime.now()))

# 243
# today = datetime.datetime.now()
# for n in range(5, 0, -1):
#     print(today-datetime.timedelta(days=n))

# 244
# print(datetime.datetime.now().strftime("%H:%M:%S"))

# 245
# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))

# 246
import time
import datetime

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

# 247


# 248
ret = os.getcwd()
print(ret, type(ret))

# 249
os.rename("C:/Users/hyunh/Desktop/before.txt",
          "C:/Users/hyunh/Desktop/after.txt")

# 250
for i in numpy.arange(0, 5, 0.1):
    print(i)
