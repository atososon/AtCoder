#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    ans = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            ans += 100*i+j
    print(ans)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
