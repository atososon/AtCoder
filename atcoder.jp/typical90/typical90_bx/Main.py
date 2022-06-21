#!/usr/bin/env python3
import sys
from collections import deque

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: "List[int]"):
    all_size = sum(A)
    if all_size % 10 != 0:
        print(NO)
        return
    double_A = A + A
    q = deque([double_A[0]])
    one_tenth = all_size // 10
    q_sum = double_A[0]
    i = 1
    while True:
        if q_sum == one_tenth:
            print(YES)
            return
        elif q_sum > one_tenth:
            q_sum -= q.popleft()
        else:
            q.append(double_A[i])
            q_sum += double_A[i]
            i += 1
        if i >= 2*N-1:
            break
    print(NO)
    return


# Generated by 2.5.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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