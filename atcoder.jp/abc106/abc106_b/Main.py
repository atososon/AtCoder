n = int(input())
def solve(n):
  li = list()
  for i in range(1, n+1):
    if n%i == 0:
      li.append(i)
  return li
ans = 0
for i in range(2, n+1):
  if len(solve(i)) == 8 and i%2 == 1:
    ans += 1
    
print(ans)
      
    