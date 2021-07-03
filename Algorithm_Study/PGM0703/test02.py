# 2진수 문자열(8비트) -> 16진수 문자열
def boost_bin2hex(bin_str) :
    bits = {10 : 'A', 11:"B", 12:"C", 13:"D", 14:"E", 15:"F" }
    result = 0 
    f =  int(bin_str[0]) * 8 + int(bin_str[1]) * 4 + int(bin_str[2]) * 2 + int(bin_str[3]) * 1
    if f >= 10 :
        f= bits[f]
    s =  int(bin_str[4]) * 8 + int(bin_str[5]) * 4 + int(bin_str[6]) * 2 + int(bin_str[7]) * 1
    if s >= 10 :
        s = bits[s]

    return str(f) + str(s)

# 10진수 입력 -> 16진수 문자열
def boost_dec2hex(dec) :
    bits = {10 : 'A', 11:"B", 12:"C", 13:"D", 14:"E", 15:"F" }
    dec = int(dec)
    f, s = divmod(dec, 16)
    if f >= 10 :
        f= bits[f]
    if s >= 10 :
        s = bits[s]
    return str(f) + str(s) 






registers = { 'A' : '111', 'B' : '000', 'C' : '001', 'D' : '010', 'E' : '011', 'H' : '100', 'L' : '101'}
def solution(param0):
    answer = ''
    if param0[2] != ' ' :
        return "ERROR"
    cmd, body = param0.split()
    if body[1] != ',' :
        return "ERROR"
    r1 ,r2 = body.split(",")
    if cmd == 'LD' :
        if r1 in registers and r2 in registers :
            answer += "01" + registers[r1] + registers[r2]
        else :
            return "ERROR"
        if r1 == r2  :
            return "NOOP"
        answer = boost_bin2hex(answer)
    if cmd == 'LN' :
        if r1 in registers :
            answer += "00" + registers[r1] + "110"
        else :
            return "ERROR"
        r2 = boost_dec2hex(r2) 
        answer = boost_bin2hex(answer) + r2 



    return "0x" + answer