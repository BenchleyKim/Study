import sys 

def solution(n,passenger, train) :
  graph = {i : [] for i in range(1,n+1)}
  for v in train :
    s, e =v 
    graph[s].append(e)
    graph[e].append(s)
  start = 1
  stack = []
  for i in graph[start] :
    stack.append([start, i])
  check = [0] * (n+1)
  check[start] = passenger[start-1]
  mx = 0 
  end_station = start
  while stack :
    parent, child = stack.pop()
    if check[child] :
      continue
    check[child] = check[parent] + passenger[child-1]
    mx = max(mx, check[child])
    if mx <= check[child] :
      mx = check[child] 
      end_station = max(end_station, child)

    for i in graph[child] :
      stack.append([child,i])
  return [end_station, mx]

print(solution(6,	[1,1,1,1,1,1],[[1,2],[1,3],[1,4],[3,5],[3,6]] ))
print(solution(4,	[2,1,2,2],[[1,2],[1,3],[2,4]]))
print(solution(5,[1,1,2,3,4],[[1,2],[1,3],[1,4],[1,5]]))
    