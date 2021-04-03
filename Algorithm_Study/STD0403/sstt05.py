import sys 
sys.stdin = open("./Algorithm_Study/STD0403/sstt05", "r")
input = sys.stdin.readline
N = int(input())
DP = [0] * (N+1)
mx = 0 
timeline = []
for i in range(N) :
    timeline.append(list(map(int, input().split())))
for i in range(N) :
    print(DP)
    if i + timeline[i][0] >= N+1 :
        continue
    else :
        DP[i+timeline[i][0]] = max(DP[i+timeline[i][0]], DP[i]+timeline[i][1]) 
        mx = max(mx,DP[i+timeline[i][0]] )
        for j in range(i+timeline[i][0],N):
            DP[j] = max(DP[j],DP[i+timeline[i][0]])
print(mx)