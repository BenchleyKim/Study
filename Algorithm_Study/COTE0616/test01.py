import heapq

def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    T = int(input())
    for t in range(T) :
        N = int(input())
        print(N)
        arr = list(map(int, input().split()))
        arr.sort()
        print(arr)
        ans = 0 
        if len(arr) <= 2 :
            ans = max(arr)
        else :
            f ,s = arr.pop(0), arr.pop(0)
            while len(arr) < 2 :
                left = arr.pop(0)
                right = arr.pop(0)
                ans += max(left,right)
                ans += max(f,s)
                ans += f
                
                
main()