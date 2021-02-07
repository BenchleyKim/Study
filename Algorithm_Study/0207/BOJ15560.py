# 길이 N의 수열 K1, K2, ..., KN과 상수 U, V가 주어진다.

# Q개의 쿼리가 주어지며, 그 종류는 두 가지가 있다.

# A, B가 주어지면, max(U × (Ki + Ki + 1 + ... + Kj) + V × (j - i)) (A ≤ i ≤ j ≤ B) 의 값을 구한다.
# A, B가 주어지면, KA의 값을 B으로 바꾼다.

# 첫 번째 줄에 N과 Q, U, V가 입력된다. (1 ≤ N, Q ≤ 103,  - 5 ≤ U, V ≤ 5)

# 두 번째 줄에 K1, K2, ..., KN이 주어진다. ( - 102 ≤ Ki ≤ 102)

# 세 번째 줄부터 쿼리가 주어진다. 세 수 C, A, B가 주어진다. (1 ≤ A, B ≤ N, 0 ≤ C ≤ 1)

# C가 0이면 첫 번째 쿼리를, 아니면 두 번째 쿼리를 수행한다. 첫 번째 쿼리일 경우 1 ≤ A ≤ B ≤ N 이다. 두 번째 쿼리일 경우 1 ≤ A ≤ N,  - 102 ≤ B ≤ 102이다.


# 한 줄마다 첫 번째 쿼리의 결과값을 출력한다.

# 입력 예시
# 5 3 2 4
# 1 1 1 1 1
# 0 1 5
# 1 3 -2
# 0 1 5
# 출력 예시
# 26
# 20

N , Q , U , V = map(int, input().split())
K = list(map(int, input().split()))
result = []
for i in range(Q) :
    C , A ,B = map(int, input().split())
    if C == 0 :
        result.append(sum(K[A-1:B])*U+(B-A)*V)
    if C == 1 :
        K[A-1] = B

for r in result :
    print(r)
