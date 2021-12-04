S = input()
S = S[::-1]
d = {'6': '9', '9':'6'}
tbl = str.maketrans(d)
ans = S.translate(tbl)
print(ans)
