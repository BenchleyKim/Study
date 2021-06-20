def main():
    # 이곳에 소스코드를 작성하세요.
    # Python3 만 지원됩니다.
    # pass는 삭제해도 됩니다.
    T = int(input())
    for t in range(T) :
        N = int(input())
        camels = list(map(int, input().split()))
        camels.sort()
        ans = 0 
        if len(camels) <= 2 :
            ans = max(camels)
        else :
            first ,second = camels.pop(0), camels.pop(0)
            while len(camels) >= 2 :
                left = camels.pop()
                right = camels.pop()
                ans += min(second+first+left+second, left+right+first+first)
            if len(camels) > 0 :
                last = camels.pop()
                ans += second + first + last 
            else :
                ans += second

        print(f"#{t+1} {ans}")
main()