from collections import deque
import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ2842/BOJ2842.in","r")
input = sys.stdin.readline

# 입력 
N = int(input())
board =[]
for i in range(N) :
    board.append(list(input().rstrip()))
height_board = []
for i in range(N) :
    height_board.append(list(map(int, input().split())))

# 변수 선언
dx = [-1, 1, 0, 0 , -1 , -1, 1, 1]
dy = [0,0, -1, 1 , -1 , 1 , -1 ,1]
home_candidate_set = set()
total_candidate_set = set()
K_list = []
p = []
for i in range(N) :
    for j in range(N) :
        h = height_board[i][j]
        if board[i][j] == 'P' :
            p = [i,j]
            home_candidate_set.add(h)
        if board[i][j] == 'K' :
            K_list.append((i,j))
            home_candidate_set.add(h)
        total_candidate_set.add(h)
def isSuccessTrue(l, r) :
    dq = deque()
    dq.append(p)
    check = [[0] * N for _ in range(N)] 
    while dq :
        x, y = dq.popleft()
        if check[x][y] :
            continue
        check[x][y] = 1
        for d in range(8) :
            nx, ny = x + dx[d] , y + dy[d]
            if 0<= nx < N and 0<= ny < N :
                h = height_board[nx][ny] 
                if l <= h <= r :
                    dq.append((nx,ny))
    for x, y in K_list :
        if check[x][y] == 0 :
            return False
    return True
home_candidate_list = list(sorted(home_candidate_set))
total_candidate_list = list(sorted(total_candidate_set))


l_mn = min(total_candidate_list)
l_mx = min(home_candidate_list)
r_mn = max(home_candidate_list)
r_mx = max(total_candidate_list)

left_candidate = []
right_candidate = []
for candi in total_candidate_list :
    if l_mn <= candi <= l_mx :
        left_candidate.append(candi)
    if r_mn <= candi <= r_mx :
        right_candidate.append(candi)

mn_answer = 1_000_000
l_idx ,r_idx = 0,0
while l_idx < len(left_candidate) and r_idx < len(right_candidate) :
    suc_l , suc_r = False, False 
    if isSuccessTrue(left_candidate[l_idx], right_candidate[r_idx]) :
        mn_answer = min(mn_answer , right_candidate[r_idx] - left_candidate[l_idx] )
        l_idx += 1
        suc_l = True
    else :
        if suc_l and suc_r :
            l_idx += 1
            r_idx += 1
        else :
            r_idx += 1


print(mn_answer)