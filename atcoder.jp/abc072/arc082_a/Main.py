n = int(input())
a = list(map(int, input().split()))
l = [0] * 10**5
for i in range(n):
    if a[i] != 0:
        l[a[i]-1] += 1
    if a[i] != 10**5-1:
        l[a[i]+1] += 1
    l[a[i]] += 1
print(max(l))