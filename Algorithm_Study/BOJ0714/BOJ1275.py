import sys
sys.stdin = open("./Algorithm_Study/BOJ0714/BOJ1275.in","r")
input = sys.stdin.readline

N, Q = map(int, input().split())
l = list(map(int, input().split()))

def init(node, start, end): 
    # node가 leaf 노드인 경우 배열의 원소 값을 반환.
    if start == end :
        tree[node] = l[start]
        return tree[node]
    else :
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)

def subSum(node, start, end, left, right) :
    
    # 겹치지 않기 때문에, 더 이상 탐색을 이어갈 필요가 없다.    
    if left > end or right < start :
        return 0

    # 구해야하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함되고
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적이다.
    if left <= start and end <= right :
        return tree[node]

    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야한다.
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start+end)//2+1, end, left, right)

def update(node, start, end, index, diff) :

    if index < start or index > end :
        return

    tree[node] += diff
    
    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사해야함.
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

tree = [0] * 10 * 4
init(1, 0, N-1)
for i in range(Q) :
    print(tree)
    X, Y, A, B = map(int, input().split())
    print(subSum(1,0,N-1, X, Y))
    update(1,0,N-1, A, B-l[A])

