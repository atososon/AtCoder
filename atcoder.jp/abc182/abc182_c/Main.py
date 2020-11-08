n = input()
l = len(n)
count_1 = n.count("1")
count_2 = n.count("2")
count_3 = n.count("3")
count_4 = n.count("4")
count_5 = n.count("5")
count_6 = n.count("6")
count_7 = n.count("7")
count_8 = n.count("8")
count_9 = n.count("9")
s = 0
for i in range(l):
    s += int(n[i])
if s%3 == 0:
    print("0")
elif s%3 == 1:
    if count_1>0 and s>=4 or count_4>0 and s>=7 or count_7>0 and s>=10:
        print("1")
    else:
        if count_2>1 and s>=7 or count_5>1 and s>=13 or count_8>1 and s>=19 or count_2>0 and count_5>0 and s>=10 or count_2>0 and count_8>0 and s>=13 or count_8>0 and count_5>0 and s>=16:
            print("2")
        else:
            print("-1")
elif s%3 == 2:
    if count_2>0 and s>=5 or count_5>0 and s>=8 or count_8>0 and s>=11:
        print("1")
    else:
        if count_1>1 and s>=5 or count_4>1 and s>=11 or count_7>1 and s>=17 or count_1>0 and count_4>0 and s>=8 or count_7>0 and count_4>0 and s>=14 or count_7>0 and count_1>0 and s>=11:
            print("2")
        else:
            print("-1")
