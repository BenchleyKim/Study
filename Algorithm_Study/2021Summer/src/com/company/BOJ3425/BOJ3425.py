import sys
from collections import deque
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ3425/BOJ3425.in","r")
input = sys.stdin.readline

commands = deque()
stack = []

while True :
    cmd = input().rstrip()
    if cmd == "QUIT" :
        break
    if cmd == "END" : 
        N = int(input())
        for _ in range(N) :
            V = int(input())
            stack = [V]
            error_flag = False
            for cmd in commands :
                if cmd == "" :
                    continue
                if cmd.startswith("NUM") :
                    cmd, value_X = cmd.split()
                    stack.append(int(value_X))
                    continue
                if len(stack) < 1 :
                    error_flag = True 
                    break
                if cmd == "POP" :
                    stack.pop()
                    continue
                if cmd == "INV" :
                    stack[-1] *= -1 
                    continue
                if cmd == "DUP" :
                    stack.append(stack[-1])
                    continue
                if len(stack) < 2 :
                    error_flag = True
                    break
                if cmd == "SWP" :
                    stack[-1] , stack[-2] = stack[-2] , stack[-1]
                    continue
                first , second = stack.pop() , stack.pop()
                if cmd == "ADD" :
                    result = first + second
                if cmd == "SUB" :
                    result = second - first
                if cmd == "MUL" :
                    result = first * second
                if cmd == "DIV" :
                    if first == 0 :
                        error_flag = True
                        break
                    result = abs(second) // abs(first)
                    if first < 0 or second < 0 :
                        if first < 0 and second < 0 :
                            pass
                        else :
                            result = -result
                if cmd == "MOD" :
                    if first == 0 :
                        error_flag = True
                        break
                    result = abs(second) % abs(first)
                    if second < 0 :
                        
                        result = -result
                if abs(result) > 10**9 :
                    error_flag = True
                    break
                stack.append(result)
            if error_flag == True :
                print("ERROR")
                continue
            if len(stack) == 1 :
                print(stack[-1])
            else :
                print("stack is not 1 error")
                print("ERROR")
        commands = deque()
        print()
        continue
    commands.append(cmd)
