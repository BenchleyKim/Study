import sys
sys.stdin = open(".\Algorithm_Study\COTE0616\\test01","r")
input = sys.stdin.readline

def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    T = int(input())
    for t in range(T) :
        N = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        ans = 0 
        if len(arr) <= 2 :
            ans = max(arr)
        else :
            f ,s = arr.pop(0), arr.pop(0)
            while len(arr) >= 2 :
                left = arr.pop(0)
                right = arr.pop(0)
                ans += max(left,right)
                ans += max(f,s)
                ans += f+s
            if len(arr) > 0 :
                last = arr.pop(0)
                ans += min(f,s)
                ans += last
            else :
                ans += max(f,s)

        print(f"#{t+1} {ans}")
main()