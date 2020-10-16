s = input()
f = 0
for i in range(len(s)):
  if i==0:
    if s[i]=="A":
      continue
    else:
      print("WA")
      break
  elif 2<=i<=len(s)-2:
    if s[i]=="C":
      f+=1
      continue
    else:
      if s[i].islower():
        continue
      else:
        print("WA")
        break
  else:
    if not s[i].islower():
      print("WA")
      break
  if f>1:
    print("WA")
    break
  if i==len(s)-1 and f==1:
    print("AC")
    break
  elif i==len(s)-1:
    print("WA")
    break