from collections import deque

for test in range(1, int(input())+1):
    result = 0
    que = deque()
    N, K = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    que.append((1, numbers[0]))
    que.append((1, 0))
    while que:
        q = que.popleft()
        if q[0] == N:
            if q[1] == K:
                result += 1
        else:
            que.append((q[0]+1, q[1] + numbers[q[0]]))
            que.append((q[0]+1, q[1]))

    print('#{} {}'.format(test, result))
