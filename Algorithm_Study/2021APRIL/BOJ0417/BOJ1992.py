import sys
sys.stdin = open("./Algorithm_Study/BOJ0417/BOJ1992","r")
input = sys.stdin.readline


N = int(input())
board = []
for i in range(N) :
    board.append(list(input().rstrip()))

def dac(x,y,n) :
    if n == 1 :
        if board[x][y] =='1' :
            print(1,end='')
            return
        if board[x][y] == '0' :
            print(0,end='')
            return
    else :
        flag = 0
        criteria = board[x][y]
        for i in range(x,x+n) :
            for j in range(y,y+n) :
                if board[i][j] == criteria :
                    continue
                else :
                    flag = 1
                    break
            if flag :
                break
        if flag :
            print('(',end='')
            n //= 2
            dac(x,y,n)
            dac(x,y+n,n)
            dac(x+n, y , n)
            dac(x+n,y+n,n)
            print(')',end='')
        else :
            print(criteria,end='')

dac(0,0,N)

        
