import sys
sys.stdin = open("./Algorithm_Study/BOJ0421/BOJ20422","r")
input = sys.stdin.readline

S = input().rstrip()
update = {'B':'b', 'D':'d','N':'n','P':'p','Q':'q','R':'r','a':'A','e':'E','h':'H','L':'l', 's':'S', 't':'T', 'y':'Y', 'z':'Z'}

match = {'A':'A',  'E':'3', 'H':'H', 'I':'I', 'M':'M', 'O':'O', 'S':'2', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y','Z':'5', 'b':'d', 'd':'b', 'i':'i', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'q', 'q':'p', 'r':'7', 'u' :'u', 'v':'v', 'w':'w', 'x':'x','0':'0', '1':'1', '2':'S', '3':'E', '5':'Z', '7':'r','8':'8'}
dstS = ''
check = [0]* len(S)
for i in range(len(S)) :
    if S[i] in update.keys() : 
        dstS += update[S[i]]
    else : 
        dstS+=S[i]
    if dstS[i] in match.keys() :

        check[i] = 1

mid = int(len(S)//2)
# if (len(S)%2) == 1 :
#     mid = len(S) // 2
print(dstS)
print(mid)
for i in range(mid, len(S)) :
    if  (i % 2) == 0 :
        flag = True
        print(dstS[i])
        for j in range(1,len(S)-i) :
            print(dstS[i+j], dstS[i-j])
            if dstS[i+j] == match[dstS[i-j]] :
                pass
            else :
                flag = False
                break
        if flag :
            print(dstS[:i])
    else :
        flag = True 
        for j in range(0,len(S)-i) :
            
            

