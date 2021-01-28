


n , k , s = list(map(int, input().split())) 
adj = {}
for x in range(1,n+1):
    adj[x] = []
for _ in range(k):
    v, e = list(map(int, input().split())) 
    
    adj[v] += [e]
    adj[e] += [v]


checkList = [False] * n
stack = []
def dfs(root):
    checkList[root-1] = True
    print(root, end = ' ')
    adj[root].sort()
    for i in adj[root]:
        if not checkList[i-1] :
            dfs(i)
    
dfs(s)
print()
# adj = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}

queue = []
checkList = [False] * n
def bfs(root) :
    queue.append(root)
    checkList[root - 1] = True
    print(root, end=' ')
    while True :
        if len(queue) == 0 :
            return 0
        parent = queue.pop(0)
        checkList[parent-1] = True
        children = adj[parent]
        children.sort()
        for child in children :
            if not checkList[child-1] :
                checkList[child-1] = True
                queue.append(child)
                print(child, end=' ')

bfs(s)


# 4
# 4
# 1 2
# 1 3
# 2 3
# 3 4

# import queue



# n = int(input())
# adjMat = [[0]*n for _ in range(n)]
# k = int(input())
# for _ in range(k):
# 	a, b = map(int, input().split())
# 	adjMat[a-1][b-1] = 1
# 	adjMat[b-1][a-1] = 1

# # dfs
# print("dfs")
# visited = [False]*n

# def dfs(r):
#     visited[r] = True
#     print(r+1)
#     for i in range(n):
#         if adjMat[r][i] == 1 and not visited[i]:
#             dfs(i)
# dfs(0)


# # bfs
# print("bfs")
# visited = [False]*n
# queue = queue.Queue()
# queue.put(0)
# visited[0] = True
# while not queue.empty():
# 	r = queue.get()
# 	print(r+1)
# 	for i in range(n):
# 		if adjMat[r][i] == 1 and not visited[i]:
# 			queue.put(i)
# 			visited[i] = True