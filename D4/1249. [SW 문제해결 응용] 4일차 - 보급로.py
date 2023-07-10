import heapq

T = int(input())
INF = 1e9

for test_case in range(1, T+1):
    N = int(input())
    check = [[INF]*N for _ in range(N)]
    board = []
    que = []

    for _ in range(N):
        temp = []
        for i in input():
            temp.append(int(i))
        board.append(temp)

    heapq.heappush(que, (board[0][0], 0, 0))
    check[0][0] = board[0][0]

    while que:
        q = heapq.heappop(que)
        cost, row, col = q
        # print(cost, row, col)
        if row == N-1 and col == N-1:
            print("#{} {}".format(test_case, check[row][col]))
        if cost <= check[row][col]:
            for rx, cx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r = row + rx
                c = col + cx
                if -1 < r < N and -1 < c < N and cost + board[r][c] < check[r][c]:
                    check[r][c] = cost + board[r][c]
                    heapq.heappush(que, (check[r][c], r, c))


    # print("#{} {}".format(test_case, 1))
