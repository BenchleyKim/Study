import sys 
sys.stdin = open("./Algorithm_Study/BOJ0327_study/BOJ16236", "r")
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N) :
    board.append(list(map(int, input().split())))
for b in board :
    print(b)
shark_state = 2
growth_count = shark_state
shark_location = []
fish = {i : [] for i in range(1,7)}
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 9 :
            shark_location = [i,j]
            board[i][j] = 0
        if board[i][j] != 0 :
            fish[board[i][j]].append([i,j])
print(fish[shark_state-1])
print(fish)
time = 0
while True :
    cSx, cSy = shark_location
    eatible_fish = []
    for substate in range(1, min(shark_state,7)) :
        eatible_fish.extend(fish[substate])
    if eatible_fish :
        near_fish = 0
        mn = int((20**2 + 20**2))
        # 먹을 수 있는 물고기의 동일 조건 처리 구현 ~ 
        for substate in range(1,min(shark_state,7)) : 
            for fish_idx, afish in enumerate(fish[substate]) :
                if (cSx - afish[0])**2 + (cSy-afish[1]) **2 < mn :
                    mn = (cSx - afish[0])**2 + (cSy-afish[1]) **2
                    near_fish = [fish_idx, substate]
        # 아기 상어 위치 이동

        fish_list = fish[near_fish[1]]
        time += abs(cSx - fish_list[near_fish[0]][0])
        time += abs(cSy - fish_list[near_fish[0]][1])
        shark_location = fish[near_fish[1]][near_fish[0]][:]
        print(shark_location,shark_state,time)
        fish[near_fish[1]].pop(near_fish[0])
        # 먹고 상태 카운트
        growth_count -= 1
        if growth_count == 0 :
            shark_state += 1
            growth_count = shark_state
    else : 
        break

print(time)


