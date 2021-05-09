

def distance(x, y, nx,ny) :
    ans = abs(abs(x-nx) + abs(y-ny))
    return ans

def solution(maps, p, r):
    # p 공격력 , r은 범위 
    empty_line = [100] * (r+len(maps))
    board = []
    for i in range(r//2) :
        board.append(empty_line)
    for m in maps :
        board.append([100]*(r//2) + m + [100]*(r//2))
    for i in range(r//2) :
        board.append(empty_line)
    # for b in board :
    #     print(b)
    answer = 0
    for i in range(len(maps)) :
        for j in range(len(maps)) :
            count = 0
            mi , mj = i+r//2-0.5, j+r//2-0.5
            # print()
            # print(mi,mj)
            # print()
            for ri in range(i, i+r) :
                for rj in range(j,j+r) :
                    # print(ri,rj,distance(mi, mj, ri, rj) )
                    # ri += 0
                    # rj += 0.5 
                    if distance(mi, mj, ri, rj) == (r//2) :
                        if board[ri][rj] <= p/2 :
                            count += 1
                        continue
                    if distance(mi, mj, ri, rj) < (r//2) :
                        if board[ri][rj] <= p :
                            count += 1
                        continue

            answer = max(answer,count)
    return answer

print(solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],	19,	6))
print(solution([[47, 8, 99, 9, 85, 3, 8], [90, 93, 8, 25, 98, 15, 97], [9, 95, 91, 87, 8, 81, 9], [98, 88, 82, 89, 79, 81, 97], [97, 35, 31, 97, 81, 2, 92], [32, 16, 49, 9, 91, 89, 17], [53, 6, 35, 12, 13, 98, 5]],	78,	6))