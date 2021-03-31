import sys 
sys.stdin = open("./Algorithm_Study/BOJ0331/BOJ15997", "r")
input = sys.stdin.readline

country = {i : 0 for i in list( input().split())}
log = []
for i in range(6) :
  # A국가, B국가, A가 이길확률 : W , 비길확률 : D, 질 확률 : L 
  A,B,W,D,L = input().split()
  W, D, L = float(W), float(D), float(L)
  log.append([A,B,W,D,L])
score = [(0,3),(1,1),(3,0)]
total_prob = {i : 0 for i in country.keys()}
stack = [(0,0,0)]
def solution(prob, sb, count) :
  if prob == 0 :
    return
  if count == 6 :
    first, second,third,fourth = sorted(sb.items(),key=lambda x:x[1], reverse=True)
  
    if sb[first[0]] == sb[second[0]] == sb[third[0]] == sb[fourth[0]]:
      for i in sb.keys() :
        total_prob[i] += prob*0.5 
      return
    if sb[first[0]] == sb[second[0]] == sb[third[0]] :
      total_prob[first[0]] += prob*(2/3)
      total_prob[second[0]] += prob*(2/3)
      total_prob[third[0]] += prob*(2/3)
      return
    if sb[fourth[0]] == sb[second[0]] == sb[third[0]] :
      total_prob[first[0]] += prob
      total_prob[fourth[0]] += prob*(1/3)
      total_prob[second[0]] += prob*(1/3)
      total_prob[third[0]] += prob*(1/3)
      return
    if sb[third[0]] == sb[second[0]] :
      total_prob[first[0]] += prob
      total_prob[third[0]] += prob*0.5
      total_prob[second[0]] += prob*0.5
      return
    total_prob[first[0]] += prob
    total_prob[second[0]] += prob
    return
  A,B,W,D,L = log[count]
  count += 1
  # A가 이길 떄 
  sb[A] += 3
  solution(prob*W,sb,count)
  sb[A] -= 3
  # A와 B가 무승부일때
  sb[A] += 1
  sb[B] += 1
  solution(prob*D,sb,count) 
  sb[A] -= 1
  sb[B] -= 1
  # B가 이길 때
  sb[B] += 3 
  solution(prob*L,sb,count) 
  sb[B] -= 3 


solution(1,country,0)
for i in total_prob.keys() :
  print(total_prob[i])
