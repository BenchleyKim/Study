def pop(stack, registers , name, answer) :
    if not stack :
        answer.append("EMPTY")
        return
    if name == 'A' :
        registers[0] = stack.pop()
        return
    if name == 'B' :
        registers[1] = stack.pop()
        return 
def push(stack, cnt, answer) :
    if len(stack) >= 8 :
        answer.append("OVERFLOW")
        return 
    stack.append(cnt)
    return
def swap(registers , answer ) :
    if None in registers :
        answer.append("ERROR")
        return 
    registers[0], registers[1] =registers[1], registers[0]
    return
def sub(registers , stack, answer ) :
    if None in registers :
        answer.append("ERROR")
        return 
    stack.append(registers[0]- registers[1])
    return

def add(registers , stack ,answer ) :
    if None in registers :
        answer.append("ERROR")
        return 
    stack.append(registers[0] + registers[1])
    return
def prt(stack, answer ) :
    if not stack :
        answer.append("EMPTY")
        return
    answer.append(str(stack.pop()))

def solution(params):

    answer = []
    stack = [ ]
    registers = [None, None]
    # commands = {"POPA" : pop(stack,registers,"A", answer), "POPB" :pop(stack,registers,"B", answer),
    #             "ADD" : add(registers, stack, answer), "SUB" : sub(registers, stack, answer),
    #             "PUSH0" : push(stack, 0, answer), "PUSH1" : push(stack, 1, answer),
    #             "PUSH2" : push(stack, 2, answer), "PUSH3" : push(stack, 3, answer),
    #             "SWAP" : swap(registers, answer), "PRINT" : prt(stack,answer)}
    commands = ["POPA", "POPB" ,"ADD" , "SUB" , "PUSH0" , "PUSH1" ,"PUSH2" , "PUSH3" ,"SWAP" , "PRINT" ]
    for cmd in params :
        if not cmd in commands : 
            answer.append("UNKNOWN")
            continue
        if cmd == "POPA" : 
            pop(stack,registers,"A", answer)
        if cmd == "POPB" :
            pop(stack,registers,"B", answer)
        if cmd == "ADD" :
            add(registers, stack, answer)
        if cmd == "SUB" :
            sub(registers, stack, answer)
        if cmd == "PUSH0" :
            push(stack, 0, answer)
        if cmd == "PUSH1" :
            push(stack, 1, answer)
        if cmd == "PUSH2" :
            push(stack, 2, answer)
        if cmd == "PUSH3" :
            push(stack, 3, answer)
        if cmd == "SWAP" :
            swap(registers, answer)
        if cmd == "PRINT" :
            prt(stack,answer)



    return answer
