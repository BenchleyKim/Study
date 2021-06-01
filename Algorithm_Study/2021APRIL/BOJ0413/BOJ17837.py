import sys
sys.stdin = open("./Algorithm_Study/BOJ0413/BOJ17837","r")
input = sys.stdin.readline
 
N , K = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))
class token() :
    def __init__(self,R,C,D) :
        self.R = R
        self.C = C
        self.D = D
        self.uplist = []
    def move(self,nx,ny) :
        self.R, self.C = nx,ny
        for utoken in self.uplist :
            utoken.R , utoken.C = nx,ny
    def reverse(self) :
        self.uplist = list(reversed(self.uplist))
        for idx in range(1,len(self.uplist)+1) :
            self.uplist[idx-1].uplist = self.uplist[idx:] 
    
tokenList = []
check = [[0]*N for _ in range(N)]
for i in range(K) :
    R, C, D = map(int, input().split())
    R -= 1
    C -= 1
    D -= 1
    check[R][C] = i+1
    tokenList.append(token(R,C,D))

print(tokenList)
dx = [0,0,-1,1]
dy = [1,-1,0,0]
endFlag = False
count = 0
while True :
    if count > 1000  :
        count = -1
        break
    if endFlag :
        break
    count += 1
    for idx, ntoken in enumerate(tokenList) :
        x, y, d= ntoken.R, ntoken.C, ntoken.D 
        nx, ny = x+dx[d], y+dy[d]
        blue_flag = False
        if 0<= nx < N and 0<= ny < N :
            if board[nx][ny] == 0 :
                check[x][y] = 0
                ntoken.move(nx,ny)
                if check[R][C] != 0 :
                    tokenList[check[R][C]-1].uplist.append(ntoken)
                    tokenList[check[R][C]-1].uplist.extend(ntoken.uplist)
                else :
                    check[nx][ny] = idx+1
            elif board[nx][ny] == 1 :
                ntoken.move(nx,ny)
                if check[R][C] != 0 :
                    ntoken.reverse()
                    tokenList[check[R][C]-1].uplist.extend(ntoken.uplist)
                    tokenList[check[R][C]-1].uplist.append(ntoken)
                    pass
                else :
                    ntoken.reverse()
            else :
                blue_flag = True
            if len(tokenList[check[R][C]-1].uplist) >= 4 :
                endFlag = True 
                break

        else :
            blue_flag = True

        if blue_flag :
            if d == 0 :
                ntoken.D = 1
            if d == 1 :
                ntoken.D = 0
            if d == 2 :
                ntoken.D = 3
            if d == 3 :
                ntoken.D = 2
            nx, ny = x+dx[d], y+dy[d]
            if 0<= nx < N and 0<= ny < N :
                if board[nx][ny] == 0 :
                    check[x][y] = 0
                    ntoken.move(nx,ny)
                    if check[R][C] != 0 :
                        tokenList[check[R][C]-1].uplist.append(ntoken)
                        tokenList[check[R][C]-1].uplist.extend(ntoken.uplist)
                    else :
                        check[nx][ny] = idx+1
                elif board[nx][ny] == 1 :
                    if check[R][C] != 0 :
                        ntoken.reverse()
                        tokenList[check[R][C]-1].uplist.extend(ntoken.uplist)
                        tokenList[check[R][C]-1].uplist.append(ntoken)
                        pass
                    else :
                        ntoken.move(nx,ny)
                        ntoken.reverse()
                else :
                    continue
            else :
                continue


print(count)


