import re
import sys
import heapq

def solution(data, word):
    tree = {}
    nodes = {}
    leaf_check = [1] * len(data)
    for d in data :
        d = d.split()
        nodes[int(d[0])] = d[1]
        tree[int(d[0])] = int(d[2])
        if int(d[2]) == 0 :
            leaf_check[int(d[0])-1] = 0
        else :
            leaf_check[int(d[2])-1] = 0
    find_list = []
    for i in range(1,len(data)+1) :
        if leaf_check[i-1] == 0:
            continue
        l = re.finditer(word,nodes[i])
        count = 0
        prior = []
        for itr in re.finditer(word,nodes[i]):
            count += 1
            prior.append(itr.start())
        if count == 0 :
            continue
        prior.append(i)
        prior.insert(0,-count)
        
        heapq.heappush(find_list, prior)
    answer = []
    print(leaf_check)
    print(find_list)
    for f in find_list :
        node = f[-1]
        ans = ""
        while tree[node] != 0 :
            ans.insert(0,'/'+nodes[node] )
            node = tree[node]
        ans.insert(0,nodes[0])
        answer.append(ans)
            
    
    return answer

solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"],"BROWN")