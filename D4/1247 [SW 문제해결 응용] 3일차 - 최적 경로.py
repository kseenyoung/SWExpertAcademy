import heapq
T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    points = list(map(int, input().split()))
    graph = [[] for _ in range(n+2)]
    checked = [False]*(n+2)
    answer = 1e9

    for i in range(0, len(points), 2):
        for j in range(i+2, len(points), 2):
            if i == 0 and j == 2:
                continue
            graph[i//2].append((abs(points[i]-points[j]) + abs(points[i+1]-points[j+1]), j//2))
            graph[j//2].append((abs(points[i]-points[j]) + abs(points[i+1]-points[j+1]), i//2))

    def dfs(vertex, sum, level):
        global answer
        if answer < sum:
            return
        if level != n+1 and vertex == 1:  # 마지막 노드 아닌데 1인 경우
            return
        if not checked[vertex]:
            if level == n+1 and vertex == 1:
                answer = min(answer, sum)
                return

            for w, v in graph[vertex]:
                checked[vertex] = True
                dfs(v, sum+w, level+1)
                checked[vertex] = False
    dfs(0, 0, 0)


    print("#{} {}".format(test_case, answer))
