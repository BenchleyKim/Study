import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ2407", "r")

N , M = map(int, input().split())

def factorial(N,idx) :
  sum = 1
  while idx >= 1 :
    sum *= N 
    N -= 1
    idx -= 1
  return sum

print(factorial(N,M)//factorial(M,M))
