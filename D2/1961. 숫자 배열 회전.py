T = int(input())
for test in range(1, T+1):
    print("#"+str(test))
    n = int(input())
    result = [['']*n for _ in range(n)]
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        t90 = ''
        t180 = ''
        t270 = ''
        # 90
        for j in reversed(range(n)):
            t90 += str(board[j][i])
            t180 += str(board[n-i-1][j])
            t270 += str(board[n-j-1][n-i-1])
        # 270

        result[i][0] += t90
        result[i][1] += t180
        result[i][2] += t270

    for i in range(n):
        print(' '.join(result[i]))