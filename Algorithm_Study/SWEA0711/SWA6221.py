man1 = input()
man2 = input()
rsp = {'가위' : 0 , "바위" : 1 , "보" : 2 }
if rsp[man1] == rsp[man2] :
    print("Result : Draw")
elif rsp[man1] < rsp[man2] :
    if rsp[man2] == 2 and rsp[man1] == 0 :
        print("Result : Man1 Win!")
    else :
    	print("Result : Man2 Win!")
else :
    if rsp[man1] == 2 and rsp[man2] == 0 :
        print("Result : Man2 Win!")
    else :
    	print("Result : Man1 Win!")