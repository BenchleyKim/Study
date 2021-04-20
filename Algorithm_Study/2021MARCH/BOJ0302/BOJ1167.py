
from collections import deque
import sys
input = sys.stdin.readline
sys.stdin = open("./Algorithm_Study/BOJ0302/BOJ1167", "r")

n = int(input())
graph = [[] for _ in range(n + 1)]

# 인접 리스트 만들기
for i in range(1, n + 1):
    temp = list(map(int, input().rstrip().split()))
    start = temp[0]
    k = 1
    while 1:
        to = temp[k]
        if to == -1:
            break
        cost = temp[k + 1]
        graph[start].append((cost, to))
        k += 2


def bfs(start):
    q = deque()
    q.append((0, start))
    dis = [-1] * (n + 1) # -1은 아직 방문하지 않은 곳
    dis[start] = 0
    while q:
        now_cost, v = q.popleft()
        for new_cost, to in graph[v]:
            if dis[to] == -1:  # 방문하지 않은 곳 거리값으로 수정
                dis[to] = now_cost + new_cost
                q.append((dis[to], to))
    ans = max(dis) # start로부터 최대 거리에 있는 노드와의 거리
    idx = dis.index(ans) # start로부터 최대 거리에 있는 노드 번호
    return ans, idx


ans = bfs(1)[1] # 임의의 노드에서 최대 거리에 있는 노드 v 찾기
ans = bfs(ans)[0] # v와 u사이의 거리

print(ans)

