def solution(n, k, cmd):
    answer = ''
    length = n 
    current = k 
    check = ['O'] * length
    end  = n-1 
    redo = [] 
    for c in cmd :
        oper = c[0]
        if oper == 'D' :
            x = int(c.split()[1])
            while x > 0 :
                current += 1
                if check[current] == 'X' :
                    continue
                x -= 1
            continue
        if oper == 'U' :
            x = int(c.split()[1])
            while x > 0 :
                current -= 1
                if check[current] == 'X' :
                    continue
                x -= 1
            continue
        if oper == 'C' :
            check[current] = 'X' 
            redo.append(current) 
            if current == end :
                current -= 1
                while check[current] =='X':
                    current -=1 
            else :
                current += 1
                while check[current] =='X' :
                    current += 1
            continue
        if oper =='Z' :
            check[redo.pop()] == 'O'
            continue
    answer = str(check)
    print(check)
    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))