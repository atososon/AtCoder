#!/usr/bin/env python3
import sys


def solve(H: int, W: int, R: int, C: int):
    ans = 0
    for i in range(1, H+1):
        for j in range(1, W+1):
            if abs(i-R) + abs(j-C) == 1:
                ans += 1
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(H, W, R, C)


if __name__ == '__main__':
    main()
