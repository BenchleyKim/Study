sb = {'KOREA': 9, 'CCC': 0, 'BBB': 3, 'AAA': 6}
print(sorted(sb.items(), key=lambda x:x[1], reverse=True))