a, b, s = map(int, input().split())
if a + b > s :
    if s == a or s == b :
        print("YES")
    print("NO")
else : 
    n = s % (a + b)
    if n == a or n == b or n == 0 :
        print("YES")
    else : 
        if (s - a) % b == 0 or (s - b) % a == 0 :
            print("YES")
        else : 
            print("NO")
  
        
