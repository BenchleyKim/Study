# puzzle = []
# for i in range(9):
#   puzzle.append(list(map(int, input().split())))
# print(puzzle)
puzzle = [[0, 3, 5, 4, 6, 9, 2, 7, 8], [7, 8, 2, 1, 0, 5, 6, 0, 9], [0, 6, 0, 2, 7, 8, 1, 3, 5], [3, 2, 1, 0, 4, 6, 8, 9, 7], [8, 0, 4, 9, 1, 3, 5, 0, 
6], [5, 9, 6, 8, 2, 0, 4, 1, 3], [9, 1, 7, 6, 5, 2, 0, 8, 0], [6, 0, 3, 7, 0, 1, 9, 5, 2], [2, 5, 8, 3, 9, 4, 7, 6, 0]]

queue = []
nodes = []
for i in range(9) : 
  for j in range(9) :
    if puzzle[i][j] == 0 :
      nodes.append([i,j])

visited = [0] * len(nodes)
queue.append(nodes[0])
while len(queue) == 0 :
  node = queue.pop(0)
  if 
