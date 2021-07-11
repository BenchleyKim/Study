c = input()
if not c.isalpha() :
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(c, ord(c), c,ord(c)))
elif c.islower() :
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(c, ord(c), c.upper(),ord(c.upper())))
else :
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(c, ord(c), c.lower(),ord(c.lower())))
