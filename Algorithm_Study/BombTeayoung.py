# 문제
# 시험을 망친 태영이가 인하대학교에 폭탄을 던진다!

# 인하대학교는 N×N 크기의 정사각형 모양의 땅이다. 인하대학교의 모든 땅은 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타내며, r은 가장 위에서부터 떨어진 칸의 개수, c는 가장 왼쪽으로부터 떨어진 칸의 개수이다. r과 c는 0부터 시작한다.

# 초기에 인하대학교의 모든 칸은 해발 고도 0미터이다. 하지만 태영이가 폭탄을 던지면 폭발 범위내에 있는 모든 칸의 해발 고도는 1미터씩 줄어들고 폭탄은 그 자리에 남게 된다. 태영이가 던지는 폭탄의 폭발 범위는 폭탄이 던져진 칸을 중심으로 한 M×M 크기의 정사각형 범위이다. M은 홀수이며 폭발 범위의 윗변은 인하대학교의 윗변과 평행하다. 태영이는 폭탄의 폭발 범위가 인하대학교를 넘어가게 던지지 않는다.

# 태영이가 던진 폭탄들은 한 번만 터지는 것이 아니라 3일 뒤에 한 번 더 터지도록 설계되어있다. 태영이가 폭탄을 던져 모든 폭탄이 첫 번째 폭발을 마무리했을 때의 인하대학교의 해발고도가 주어진다. 각 칸의 해발고도는 H[r][c]이다. 우리가 할 일은 3일 뒤 폭탄이 한 번 더 터지기 전에 모든 칸에 각각 폭탄이 몇 개 있는지 찾아주는 것이다.

# 입력
# 양의 정수 N과 M이 공백을 사이에 두고 주어진다.

# N개의 줄에 걸쳐 H배열의 값이 주어진다. r번째 줄의 c번째 값은 H[r][c]이다.

def bombExplore(x, y):
    X_min, X_max = x - m , x + m 
    y_min, y_max = y - m , y + m
    if X_min <= 0 : X_min = 0
    if X_max > n : X_max = n -1 
    if y_min <= 0 : y_min = 0
    if y_max > n : y_max = n -1 
    for i in range(X_min, X_max+1):
        for j in range(y_min, y_max+1):
            h[i][j] += 1

n, m = list(map(int, input().split()))
m = m//2

h = []
for i in range(n):

    h.append(list(map(int, input().split())))

answer = [[0 for x in range(n)] for x in range(n)]

for x in range(m,n-m) :
    for y in range(m,n-m):
        k = -h[x-m][y-m]
        answer[x][y] = k
        for i in range(k):
            bombExplore(x,y)

for i in answer:
    print(i)

# 출력
# N개의 줄에 각각 N개의 정수를 출력한다.

# r번째 줄의 c번째 값은 (r, c)에 존재하는 폭탄의 수이다.

# 제한
# 1 ≤ M​ ≤ N ≤ 2,000 (M은 홀수)
# -2,147,483,648 ≤ H[r][c] ≤ 0
# 예제 입력 1 
# 5 3
# -2 -2 -4 -2 -2
# -2 -2 -4 -2 -2
# -2 -2 -4 -2 -2
# 0 0 0 0 0
# 0 0 0 0 0
# 예제 출력 1 
# 0 0 0 0 0
# 0 2 0 2 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 예제 입력 2 
# 5 3
# -8 -17 -26 -18 -9
# -9 -29 -47 -38 -18
# -10 -38 -62 -52 -24
# -2 -21 -36 -34 -15
# -1 -9 -15 -14 -6
# 예제 출력 2 
# 0 0 0 0 0
# 0 8 9 9 0
# 0 1 11 9 0
# 0 1 8 6 0
# 0 0 0 0 0
# 예제 입력 3 
# 10 3
# -8 -17 -26 -19 -21 -21 -21 -18 -9 -8
# -14 -36 -56 -43 -40 -39 -42 -36 -17 -13
# -20 -50 -70 -53 -46 -54 -60 -59 -31 -22
# -22 -48 -70 -55 -48 -48 -53 -48 -26 -14
# -18 -33 -52 -50 -60 -66 -68 -64 -39 -21
# -17 -31 -63 -62 -69 -53 -51 -45 -29 -15
# -13 -31 -59 -71 -75 -66 -53 -54 -35 -23
# -12 -37 -60 -65 -53 -49 -38 -43 -24 -18
# -7 -25 -35 -43 -38 -47 -37 -39 -20 -15
# -1 -10 -13 -13 -9 -19 -21 -23 -10 -7
# 예제 출력 3 
# 0 0 0 0 0 0 0 0 0 0
# 0 8 9 9 1 11 9 1 8 0
# 0 6 13 11 0 8 10 3 5 0
# 0 6 8 0 2 4 9 5 9 0
# 0 10 5 11 5 7 3 4 0 0
# 0 2 2 8 9 14 13 9 12 0
# 0 5 7 13 2 0 0 1 3 0
# 0 6 9 7 14 8 6 2 8 0
# 0 1 9 3 1 5 13 3 7 0
# 0 0 0 0 0 0 0 0 0 0


