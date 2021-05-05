

numLoc = {i :[(i-1)//3, (i-1)%3] for i in range(1,10)}
numLoc['*'] = [3,0]
numLoc[0] = [3,1]
numLoc['#'] = [3,2]
def distance(x,y) :
    return abs(numLoc[x][0] - numLoc[y][0]) + abs(numLoc[x][1] - numLoc[y][1])
def solution(numbers, hand):
    answer = ''
    left_nums = [1,4,7]
    right_nums = [3,6,9]
    left_hand = "*"
    right_hand = "#"
    for num in numbers :
        if num in left_nums :
            answer += 'L'
            left_hand = num
            continue
        if num in right_nums :
            answer += 'R'
            right_hand = num
            continue
        if distance(num, left_hand) < distance(num, right_hand) :
            answer += 'L'
            left_hand = num
            continue
        if distance(num, left_hand) > distance(num, right_hand) :
            answer += 'R'
            right_hand = num
            continue
        if distance(num, left_hand) == distance(num, right_hand) :
            if hand == 'right' :
                right_hand = num
                answer += 'R'
            else :
                left_hand = num
                answer += 'L'
    print(answer)


    return answer



solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right")
