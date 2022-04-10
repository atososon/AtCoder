from collections import deque


def main():
    deq = deque()
    n = int(input())
    for _ in range(n):
        q = input().split()
        if q[0] == "1":
            deq.append([int(q[2]), int(q[1])])
        else:
            count = 0
            ans = 0
            while count < int(q[1]):
                p = deq.popleft()
                if count + p[0] <= int(q[1]):
                    ans += p[0] * p[1]
                else:
                    ans += abs(int(q[1]) - count) * p[1]
                    deq.appendleft(
                        [abs(count + p[0] - int(q[1])), p[1]])
                count += p[0]
            print(ans)


if __name__ == '__main__':
    main()
