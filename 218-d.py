def fuct(n):
  return n*(n-1) // 2
 
N = int(input())
position = {}
ans = 0
 
for _ in range(N):
  x, y = map(int, input().split())
  if x in position:
    position[x].append(y)
  else:
    position[x] = [y,]
print(position)

y_position = []
for y_list in position.values():
  if len(y_list) < 2:
    continue
  else:
    y_position.append(set(y_list))
print(y_position)

for i in range(len(y_position)-1):
  for j in range(i+1, len(y_position)):
    print(i,j)
    n = len(list(y_position[i] & y_position[j]))
    print(n)
    if n >= 2:
      ans += fuct(n)
 
print(ans)