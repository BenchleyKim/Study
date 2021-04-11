import sys
sys.stdin = open("./Algorithm_Study/BOJ0409/BOJ5373", "r")
input = sys.stdin.readline

T = int(input())
# 윗면 흰색
# 아랫 면 노랑색
# 앞 면은 빨간색
# 뒷면은 오렌지색
# 왼쪽면은 초록색 
# 오른쪽 면은 파란색 

# U: 윗 면, 
# D: 아랫 면, 
# F: 앞 면, 
# B: 뒷 면, 
# L: 왼쪽 면, 
# R: 오른쪽 면
def rotation(side) :
    new_side = [[0]*3 for _ in range(3)]
    # new_side[0][0] = side[2][0]
    # new_side[0][1] = side[1][0]
    # new_side[0][2] = side[0][0]
    # new_side[1][0] = side[2][1]
    # new_side[1][1] = side[1][1]
    # new_side[1][2] = side[0][1]
    # new_side[2][0]
    for i in range(3) :
        for j in range(3) :
            new_side[i][j] = side[2-j][i]
    return new_side
def f_rotation() :
    rotation(FRONTSIDE)
    tmp = UPSIDE.pop()

    for i in range(3) :
        RIGHTSIDE[2][i], tmp[i] = tmp[i], RIGHTSIDE[2][i]
    for i in range(3) :
        DOWNSIDE[0][2-i], tmp[i] = tmp[i], DOWNSIDE[0][2-i]
    for i in range(3) :
        LEFTSIDE[2][i], tmp[i] = tmp[i], LEFTSIDE[2][i]
    UPSIDE.append(tmp)

def u_rotation() : 
    rotation(UPSIDE)
    tmp = BACKSIDE.pop()
    for i in range(3) :
        RIGHTSIDE[i][0], tmp[i] = tmp[i], RIGHTSIDE[i][0]
    for i in range(3) : 
        FRONTSIDE[0][2-i], tmp[i] = tmp[i], FRONTSIDE[0][2-i]
    for i in range(3) :
        LEFTSIDE[i][2], tmp[2-i] = tmp[2-i], LEFTSIDE[i][2]
    BACKSIDE.append(tmp)
def u_rotation() : 
    rotation(UPSIDE)
    tmp = BACKSIDE.pop()
    for i in range(3) :
        RIGHTSIDE[i][0], tmp[i] = tmp[i], RIGHTSIDE[i][0]
    for i in range(3) :
        FRONTSIDE[0][2-i], tmp[i] = tmp[i], FRONTSIDE[0][2-i]
    for i in range(3) :
        LEFTSIDE[i][2], tmp[2-i] = tmp[2-i], LEFTSIDE[i][2]
    BACKSIDE.append(tmp)
    
UPSIDE = [['w','w','w'],['w','w','w'],['w','w','w']]
DOWNSIDE = [['y','y','y'],['y','y','y'],['y','y','y']]
FRONTSIDE = [['r','r','r'],['r','r','r'],['r','r','r']]
BACKSIDE = [['o','o','o'],['o','o','o'],['o','o','o']]
LEFTSIDE = [['g','g','g'],['g','g','g'],['g','g','g']]
RIGHTSIDE = [['b','b','b'],['b','b','b'],['b','b','b']]
f_rotation()
for UP in UPSIDE:
    print(UP)
        

for _ in range(T):
    N = int(input())
    arr = list(input().split())
    print(arr)
    UPSIDE = [['w','w','w'],['w','w','w'],['w','w','w']]
    DOWNSIDE = [['y','y','y'],['y','y','y'],['y','y','y']]
    FRONTSIDE = [['r','r','r'],['r','r','r'],['r','r','r']]
    BACKSIDE = [['o','o','o'],['o','o','o'],['o','o','o']]
    LEFTSIDE = [['g','g','g'],['g','g','g'],['g','g','g']]
    RIGHTSIDE = [['b','b','b'],['b','b','b'],['b','b','b']]

