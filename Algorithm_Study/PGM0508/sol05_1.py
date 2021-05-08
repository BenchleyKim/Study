
import heapq

    


def solution(k, num, links):
    answer = 0
    length = len(num)
    check = [0] * length
    parent = [-1] * length
    
    for node in range(length) :
        left, right = links[node]
        if left != -1 : 
            parent[left] = node
        if right != -1 :
            parent[right] = node
               
        if left == -1 and right == - 1:
            check[node] = num[node]
    print(parent)
    def search_node(node) :
        if check[node] == 0 :
            ans = num[node]
            left, right  = links[node]
            if left != - 1 :
                ans += search_node(left)
            if right != -1 :
                ans += search_node(right)
            return ans
        else :
            return check[node]
    heap = []
    root = 0
    mx =  0
    for node in range(length) :
        check[node] = search_node(node)
        if check[node] > mx : 
            root = node
            mx  = check[node]
        heapq.heappush(heap, (-check[node], node))
    print(root)
    stack = [root]
    heap = []
    visited = [0] * length
    while stack :
        node = stack.pop()
        left, right =  links[node]
        if left != -1 :
            stack.append(left)
            heapq.heappush(heap, (-(check[node]-check[left]),node))

    
    ww, root = heapq.heappop(heap)
    if k < 1 :
        answer = -ww
        return answer
    if k == length - 1 :
        return max(num)
    for i in range(k-1) :
        print(i, heap)
        w, node = heapq.heappop(heap)
        p = parent[node]
        if p == -1 :
            continue
        check[p] += w 
        heapq.heappush(heap, (-check[p], p))
    answer = max(check)

    print(heap)
    print(parent)
    print(check)

    return answer


print(solution(3	,[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],	[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
print(solution(1	,[6, 9, 7, 5]	,[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(2	,[6, 9, 7, 5]	,[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(4	,[6, 9, 7, 5]	,[[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
