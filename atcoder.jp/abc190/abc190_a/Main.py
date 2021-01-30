a, b, c = map(int, input().split())
if a < b:
    print("Aoki")
elif a > b:
    print("Takahashi")
elif a == b and c == 0:
    print("Aoki")
else:
    print("Takahashi")