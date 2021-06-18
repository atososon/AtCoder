#!/usr/bin/env python3
import sys
import bisect
import copy

def solve(N: int, Q: int, A: "List[int]", K: "List[int]"):
    a = copy.copy(A)
    a[0] = A[0] - 1
    for i in range(1, N):
        a[i] = a[i-1] + A[i] - A[i-1] - 1
            
    for i in range(Q):
        f = bisect.bisect_left(a, K[i])
        ans = K[i] + f
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
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    K = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, A, K)

if __name__ == '__main__':
    main()