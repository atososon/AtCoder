x = int(input())
s = [1]
for i in range(2,100):
    for j in range(2,12):
        if i**j <= 1000:
            s.append(i**j)
s.sort()
for i in range(-1, -1*len(s)-1, -1):
    if x >= s[i]:
        print(s[i])
        break