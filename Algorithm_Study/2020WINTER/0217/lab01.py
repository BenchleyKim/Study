import sys
sys.stdin = open('./Algorithm_study/0217/lab01','r')
INF = 10000000000

def init(node, start, end) :
  print(start,end)
  print(tree)
  if start == end :
    tree[node] = arr[start]
    return tree[node]
  mid = (start + end) // 2
  tree[node] = min(init(node*2, start, mid),init(node*2+1, mid+1, end))
  return tree[node]

def find(node, start, end, left, right) :
  if start > right | end < left : return INF
  if end <= right & left <= start : 
    return tree[node]
  mid = (start+end) // 2
  return min(find(node*2,start,mid,left,right),find(node*2+1,mid+1,end,left,right))
N = int(input())
arr = list(map(int,input().split()))
print(arr)
tree = [0] * N * 4
print(tree)
init(1,0,N)
print(tree)
M = int(input())
for _ in range(M) :
  a,b = map(int,input().split())
  print(find(1,0,N-1,a-1,b-1))

