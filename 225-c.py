N, M = map(int, input().split())

def calc(l):
    return [(j-1)//7 for j in l], [(j-1)%7 for j in l]

l_0 = list(map(int, input().split()))
div_0, mod_list_0 = calc(l_0)
print(div_0, mod_list_0)

ans = False
for i in range(N-1):
    l = list(map(int, input().split()))
    div_list, mod_list = calc(l)
    print(div_list, mod_list)
    if (div_0[0] + i + 1 == div_list[0]) and (mod_list == mod_list_0) and (len(set(div_list))== 1):
        pass
    else:
        ans = True

ddd = False
for i, j in enumerate(mod_list_0):
    if i != 0:
        if k+1 != j:
            ddd = True
    k = j

if ans or ddd or (len(set(div_0))!= 1):
    print("No")
else:
    print("Yes")
