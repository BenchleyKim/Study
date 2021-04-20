import sys 
sys.stdin = open("./Algorithm_Study/BOJ0307/BOJ2263", "r")

N = sys.stdin.readline()
INORDER = list(map(int, sys.stdin.readline().split()))
POSTORDER = list(map(int, sys.stdin.readline().split()))
left = []
right = []

for i in range(N) :
  for j in range(N) :
    if POSTORDER[i] == INORDER[j] :
      