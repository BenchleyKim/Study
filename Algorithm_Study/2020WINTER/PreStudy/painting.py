def box_info2grid(box_info ):
    lx, ly = box_info[0], box_info[1]
    rx, ry = box_info[2], box_info[3]
    color = box_info[4]
    grid = create_box(lx,ly,rx,ry,color)
    



def create_box(lx,ly,rx,ry,color):
    grid = [[0 for col in range(rx)] for row in range(ry)]
    grid[lx:rx][ly:ry] = color
    print(grid)
    return grid 


test_case = int(input())
answer_list = []
for i in range(test_case):
    box_num =  int(input())
    box_list = []
    for j in range(box_num) : 
        box_info = input().split()
        box_info = [int(k) for k in box_info]
        box = box_info2grid(box_info)
        box_list.append(box)
    for box in box_list:
        print(box)

        

