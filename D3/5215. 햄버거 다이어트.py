def dfs(vertex, sat, cal):
    global result
    if cal <= L:  # .... 1000이 아니라 .... L ....
        result = sat if sat > result else result
        if vertex < N:
            dfs(vertex+1, sat + igr[vertex][0], cal + igr[vertex][1])
            dfs(vertex+1, sat, cal)

from collections import deque
for test in range(1, int(input())+1):
    result = 0
    N, L = list(map(int, input().split()))
    igr = [list(map(int, input().split())) for _ in range(N)]

    # dfs(0, 0, 0)

    # BFS
    que = deque()
    que.append((0, igr[0][0], igr[0][1]))  # 0번 넣음
    que.append((0, 0, 0))  # 0번 안 넣음

    while que:
        q = que.popleft()
        if q[2] <= L:
            result = max(result, q[1])  # 칼로리 넘지 않으면서 만족도 크면 갱신
            if q[0] < N-1:
                sat, cal = igr[q[0]+1][0], igr[q[0]+1][1]
                que.append((q[0] + 1, q[1] + sat, q[2] + cal))  # 해당 재료 넣음
                que.append((q[0] + 1, q[1], q[2]))  # 해당 재료 안 넣음

    print("#{} {}".format(test, result))
