import sys
sys.stdin = open("./Algorithm_Study/BOJ0405/BOJ14500", "r")
input = sys.stdin.readline


N, M = map(int, input().split())
paper = []
paper.append([0] * (M+6))
paper.append([0] * (M+6))
paper.append([0] * (M+6))

for i in range(N) :
    paper.append([0,0,0] + list(map(int, input().split())) + [0,0,0])
paper.append([0] * (M+6))
paper.append([0] * (M+6))
paper.append([0] * (M+6))


def mino_case(x,y) :
    mx = 0 
    # 1 자형의 경우 
    mx = max(mx , paper[x][y] + paper[x][y+1]+ paper[x][y+2]+ paper[x][y+3])
    mx = max(mx , paper[x][y] + paper[x][y-1]+ paper[x][y-2]+ paper[x][y-3])
    mx = max(mx , paper[x][y] + paper[x+1][y]+ paper[x+2][y]+ paper[x+3][y])
    mx = max(mx , paper[x][y] + paper[x-1][y]+ paper[x-2][y]+ paper[x-3][y])
    # ㅁ 의 경우
    mx = max(mx, paper[x][y] + paper[x+1][y] + paper[x+1][y+1] + paper[x][y+1] )
    # ㄱ 의 경우
    mx = max(mx, paper[x][y] + paper[x][y+1] + paper[x-1][y] + paper[x-2][y])
    mx = max(mx, paper[x][y] + paper[x+1][y] + paper[x][y+1] + paper[x][y+2])
    mx = max(mx, paper[x][y] + paper[x][y-1] + paper[x+1][y] + paper[x+2][y])
    mx = max(mx, paper[x][y] + paper[x-1][y] + paper[x][y-1] + paper[x][y-2])
    # ㄴ 의 경우
    mx = max(mx, paper[x][y] + paper[x][y-1] + paper[x-1][y] + paper[x-2][y])
    mx = max(mx, paper[x][y] + paper[x-1][y] + paper[x][y+1] + paper[x][y+2])
    mx = max(mx, paper[x][y] + paper[x][y+1] + paper[x+1][y] + paper[x+2][y])
    mx = max(mx, paper[x][y] + paper[x+1][y] + paper[x][y-1] + paper[x][y-2])
    # ㄹ 의 경우
    mx = max(mx, paper[x][y] + paper[x-1][y] + paper[x-1][y-1] + paper[x-2][y-1])
    mx = max(mx, paper[x][y] + paper[x][y+1] + paper[x-1][y+1] + paper[x-1][y+2])
    mx = max(mx, paper[x][y] + paper[x+1][y] + paper[x+1][y+1] + paper[x+2][y+1])
    mx = max(mx, paper[x][y] + paper[x][y-1] + paper[x+1][y-1] + paper[x+1][y-2])
    # 5 의 경우
    mx = max(mx, paper[x][y] + paper[x-1][y] + paper[x-1][y+1] + paper[x-2][y+1])
    mx = max(mx, paper[x][y] + paper[x][y+1] + paper[x+1][y+1] + paper[x+1][y+2])
    mx = max(mx, paper[x][y] + paper[x+1][y] + paper[x+1][y-1] + paper[x+2][y-1])
    mx = max(mx, paper[x][y] + paper[x][y-1] + paper[x-1][y-1] + paper[x-1][y-2])
    # ㅗ 의 경우 
    mx = max(mx, paper[x][y] + paper[x-1][y] + paper[x-1][y-1] + paper[x-1][y+1])
    mx = max(mx, paper[x][y] + paper[x][y+1] + paper[x-1][y+1] + paper[x+1][y+1])
    mx = max(mx, paper[x][y] + paper[x+1][y] + paper[x+1][y-1] + paper[x+1][y+1])
    mx = max(mx, paper[x][y] + paper[x][y-1] + paper[x-1][y-1] + paper[x+1][y-1])
    return mx


tmp = 0 
for i in range(3, N+3) :
    for j in range(3, M+3) : 
        tmp = max(tmp , mino_case(i,j))
print(tmp)
