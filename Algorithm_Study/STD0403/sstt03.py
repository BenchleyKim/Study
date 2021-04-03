import sys 
sys.stdin = open("./Algorithm_Study/STD0403/sstt03", "r")
input = sys.stdin.readline
N , K = map(int, input().split())
arr = list(map(int, input().split()))
robot_queue = [0] * N
count = 0 
state = 0
Flag = True
for i in range(N) :
    if arr[i] == 0 :
        count+=1 
        if count >= K :
            Flag = False
            print(state)
            break
while True :
    state += 1
    # print(arr)
    # print(robot_queue)
    # print(count)
    right = arr.pop()
    arr.insert(0,right)
    right = robot_queue.pop()
    robot_queue.insert(0,0)
    # 1번 과정 끝
    if not Flag:
        print(state)
        break
    if robot_queue[N-1] != 0 :
        robot_queue[N-1] = 0
    for i in range(N-2,-1,-1) :
        if robot_queue[i] != 0 and robot_queue[i+1] == 0 and arr[i+1] > 0 :
            robot_queue[i+1] = robot_queue[i]
            robot_queue[i] = 0
            arr[i+1] -= 1 
            if arr[i+1] == 0 :
                count += 1 
                if count >= K :
                    Flag = False
                    break
    if not Flag:
        print(state)
        break              
    if robot_queue[0] == 0 and arr[0] > 0 :
        robot_queue[0]= 1
        arr[0] -= 1
        if arr[0] == 0 :
            count += 1
            if count >= K :
                Flag = False
    if not Flag:
        print(state)
        break

    

        
        
