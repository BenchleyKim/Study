import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ1339/BOJ1339.in","r")
input = sys.stdin.readline

N = int(input())
words = [list(input().rstrip().zfill(8)) for i in range(N)]
check = {}
for word in words :
    for i , w in enumerate(word) :
        if w.isalpha() :
            if w in check :
                check[w] += 10**(7-i)
            else :
                check[w] = 10**(7-i)

arr = sorted(check.items() , key = lambda x : x[1], reverse= True)
ans = 0
i = 9
for k ,v in arr :
    ans += i * v
    i -= 1
print(ans)
