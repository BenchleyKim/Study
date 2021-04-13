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
        self.uplist = reversed(self.uplist)
        for idx in range(len(self.uplist)-1) :
            self.uplist[idx] = self.uplist[idx:] 
    

for i in range(K) :
    R, C, D = map(int, input().split())