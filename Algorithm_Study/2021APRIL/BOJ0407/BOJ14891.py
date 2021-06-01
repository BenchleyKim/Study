import sys
sys.stdin = open("./Algorithm_Study/BOJ0407/BOJ14891", "r")

gears = []
gears.append(list(map(int, input())))
gears.append(list(map(int, input())))
gears.append(list(map(int, input())))
gears.append(list(map(int, input())))

# N극은 0, S극은 1이다. 2하고 6번 째 원소가 물리는 톱니 
K = int(input())
for _ in range(K) :
    check = [0] * 4
    # 톱니바퀴 번호 , 방향
    n , d = map(int, input().split())
    # 1이면 시계방향 -1 이면 반시계 방향
    n  -= 1 
    check[n] = d
    left = n
    while n-1 >= 0 :
        if gears[n][6] == gears[n-1][2] : 
            break
        check[n-1] = -(check[n])
        n -= 1
    n = left
    while n+1 <= 3 :
        if gears[n][2] == gears[n+1][6] :
            break
        check[n+1] = -(check[n])
        n += 1
    for i in range(4) :
        if check[i] == 1 :
            gears[i].insert(0, gears[i].pop())
        if check[i] == -1 :
            gears[i].append(gears[i].pop(0))
ans = 0

if gears[0][0] == 1 :
    ans += 1
if gears[1][0] == 1 :
    ans += 2
if gears[2][0] == 1 :
    ans += 4
if gears[3][0] == 1 :
    ans += 8
print(ans)


    
