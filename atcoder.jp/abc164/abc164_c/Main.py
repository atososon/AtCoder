n = int(input())
a = [input() for i in range(n)]
a.sort()
print(len(set(a)))