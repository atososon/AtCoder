k=int(input())
s=input()
if len(s)>k:
    print(s[:k],'...',sep='')
else:
    print(s)