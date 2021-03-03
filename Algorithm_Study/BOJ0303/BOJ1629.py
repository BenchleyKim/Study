import sys 
sys.stdin = open("./Algorithm_Study/BOJ0303/BOJ1629", "r")

A , B, C = map(int, sys.stdin.readline().split())
def DAC(A,B) :
  # devide 
  if B == 0 :
    return 1 % C
  if B == 1 :
    return A % C 
  if B == 2 : 
    return A**2%C
  tmp = DAC(A,B//2)
  result = tmp**2
  if B % 2 :
    result = result * A
  return result % C
print(DAC(A,B))
  
  