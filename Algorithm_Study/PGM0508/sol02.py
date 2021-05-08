from collections import deque
import sys
def check(place) :
    INF = sys.maxsize
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check_bool = True
    print(place)
    for i in range(5) :
        if not check_bool :
            break
        for j in range(5) :
            if not check_bool :
                break
            if place[i][j] == 'P' :
                stack = []
                check = [[0]*5 for _ in range(5)]
                check[i][j] = 1
                for cd in range(4) :
                    cx, cy = i + dx[cd], j + dy[cd]
                    if 0 <= cx < 5 and 0<= cy < 5 :
                        if place[cx][cy] == 'X' :
                            continue
                        stack.append((cx,cy, 1)) 
                while stack :
                    cx, cy, dist = stack.pop()
                    if dist > 2 :
                        continue
                    if place[cx][cy] == 'P' :
                        
                        check_bool = False
                        print(cx,cy, i,j)
                        break
                    if check[cx][cy]  :
                        continue
                    check[cx][cy] = dist
                    for d in range(4) :
                        nx, ny = cx+dx[d], cy+dy[d]
                        if 0<= nx < 5 and 0<= ny < 5 :
                            if place[nx][ny] == 'X' :
                                continue
                            stack.append((nx,ny,check[cx][cy]+1))
    return check_bool




def solution(places):
    answer = []
    for place in places :
        if check(place) :
            answer.append(1)
        else :
            answer.append(0)
    
    
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))