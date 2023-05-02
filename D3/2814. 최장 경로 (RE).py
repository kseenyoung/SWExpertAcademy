def dfs(vertex, depth):
    global result
    if depth > result:
        result = depth
    for vert in vertexes[vertex]:
        if not visited[vert]:
            visited[vert] = True
            dfs(vert, depth+1)
            visited[vert] = False


for test in range(1, int(input())+1):
    result = 0
    N, M = list(map(int, input().split()))
    vertexes = [[] for _ in range(N+1)]
    visited = [False]*(N+1)

    for i in range(M):
        start, end = list(map(int, input().split()))
        vertexes[start].append(end)
        vertexes[end].append(start)

    for vertex in range(1, N+1):
        visited[vertex] = True
        dfs(vertex, 1)
        visited[vertex] = False

    print("#{} {}".format(test, result))