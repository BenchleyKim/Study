import sys
sys.stdin = open(".\Algorithm_Study\BOJ0525\BOJ14567","r")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {i : {} for i in range(1,N+1)}
check = [0] *(N+1)
for i in range(M) :
    A, B = map(int, input().split())
    graph[A][B] = 1 
    check[B] += 1

stack = []
for i in range(1,N+1) :
    if check[i] == 0 :
        stack.append(i)
cnt = 0 
answer = [0] * (N+1)
while stack :
    next_stack = [ ]
    cnt += 1
    for node in stack :
        answer[node] = cnt
        for sub in graph[node].keys() :
            check[sub] -= 1
            if check[sub] == 0 :
                next_stack.append(sub)
    stack = next_stack
for i in range(1,N+1) :
    print(answer[i], end=' ') 
