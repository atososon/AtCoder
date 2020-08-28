import numpy as np
w = input()
abc = np.zeros(26,dtype=int)
for i in range(len(w)):
    if w[i] == "a":
        abc[0] += 1
    if w[i] == "b":
        abc[1] += 1
    if w[i] == "c":
        abc[2] += 1
    if w[i] == "d":
        abc[3] += 1
    if w[i] == "e":
        abc[4] += 1
    if w[i] == "f":
        abc[5] += 1
    if w[i] == "g":
        abc[6] += 1
    if w[i] == "h":
        abc[7] += 1
    if w[i] == "i":
        abc[8] += 1
    if w[i] == "j":
        abc[9] += 1
    if w[i] == "k":
        abc[10] += 1
    if w[i] == "l":
        abc[11] += 1
    if w[i] == "m":
        abc[12] += 1
    if w[i] == "n":
        abc[13] += 1
    if w[i] == "o":
        abc[14] += 1
    if w[i] == "p":
        abc[15] += 1
    if w[i] == "q":
        abc[16] += 1
    if w[i] == "r":
        abc[17] += 1
    if w[i] == "s":
        abc[18] += 1
    if w[i] == "t":
        abc[19] += 1
    if w[i] == "u":
        abc[20] += 1
    if w[i] == "v":
        abc[21] += 1
    if w[i] == "w":
        abc[22] += 1
    if w[i] == "x":
        abc[23] += 1
    if w[i] == "y":
        abc[24] += 1
    if w[i] == "z":
        abc[25] += 1
ans = 0
for i in range(26):
    if abc[i]%2 != 0:
        ans = 1
if ans == 0:
    print("Yes")
else:
    print("No")