def solution(n, k, cmds):
    # 집합 자료형을 구현 
    arr = {i : [i-1,i+1] for i in range(n)}
    start_node = 0
    end_node = n-1
    current_state = k 
    redo_stack = []
    check = [1] * n 
    for cmd in cmds :
        op = cmd[0]
        if op == 'U' :
            x = int(cmd.split()[1])
            while x > 0 :
                x -= 1 
                current_state = arr[current_state][0]
        elif op == 'D' :
            x = int(cmd.split()[1])
            while x > 0 :
                x -= 1 
                current_state = arr[current_state][1]
        elif op == 'C' :
            deletenode = current_state
            left_node = arr[deletenode][0]
            right_node = arr[deletenode][1]
            check[deletenode] = 0
            if deletenode == end_node :
                # 삭제할 노드 
                
                # 위쪽 노드가 새로운 마지막 노드 
                current_state = left_node
                end_node = left_node
                redo_stack.append((deletenode,arr[deletenode][0], arr[deletenode][1]))
                continue
            if deletenode == start_node :
                current_state= right_node
                start_node = right_node
                redo_stack.append((deletenode,arr[deletenode][0], arr[deletenode][1]))
                continue
            current_state = right_node
            # 위치 재할당 
            arr[left_node][1] = right_node
            arr[right_node][0] = left_node
            redo_stack.append((deletenode,arr[deletenode][0], arr[deletenode][1]))

        elif op == 'Z' :
            recov_node, node_left, node_right = redo_stack.pop()
            check[recov_node] = 1
            if node_left != -1 :
                if end_node == node_left :
                    end_node = recov_node
                arr[node_left][1] = recov_node
            if node_right != n :
                if node_right == start_node :
                    start_node = recov_node
                arr[node_right][0] = recov_node
    answer = ''
    for c in check :
        if c :
            answer += 'O'
        else :
            answer += 'X'


    
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))