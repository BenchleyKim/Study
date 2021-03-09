import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1676", "r")

N = int(input())
count_two = 0
count_five = 0 
for i in range(1,N+1) :
  while i % 2 == 0 :
    count_two += 1
    i //= 2
  while i % 5 == 0 :
    count_five += 1
    i //= 5

print(min(count_two,count_five))
  