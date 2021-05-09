
def solution(keycode, keyday, data):
    answer = []
    arr = {}
    for da in data :
        price, code, time = da.split()
        price = int(price.split('=')[1])
        code = code.split('=')[1]
        time = time.split('=')[1]
        date = time[:8]
        time = int(time)
        if arr.get(code) :
            if arr[code].get(date) :
                arr[code][date].append((time,price))
            else :
                arr[code][date] = [(time,price)]
        else :
            arr[code] = {date : [(time,price)]}
    for i in sorted(arr[keycode][keyday]) :
        answer.append(i[1])

    return answer


print(solution("012345"	,"20190620",	["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))
