input_t = int(input())
input_list = []
for i in range(input_t):
    input_k, input_n, input_m = map(int, input().split())
    station_list = input().split()
    station_list = [int(i) for i in station_list]
    input_list.append([input_k, input_n, input_m, station_list])

def nextStation(current_location, max_move, station_list):
    max_go = 0
    for i in range(current_location+1,current_location+max_move+1):
        
        if i in station_list:
            max_go = i
            
            
    return max_go
def moveCount(lst):
    max_move, last_station, station_num, station_list = lst
    current_location = 0 
    moveCount = 0 
    while current_location + max_move < last_station :
        current_location = nextStation(current_location, max_move, station_list)
        if current_location == 0 :
            moveCount = 0
            break
        
        moveCount += 1 
    return moveCount


for i in range(input_t):
    # print(input_list[i])
    print("#%d %d"%(i+1, moveCount(input_list[i])))