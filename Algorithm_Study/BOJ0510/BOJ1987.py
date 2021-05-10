import sys
import string
sys.stdin = open(".\Algorithm_Study\BOJ0510\BOJ1987","r")
input = sys.stdin.readline

R, C = map(int , input().split())
board = []
for r in range(R) :
    board.append(list(input().rstrip()))
alpha =list(string.ascii_uppercase)
print(alpha)
for b in board :
    print(b)
alpha = {i : 0 for i in alpha}
stack = [(0,0,0)]
check = [[0]*C for _ in range(R)]

def dfs(x,y, check) :
    if check[cx][cy] : 
        continue
while stack :
    cx,cy, dist = stack.pop()
    ca = board[cx][cy]
    if check[cx][cy] : 
        alpha[ca] = 0
        continue
    if alpha[ca] :
        continue
    check[cx][cy] = 1 
    alpha[ca] = 1 
