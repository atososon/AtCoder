x, y = map(int, input().split())
xy = [x,y]
if x == y:
    print(x)
elif 0 in xy and 1 in xy:
    print(2)
elif 1 in xy and 2 in xy:
    print(0)
elif 0 in xy and 2 in xy:
    print(1)
