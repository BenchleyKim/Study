# n , m = list(map(int, input().split()))
# castle = []
# for _ in range(n):
#   castle.append(input())
# row = []
# col = []
# for i in range(n):
#   row.append("X" not in castle[i])
# for j in range(m) :
#   col.append("X" not in [castle[i][j] for i in range(n)])
# print(row)
# print(col)
# print(max(sum(row),sum(col)))

n, m = map(int, input().split(' '))

arr = []

for _ in range(n):
    arr.append(input())

row = [0] * n
col = [0] * m

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count, col_count = 0, 0

for i in row:
    if i == 0:
        row_count += 1

for i in col:
    if i == 0:
        col_count += 1

print(max(row_count,col_count))

# check_row = [0] * m
# check_line = [0] * n
# for i in range(n) : 
#   row = list(input().split())
#   for j, r in enumerate(row) : 
#     if r=='X' :
#       check_row[j] = 1
#       check_line[i] = 1
#     # print(r)
# mr = check_row.count(0)
# ml = check_line.count(0)
# if mr >= ml :
#   print(mr)
# else :
#   print(ml)


# 2 2
# X X 
# X X
      
# 4 5 
# . . . X .
# . . X . . 
# . . . . .
# . . . . .

# 6 7
# X . . . . . X
# . . . . X . .
# . . . . . . .
# . . . . . . .
# . X . . . . .
# . . . . . . X
      
