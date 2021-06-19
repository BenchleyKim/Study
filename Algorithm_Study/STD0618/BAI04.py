n = 1 
tmp = 1 
while n < 10**12 :
    n *= tmp 
    tmp += 1
print(tmp)
def factorial(n ) :
    ans = 1
    tmp = n
    while tmp > 0 :
        ans *= tmp 
        tmp -= 1
    return ans 

print(factorial(4))
for i in range(1, 16) :
    print(factorial(i))

def fomula(n) :
    return n**2 - 2 * n**(5/3) 

is(n)=my(s=1, F=2, t); 
while(n%F==0, t=round(n^(1/(s+1))-s/2); 
    if(prod(i=0, s, t+i)==n, return(1)); 
    s++; 
    F*=s+1); 
    0