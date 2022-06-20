#!/usr/bin/env python3
import sys


def solve(R: int, C: int, A: "List[List[int]]"):
    print(A[R-1][C-1])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(2)]
         for _ in range(2)]  # type: "List[List[int]]"
    solve(R, C, A)


if __name__ == '__main__':
    main()
