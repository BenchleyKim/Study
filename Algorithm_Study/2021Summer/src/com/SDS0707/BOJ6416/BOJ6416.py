import sys
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0707/BOJ6416/BOJ6416.in","r")
input = sys.stdin.readline

k = 1
graph  = {}
cnt = 0 
endFlag = True


while endFlag :
    line = input().rstrip()
    if line == "" :

        if len(graph.keys()) == cnt + 1 :
            print(f"Case {k} is a tree.")
        else :
            print(f"Case {k} is not a tree.")
        graph =  {}
        cnt =  0
        k += 1
    arr = list(map(int, line.split()))

    for i in range(len(arr) // 2) :
        v, e = arr[i*2] , arr[i*2+1]
        if v == 0 and e == 0 :
            break
        if v == -1 and e == -1 :
            if len(graph.keys()) == cnt + 1 :
                print(f"Case {k} is a tree.")
            else :
                print(f"Case {k} is not a tree.")
            graph =  {}
            cnt =  0
            k += 1
            endFlag = False
            break
        
        cnt += 1
        if v in graph :
            graph[v].append(e)
        else :
            graph[v] = [e]
        if e in graph:
            graph[e].append(v)
        else :
            graph[e] = [v]
        
    
