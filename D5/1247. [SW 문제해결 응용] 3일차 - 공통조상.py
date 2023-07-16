import copy
from collections import deque
T = int(input())

for test_case in range(1, T+1):
    V, E, a, b = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    parents = [[] for _ in range(V+1)]
    numbers = list(map(int, input().split()))

    for i in range(0, len(numbers), 2):
        graph[numbers[i]].append(numbers[i+1])

    def dfs(parent, vertex):
        parents[vertex] = copy.deepcopy(parent)
        for v in graph[vertex]:
            parent.append(vertex)
            dfs(parent, v)
            parent.pop()

    dfs([], 1)

    # a, b의 부모 찾기
    minv, maxv = min(a, b), max(a, b)
    flag = False
    for i in range(len(parents[minv])-1, -1, -1):
        for j in range(len(parents[maxv])-1, -1, -1):
            if parents[minv][i] == parents[maxv][j]:
                temp = parents[minv][i]
                flag = True
                break
        if flag:
            break

    # subtree 크기 구하기
    size = 0
    que = deque()
    que.append(temp)
    while que:
        q = que.popleft()
        size += 1
        if len(graph[q]) != 0:
            for v in graph[q]:
                que.append(v)

    print("#{} {} {}".format(test_case, temp, size))
