import sys

sys.stdin = open(".\Algorithm_Study\BOJ0510\BOJ21734","r")
input = sys.stdin.readline

S = list(input().rstrip())
def sum_idx(i) :
    ans = 0
    while i > 0 :
        ans += i%10
        i //= 10
    return ans
for s in S :
    idx = ord(s)
    print(s*sum_idx(idx))

