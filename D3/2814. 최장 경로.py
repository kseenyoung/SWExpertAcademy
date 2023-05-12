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
    if depth > result: result = depth  # 지금까지 경로보다 길다면
    for v in vertexes[vert]:  # 해당 정점에 대해 연결된 모든 정점 탐색
        if not visited[v]:  # 아직 방문되지 않았다면
            visited[vert] = True  # 방문 표시
            dfs(v, depth+1)
            visited[vert] = False  # 방문 해제


for test in range(1, int(input())+1):
    N, M = list(map(int, input().split()))
    vertexes = [[] for _ in range(N+1)]
    result = 0

    for i in range(M):  # 모든 간선을 인접 리스트화(무방향이므로 두 정점 각각 연결)
        start, end = list(map(int, input().split()))
        vertexes[start].append(end)
        vertexes[end].append(start)

    visited = [False]*(N+1)  # 방문한 정점 표시
    for vertex in range(1, N+1):  # 처음 방문할 정점 선택
        visited[vertex] = True
        dfs(vertex, 1)

    print("#{} {}".format(test, result))
