
def argcheck(program, flag_match, commands) :
    command = commands.split()
    if command != program :
        return False
    check = [0] * len(command)
    for idx in range(1, len(command)) :
        print(command[idx])
        if check[idx] : 
            continue

def solution(program, flag_rules, commands):
    answer = []
    flag_match = {}
    for flag in flag_rules :
        flag = flag.split()
        flag_match[flag[0]] = flag[1]
    for command in commands :
        
        answer.append(argcheck(program, flag_match, commands))
    
    return answer