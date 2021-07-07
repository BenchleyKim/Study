import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0707/BOJ3020/BOJ3020.in","r")
input = sys.stdin.readline

N , H = map(int,  input().split())
left_list = []
right_list = []
for i in range(N) :
    a = int(input())
    if i % 2 :
        right_list.append(a)
    else :
        left_list.append(a)
print(left_list)

print(right_list)
 
ll , lr = 0, H
while True :
    if ll >= lr : 
        break
    