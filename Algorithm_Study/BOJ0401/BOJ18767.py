import sys 
sys.stdin = open("./Algorithm_Study/BOJ0401/BOJ18767", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
  ans = []
  N = int(input())
  nA , nB, nC = map(int, input().split())
  count = {'A' : nA, 'B' : nB, 'C' : nC}
  
  subA = list(map(int,input().split()))
  subB = list(map(int,input().split()))
  subC = list(map(int,input().split()))
  mA , mB, mC = subA[0], subB[0], subC[0]
  
  graph = {'A':[],'B':[],'C':[]}
  for i in range(mA) :
    graph['A'].append(subA[i+1])
  for i in range(mB) :
    graph['B'].append(subB[i+1])
  for i in range(mC) :
    graph['C'].append(subC[i+1])
  state = {}

  Left = ['A'] * nA + ['B']*nB + ['C']*nC
  print(Left)
  stack = Left
  print(graph)
  while stack :
    lnode =stack.pop()
    print(lnode)
    print(graph)
    print(state)
    for sub in graph[lnode] :
      if sub in state.keys() :
        if len(graph[state[sub]]) <= 1 :
          continue
        graph[lnode].remove(sub)
        stack.append(state[sub])
        state[sub] = lnode
        break
      else :
        state[sub] = lnode
  print(state)



