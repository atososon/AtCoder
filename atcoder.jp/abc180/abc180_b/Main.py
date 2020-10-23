n = int(input())
x = list(map(int, input().split()))
x = [abs(i) for i in x]
m = sum(x)
y = sum([i**2 for i in x])**0.5
t = max(x)
print(m)
print(y)
print(t)