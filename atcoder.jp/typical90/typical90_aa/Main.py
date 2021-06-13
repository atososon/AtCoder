#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]"):
    b = set()
    for i in range(N):
        if S[i] in b:
            continue
        else:
            print(i+1)
            b.add(S[i])
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()