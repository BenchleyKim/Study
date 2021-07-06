import sys
import heapq
sys.setrecursionlimit(100000)
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ2517/BOJ2517.in","r")
input = sys.stdin.readline

N = int(input())
runners = []
for i in range(N) :
    runners.append(int(input()))
A = [0] * N 
soted_runner = list(sorted([ (v, e) for e ,v in enumerate(runners) ]))

for i ,( v, e) in enumerate(soted_runner) :
    A[e] = i
tree = [0] * ( 4 * N)
def subSum(node, start, end, left, right) :
    if left > end or right < start :
        return 0
    if left <= start and end <= right :
        return tree[node]    
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2+1, (start+end)//2+1, end, left, right )

def update(node, start, end, index,diff) :
    if index < start or index > end :
        return 
    tree[node] += diff
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

for i, a in enumerate(A) :
    update(1,0,N-1,a,1)
    print(i - subSum(1,0,N-1,0,a-1) +1 )
