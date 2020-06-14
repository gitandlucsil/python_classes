import time
import datetime

print(time.localtime())
print(time.asctime())
print(time.localtime())
print(time.ctime())
time1 = time.time()
time.sleep(1)
time2 = time.time()
print("Difference: ",(time2-time1))

print(datetime.date(2020, 6, 14))
print(datetime.time(14, 7, 32))