import sys
sys.stdin = open(".\Algorithm_Study\BOJ0524\BOJ4358","r")
input = sys.stdin.readline

hashmap = {}
tmp = input().rstrip()
cnt = 0
while tmp :
    cnt += 1
    if hashmap.get(tmp) :
        hashmap[tmp] += 1
    else :
        hashmap[tmp] = 1
    tmp = input().rstrip()
for i in sorted(hashmap.keys()) :
    print(f"{i} {hashmap[i]/cnt * 100:.4f}")