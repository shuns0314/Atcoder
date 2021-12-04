l = ["ABC", "ARC","AGC","AHC"]
S = [input() for _ in range(3)]

for s in S:
    l.remove(s)

print(l[0])