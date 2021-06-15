from os import error
import sys
sys.stdin = open(".\Algorithm_Study\BOJ0614\BOJ4836","r")
input = sys.stdin.readline

def check( string ) :
    
    str_list = string.split()
    # rule 1 
    rule1_flag = False
    for i in range(len(str_list)) :
        if str_list[i] == 'dip' :
            rule1_flag = False
            if i >= 1 :
                if str_list[i-1] == 'jiggle' :
                    rule1_flag = True
                    continue
            if i >= 2 :
                if str_list[i-2] == 'jiggle' :
                    rule1_flag = True
                    continue
            if i < len(str_list) - 1:
                if str_list[i+1] == 'twirl' :
                    rule1_flag = True
                    continue
            if not rule1_flag :
                str_list[i] = 'DIP'
                continue
    if 'DIP' in str_list :
        rule1_flag = False
    if 'dip' not in str_list and 'DIP' not in str_list :
        rule1_flag = True
    
    # rule 2 
    rule2_flag = False
    if len(str_list) >= 2 :
        if str_list[-1] == 'clap' and str_list[-2] == 'stomp' and str_list[-3] == 'clap' :
            rule2_flag = True
    # rule 3 
    rule3_flag = False
    if 'twirl' in str_list :
        if 'hop' in str_list :
            rule3_flag = True
    else :
        rule3_flag = True
    
    # rule 4 
    rule4_flag = False
    if str_list[0] != 'jiggle' :
        rule4_flag = True
    
    # rule 5 
    rule5_flag = False
    if 'dip' in str_list or 'DIP' in str_list :
        rule5_flag = True
    error_list = []

    for i, a in enumerate((rule1_flag, rule2_flag, rule3_flag, rule4_flag, rule5_flag)) :
        if a == False :
            error_list.append(i+1)

    return error_list, " ".join(str_list)


while True :
    tmp = input().rstrip()
    if tmp  == '' :
        break
    print("form",end=' ')
    result, answer = check(tmp)
    if len(result) :
        print("error",end='')
    else :
        print(f"ok: {tmp}")
        continue
    if len(result) > 1 :
        print("s",end=' ')
        for i in range(len(result) -2) :
            print(result[i], end=", ")
        print(f"{result[-2]} and {result[-1]}: {answer}")
    else :
        print(f" {result[0]}: {answer}")


