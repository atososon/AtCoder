import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
s = list(itertools.permutations(range(1,n+1),n))
print(abs(s.index(p)-s.index(q)))