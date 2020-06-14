x,n = map(int, input().split())
p = list(map(int, input().split()))
mini = 1000
for i in range(-200,200):
    if not i in p:
        if mini>abs(x-i):
            ans = i
            mini=abs(x-i)
print(ans)