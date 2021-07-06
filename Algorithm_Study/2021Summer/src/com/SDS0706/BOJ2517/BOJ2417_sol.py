import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ2517/BOJ2517.in","r")

sys.setrecursionlimit(100000)
# 세그먼트 트리 생성
def set_tree(n,node, strt, end):
    if strt == end:
        tree[node] = 1
        return tree[node]
    mid = (strt+end)//2
    if n<=mid:
        tree[node] = set_tree(n,2*node,strt,mid)+tree[2*node+1]
    else:
        tree[node] = tree[2*node] + set_tree(n,2*node+1,mid+1,end)
    return tree[node]
# 세그먼트 트리 서치
def search(n,node, strt, end):
    if strt == end:
        return tree[node]
    mid = (strt+end)//2
    if n<=mid:
        return search(n,2*node,strt,mid) + tree[2*node+1]
    else:
        return search(n,2*node+1,mid+1, end)

N = int(sys.stdin.readline())
position = []
rel_val = dict()
for current in range(1,N+1):
    record = int(sys.stdin.readline())
    position.append(record)
tmp = sorted(position)
for idx in range(N):
    rel_val[tmp[idx]] = idx
tree = [0]*(4*N+2)
idx = 0
for record in position:
    idx +=1
    set_tree(rel_val[record],1, 0, N)
    predict = search(rel_val[record],1,0,N)
    print(min(predict,idx))
