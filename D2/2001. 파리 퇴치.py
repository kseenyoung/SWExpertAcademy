T = int(input())
for test in range(1, T+1):
    result = 0
    n, m = list(map(int, input().split()))
    board = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for k in range(m):
                # print(board[i+k][j:j+m])
                temp += sum(board[i+k][j:j+m])

            result = max(result, temp)

    print("#"+str(test), result)