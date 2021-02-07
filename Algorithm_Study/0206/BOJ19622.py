
N = int(input())
meeting = []

for _ in range(N) :
    meeting.append(list(map(int,input().split())))
# N = 6
# meeting = [[10, 40, 80], [30, 60, 100], [50, 80, 70], [70, 100, 100], [90, 120, 40], [110, 140, 50]]
# meeting.sort()
arr = [0] * (N)
for idx, meet in enumerate(meeting) :
    if idx == 0 :
        arr[idx] = meet[2]
        continue
    if idx == 1:
        if meeting[idx-1][2] >= meet[2] :
            arr[idx] = arr[idx-1]
        else : 
            arr[idx] = meet[2]
        continue
    if arr[idx-1] > arr[idx-2] + meet[2] :
        arr[idx] = arr[idx-1]
    else : 
        arr[idx] = arr[idx-2] + meet[2]
    

print(arr[N-1])