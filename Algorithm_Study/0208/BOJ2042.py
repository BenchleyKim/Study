# 문제
# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

# 입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 예제 입력 1 
# 5 2 2
# 1
# 2
# 3
# 4
# 5
# 1 3 6
# 2 2 5
# 1 5 2
# 2 3 5
# 예제 출력 1 
# 17
# 12
def init(start, end, r) :
    if start == end :
        tree[r] = arr[start]
        return tree[r]
    mid = (end + start) // 2
    tree[r] = init(start, mid, r*2) + init(mid+1, end, r*2+1)
    return tree[r]

def sumInterval(start, end, r, left ,right) :
    if left > end or right < start :
        return 0
    if left <= start and end <= right :
        return tree[r]
    mid = (start + end) // 2
    resum = sumInterval(start, mid, r*2 , left, right) + sumInterval(mid+1, end, r*2+1, left, right)
    return resum

def update(start, end, r, idx, diff) :
    if idx > end or idx < start :
        return 
    tree[r] += diff
    if start == end :
        return
    mid = (start+end) // 2
    update(start, mid , r*2, idx, diff) 
    update(mid+1, end, r*2+1, idx, diff)

N , M , K = map(int,input().split())
tree = [0] * 3000000
arr = []
for _ in range(N) :
    arr.append(int(input()))

# print(arr)
init(0, N-1, 1)
# print(tree)
for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1 : 
        # b번째 수를 c로 바꾸고 
        diff = c - arr[b-1] 
        arr[b-1] = c
        update(0,N-1, 1, b-1, diff)
        # print(arr)
    if a == 2 :
        # b번째 수부터 c번쨰 수까지의 합을 구하여 출력
        sum = sumInterval(0, N-1, 1, b-1, c-1)
        print(sum)