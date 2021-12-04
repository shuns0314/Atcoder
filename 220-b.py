K = int(input())
A, B = input().split()

def kto10(x: str, k):
    result = 0
    for i, s in enumerate(x[::-1]):
        result += (int(s) * k**i)
    return result

print(kto10(A, K)*kto10(B, K))
