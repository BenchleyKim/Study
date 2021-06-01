import sys 
sys.stdin = open("./Algorithm_Study/BOJ0429/BOJ9375","r")
input = sys.stdin.readline

T = int(input())
for t in range(T) :
    N = int(input())
    hashmap = {}
    for n in range(N) : 
        name, cat = input().rstrip().split()
        if hashmap.get(cat) :
            hashmap[cat].append(name)
        else :
            hashmap[cat] = [name]
    s = 1
    for k in hashmap.keys() :
        s *= len(hashmap[k])+1
    print(s-1)
