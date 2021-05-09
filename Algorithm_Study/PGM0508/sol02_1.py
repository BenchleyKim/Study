from collections import deque
import sys
def check(place) :
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    endFlag = True

    for i in range(5) :
        if not endFlag :
            break
        for j in range(5) :
            if place[i][j] == 'P' :
                for d in range(8) :
                    nx, ny = i+dx[d], j+dx[d]
                    if 0<=nx < 5 and 0<= ny < 5 :
                        if place[nx][ny] == 'P' :
                            endFlag = False
                            break
            if not endFlag :
                break

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