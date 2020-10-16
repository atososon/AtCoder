o = input()
e = input()
for i in range(len(e)):
    print(o[i], e[i], sep="", end="")
if len(o)-len(e) == 1:
    print(o[-1], sep="")