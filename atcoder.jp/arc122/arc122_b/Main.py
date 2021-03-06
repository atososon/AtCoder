#!/usr/bin/env python3
import sys
import statistics

def solve(N: int, A: "List[int]"):
    s = statistics.median(A)/2
    ans = 0.0
    for i in range(N):
        ans += s + A[i] - min(A[i], 2*s)
    print(ans/N)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
