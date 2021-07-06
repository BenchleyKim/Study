import sys
import heapq
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ1072/BOJ1072.in","r")
input = sys.stdin.readline

def cal_win_rate(total_game , win_game) :
    return int(win_game * 100 / total_game )


while True :
    try : X, Y = map(int, input().split())
    except : break

    current_win_rate = cal_win_rate(X,Y)
    if current_win_rate >= 99 :
        print(-1)
        continue
    left, right = 0, X + 1
    while True :
        if left >= right :
            break
        mid = (left + right)//2
        expected_win_rate = cal_win_rate(X+mid, Y+mid)
        if expected_win_rate == current_win_rate :
            left = mid + 1
            continue
        if expected_win_rate > current_win_rate :
            right  = mid
    if left == X + 1 :
        print(-1)
    else :
        print(left)

