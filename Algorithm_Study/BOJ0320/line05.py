import re
def argsNumber(idx) :
    next_idx = idx + 1
    if next_idx > len(command) -1 :
        return False
    if command[next_idx].isdigit() :
        check[idx] = check[next_idx] = 1 
        return True
    else : return False
def argsString(idx) :
    next_idx = idx + 1
    if next_idx > len(command) -1 :
        return False
    if command[next_idx].isalpha() :
        check[idx] = check[next_idx] = 1 
        return True
    else : return False
    return True

def argsNulls(idx) :
    check[idx] = 1
    
def argsNumbers(idx) :
    while idx < len(command) and command[idx] not in flag_match.keys() :
        if argsNumber(idx) :
            idx += 1
        else :
            return False 
    return True
def argsStrings(idx) :
    while idx < len(command) and command[idx] not in flag_match.keys() :
        if argString(idx) :
            idx += 1
        else :
            return False 
    return True
            


def argcheck(commands,program, flag_rules) :
    global command
    global flag_match
    global check
    command = commands.split()
    flag_match = {}
    for flag in flag_rules :
        flag = flag.split()
        flag_match[flag[0]] = flag[1]
    if command[0] != program :
        return False
    check = [0] * len(command)
    check[0] = 1
    for idx in range(1, len(command)) :
        print(command[idx],check)
        if check[idx] : 
            continue
        if command[idx] in flag_match.keys() :
            if flag_match[command[idx]] == 'STRINGS' :
                if argsStrings(idx+1) :
                    continue
                else :
                    return False
            elif flag_match[command[idx]] == 'NUMBERS' :
                if argsNumbers(idx) :
                    continue
                else :
                    return False
            elif flag_match[command[idx]] == 'STRING' :
                if argsString(idx) :
                    continue
                else :
                    return False 
            elif flag_match[command[idx]] == 'NUMBER' :
                if argsNumber(idx) :
                    continue
                else :
                    return False 
            elif flag_match[command[idx]] == "NULL" :
                argsNull()
        else :
            return False
    return True
            
                
            
            
def solution(program, flag_rules, commands):
    answer = []
    for command in commands :
        
        answer.append(argcheck(command, program, flag_rules))
    
    return answer

print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"],	["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
print(solution("trip"	,["-days NUMBERS", "-dest STRING"],	["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]	))