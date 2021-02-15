import sys 
sys.stdin = open("./Algorithm_Study/0215/2798", "r")
N , M = list(map(int, input().split()))
cards = list(map(int, input().split()))
result = 0
min = cards[1] + cards[2] + cards[0]
for i in range(N) :
  for j in range(N-1):
    for k in range(N-2) :
      sum = cards[i] + cards[j] + cards[k]
      if sum < M :  
        diff = M-sum
        if diff < min : 
          min = diff
          result = sum
print(result)