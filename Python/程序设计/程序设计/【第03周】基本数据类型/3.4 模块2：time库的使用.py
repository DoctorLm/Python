import time

#提供获取系统时间并格式化输出功能
print(time.time())
print(time.ctime())
print(time.gmtime())


t = time.gmtime()
t = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(t)

timeStr = '2018-01-26 12:55:20'
timeStr = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
print(timeStr)

start = time.perf_counter()
time.sleep(3)
end = time.perf_counter()
print(end - start)
