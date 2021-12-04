N =  int(input())
A = list(map(int, input().split()))

is_even = True
count = 0

while is_even:
    for a in A:
        if a % 2 == 1:
            is_even = False
    if is_even:
        A = [int(a/2) for a in A]
        count += 1

print(count)
