import datetime as dt
import math

def str2time(s) :
    l = s.split()
    date = l[0].split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    time = l[1].split(":")
    hour = int(time[0])
    minute = int(time[1])
    second = int(time[2].split(".")[0])
    milsecond = int(time[2].split(".")[1])
    sustain = float(l[2].replace("s", ""))
    result = dt.datetime(year,month,day, hour, minute, second, milsecond)
    # return [year, month, day, hour, minute, second, sustain]
    return result

def string2time (s):
    ms = s.split()[2]
    s = s.replace(ms, "")
    s = s.rstrip()
    ms = float(ms.replace("s", ""))
    end = dt.datetime.strptime(s, '%Y-%m-%d %H:%M:%S.%f')
    start = end - dt.timedelta(seconds=(ms-0.001))
    inter = dt.timedelta(seconds=(ms-0.001))
    return (start, inter)

# lines =  [
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]
lines = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
s = string2time(lines[0])[0]
e = string2time(lines[-1])[0] + string2time(lines[-1])[1]
# e = string2time(lines[-1])[1]
print(s, e)
interval = (e- s) / dt.timedelta(milliseconds=1)
interval = math.ceil(interval) + 1
# print(interval)
# count = 0
# current = s
# while current < e :
#     count += 1
#     current += dt.timedelta(seconds=1)
# e = s + count * dt.timedelta(seconds=1)
# print(count)
# # arr = [0 for x in range(interval)]
# arr = [0] * count
arr = [0] * (interval)
print(arr)
for l in lines :
    start, inter = string2time(l)
    print(start, inter)
    # print(start-s ,e- end)
    # idx , jdx = round((start-s)/dt.timedelta(milliseconds=1)), round((e-end)/dt.timedelta(milliseconds=1)) +1 
    idx = (start+inter - s)/dt.timedelta(milliseconds=1)
    start = (start-s)/dt.timedelta(milliseconds=1)
    idx =int(idx)
    start = int(start)
    print(start, idx)
    for i in range(start, idx) :
        arr[i] += 1
print(arr)
print(max(arr)) 