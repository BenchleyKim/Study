import sys
sys.stdin = open(".\Algorithm_Study\BOJ0601\BOJ5052","r")
input = sys.stdin.readline

T = int(input())
for t in range(T) :
    N = int(input())
    arr = []
    for i in range(N) :
        arr.append(input().rstrip())
    arr = sorted(arr, key= lambda x : len(x))
    num_dict = {}
    flag = False 
    for string in arr :
        base_dict = num_dict
        if flag :
            break
        for s in range(len(string)-1) :
            if base_dict.get(string[s])  :
                if base_dict.get(string[s]) == 1 :
                    flag = True
                    break
                else :
                    base_dict = base_dict[string[s]]
                    continue
            base_dict[string[s]] = {}
            base_dict = base_dict[string[s]]
        base_dict[string[-1]] = 1 
    if flag : 
        print("NO")
    else :
        print("YES")

    
    