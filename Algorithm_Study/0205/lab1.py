

def init(start, end, r):
    if start == end:
        tree[r] = array[start]
        return tree[r]
    
    mid = (start + end) // 2
    tree[r] = init(start, mid, r * 2) + init(mid + 1, end, r * 2 + 1)
    return tree[r]

def sumInterval(start, end, r, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[r]
    
    mid = (start+end) // 2
    return sumInterval(start, mid, r*2, left, right) + sumInterval(mid + 1, end, r*2+1, left, right)

def update(start, end, r, index, dif):
    if index < start or index > end:
        return 
    
    tree[r] += dif
    if start == end:
        return
    
    mid = (start+end) // 2
    update(start, mid, r*2, index, dif)
    update(mid+1, end, r*2+1, index, dif)



N = int(input())
array = list(map(int, input().split()))
tree = [0] * (2 * N)
K = int(input())
init(0, N-1, 1)
result = []
for i in range(K):
    a,b,c =  input().split()
    b = int(b)
    c = int(c)

    if a == 'u':
        b -= 1
        diff = c - array[b]
        array[b] = c
        update(0, N-1, 1, b, diff)
    elif a == 's':
        result.append(sumInterval(0, N-1, 1, b-1, c-1))

for t in result :
    print(t)
      
