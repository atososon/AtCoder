#!/usr/bin/env python3


# Generated by 2.4.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    h,w,x,y = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0
    temp = 0
    for i in range(h):
        if s[i][y-1] == "#" and i < x-1:
            temp = 0
        elif s[i][y-1] == "#" and i >= x:
            break
        elif s[i][y-1] == ".":
            temp += 1
    ans += temp
    temp = 0
    for i in range(w):
        if s[x-1][i] == "#" and i < y-1:
            temp = 0
        elif s[x-1][i] == "#" and i >= y:
            break
        elif s[x-1][i] == ".":
            temp += 1
    ans += temp
    if s[x-1][y-1] == ".":
        ans -= 1
    print(ans)
            

if __name__ == '__main__':
    main()
