import sys
sys.stdin = open("./Algorithm_Study/BOJ0415/BOJ1043","r")
input = sys.stdin.readline

N, M  = map(int, input().split())

stack = list(map(int,input().split()))
parties = []
check  = [0] * (N+1)

graph = {i : [] for i in range(1,N+1) }
for i in range(M) :
    arr = list(map(int, input().split()))
    parties.append(arr)
    for j in range(1,len(arr)) :
        for k in range(1,len(arr)) :
            if j == k :
                continue
            graph[arr[j]].append(arr[k])
stack.pop(0)
while stack :
    node = stack.pop()
    if check[node] :
        continue
    check[node] = 1
    stack.extend(graph[node])

ans = 0
for party in parties :
    flag = True
    for i in range(1,len(party)) :
        if check[party[i]] : 
            flag = False
            break
    if flag :
        ans += 1
print(ans)
