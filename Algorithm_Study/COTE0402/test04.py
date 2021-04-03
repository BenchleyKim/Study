import datetime
import time
import sys
INF = sys.maxsize
def getsecond(time) :
  rest = 0
  if int(time[:2]) >= 24 :
    rest = int(time[:2]) * 3600
    time = "00" + ''.join(time[2:])
  return int((datetime.datetime.strptime(time, "%H:%M:%S")-datetime.datetime.strptime("00:00:00", "%H:%M:%S")).total_seconds()) + rest

def solution(play_time, adv_time, logs):
  play_time = getsecond(play_time)
  adv_time = getsecond(adv_time)
  time_arr = [0]*(play_time)
  for log in logs :
    start, end = log.split('-')
    start = getsecond(start)
    end = getsecond(end)
    for i in range(start,end) :
      time_arr[i] += 1
  mx = 0
  start_point = 0
  for i in range(play_time-adv_time) :
    local_mn = len(logs)
    for j in range(i,i+adv_time) :
      local_mn = min(time_arr[j],local_mn)
    if mx < local_mn :
      mx = local_mn
      start_point = i
  answer = time.strftime('%H:%M:%S', time.gmtime(start_point))
  
  return answer

print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))