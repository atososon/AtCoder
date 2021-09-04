#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(a, s):
    ans = NO
    if 2*a <= s:
        differ = s-2*a
        if ((differ & a) == 0):
            ans = YES
    print(ans)

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)


def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        solve(a, s)


if __name__ == '__main__':
    main()