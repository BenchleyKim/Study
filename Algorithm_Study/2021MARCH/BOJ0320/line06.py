import re

def argcheck(command,program, flag_match, flag_functions, flag_list) :
    command = command.split()
    
    if command[0] != program :
        return False
    check = [0] * len(command)
    check[0] = 1
    for idx in range(1, len(command)) :
        if check[idx] : 
            continue
        if command[idx] in flag_match.keys() :
            flag_function = flag_match[command[idx]]
            flag_type = flag_list[flag_function]
            if flag_functions[flag_function] == 1 :
                return False
            else :
                flag_functions[flag_function] = 1 

            next_idx = idx+1 
            if flag_type == 'STRINGS' :
                if next_idx > len(command)-1 :
                    return False
                success_flag = False 
                while str(command[next_idx]).isalpha() :
                    success_flag = True
                    check[next_idx] = 1
                    next_idx += 1
                if success_flag :
                    check[idx] = 1
                else : 
                    return False
            if flag_type == 'NUMBERS' :
                if next_idx > len(command)-1 :
                    return False
                success_flag = False 
                while str(command[next_idx]).isdigit() :
                    success_flag = True
                    check[next_idx] = 1
                    next_idx += 1
                if success_flag :
                    check[idx] = 1
                else : 
                    return False
            if flag_type == 'STRING' :
                if next_idx > len(command)-1 :
                    return False
                if str(command[idx+1]).isalpha() :
                    check[idx] = check[idx+1] = 1
                else : 
                    return False
            elif flag_type == 'NUMBER' :
                if next_idx > len(command)-1 :
                    return False
                try : 
                    print(int(command[idx+1]))
                except ValueError :
                    return False
                check[idx] = check[idx+1] = 1
            elif flag_type == "NULL" :
                check[idx] = 1
                    
        else :
            return False
    return True
            
                
            
            
def solution(program, flag_rules, commands):
    answer = []
    for command in commands :
        flag_match = {}
        flag_list = {}

        flag_functions = {}
        # flag_match = {키워드 : [타입 , 실제 기능]}
        for flag in flag_rules :
            print(flag)
            flag = flag.split()
            if flag[1] == 'ALIAS' :
                flag_match[flag[0]] =  flag[2]
            else : 
              flag_list[flag[0]] = flag[1]
              flag_match[flag[0]] = flag[0]
            flag_functions[flag[0]] = 0
            
        
        answer.append(argcheck(command, program, flag_match, flag_functions,flag_list))
    
    return answer

print(solution("line",	["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],	["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
print(solution("bank"	,["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"],	["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]	))