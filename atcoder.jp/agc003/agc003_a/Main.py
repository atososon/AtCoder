s = input()
if (s.count("W")>=1 and s.count("E")>=1 or s.count("W")==0 and s.count("E")==0) and (s.count("N")>=1 and s.count("S")>=1 or s.count("N")==0 and s.count("S")==0):
    print("Yes")
else:
    print("No")