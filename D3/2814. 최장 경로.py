# BFS 풀이(불가능)
# from collections import deque
#
# for test in range(1, int(input())+1):
#     result = 0
#     N, M = list(map(int, input().split()))
#     vertexes = [[] for _ in range(N+1)]
#
#     que = deque()
#
#     for i in range(M):
#         start, end = list(map(int, input().split()))
#         vertexes[start].append(end)
#         vertexes[end].append(start)
#
#     for i in range(1, N+1):
#         que.append((i, 1))  # 정점, 노드
#         visited = [False] * (N + 1)
#
#         while que:
#             q = que.popleft()
#             if q[1] > result: result = q[1]
#             visited[q[0]] = True
#             for v in vertexes[q[0]]:
#                 if not visited[v]:
#                     que.append((v, q[1]+1))
#
#     print("#{} {}".format(test, result))


# DFS 풀이
def dfs(vert, depth):
    global result
    if depth > result: result = depth
    for v in vertexes[vert]:
        if not visited[v]:
            visited[vert] = True
            dfs(v, depth+1)
            visited[vert] = False


for test in range(1, int(input())+1):
    N, M = list(map(int, input().split()))
    vertexes = [[] for _ in range(N+1)]
    result = 0

    for i in range(M):
        start, end = list(map(int, input().split()))
        vertexes[start].append(end)
        vertexes[end].append(start)

    for vertex in range(1, N+1):
        visited = [False]*(N+1)
        visited[vertex] = True
        dfs(vertex, 1)

    print("#{} {}".format(test, result))
