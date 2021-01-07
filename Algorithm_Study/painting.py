test_case = int(input())
for i in range(test_case):
    box_num =  int(input())
    for j in range(box_num) : 
        box_info = input().split
        box_info = [int(k) for k in box_info]
        box = 

        
def box_info2grid(box_info ):
    lx, ly = box_info[0], box_info[1]
    rx, ry = box_info[2], box_info[3]
    color = box_info[4]
    create_box(lx,ly,rx,ry,color)
    grid[]



def create_box(lx,ly,rx,ry,color):
    grid = [[0 for col in range(rx)] for row in range(ry)]
    grid[lx:rx, ly:ry] = color
    print(grid)
    return grid 
