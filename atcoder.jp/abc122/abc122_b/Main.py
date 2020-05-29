s = input()
ans = 0
for i in range(len(s)):
    count = i
    acgt = 0
    while count<=len(s)-1:
        if s[count]=="A" or s[count]=="C" or s[count]=="G" or s[count]=="T":
            acgt+=1
        else:
            break
        ans = max(ans,acgt)
        count+=1
print(ans)