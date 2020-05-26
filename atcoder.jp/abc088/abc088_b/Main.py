n = int(input())
a = list(map(int, input().split()))
alice = 0
bob = 0
a.sort()
for i in range(n):
    if i%2==0:
        alice += a[-1]
        a.pop()
    elif i%2==1:
        bob += a[-1]
        a.pop()
print(alice-bob)