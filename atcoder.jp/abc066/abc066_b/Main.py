s = input()
for i in range(len(s)-1, 0, -1):
    if i%2 == 1:
        pass
    
    else:
        if s[:i//2] == s[i//2:i]:
            print(i)
            break
    