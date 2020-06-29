n = int(input())
a = [int(input()) for _ in range(n)]
temp = sorted(a)
m1 = temp[-1]
m2 = temp[-2]
for i in range(n):
    if a[i] == m1:
        print(m2)
    else:
        print(m1)