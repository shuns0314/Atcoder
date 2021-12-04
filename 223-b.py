s = input()
l = len(s)
a = []

for i in range(l):
    a.append(s)
    s = s[1:] + s[0]
a = sorted(a)

print(a[0])
print(a[-1])
