import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0705/BOJ2003/BOJ2003.in","r")
input = sys.stdin.readline

N , M = map(int ,input().split())
arr = list(map(int ,input().split()))
sarr = [0]
for i in range(N) :
    sarr.append(sarr[i] + arr[i])
left , right = 0, 1 
cnt = 0
while right <= N :
    if sarr[right] - sarr[left] == M :
        cnt += 1
        if right + 1 <= N :
            if sarr[right] == sarr[right+1] :
                right += 1
                continue
        if left + 1 <= N :
            if sarr[left] == sarr[left + 1]:
                left += 1
                continue
        right += 1
        left += 1
        continue

    if sarr[right] - sarr[left] < M :
        right += 1
    else :
        left += 1

print(cnt)