T = int(input())
for test in range(1, T+1):
    print("#"+str(test))
    n = int(input())
    board = [[0]*n for _ in range(n)]
    i, j = 0, 0
    direction = 0
    dix = [1, 0, -1, 0]  # R D L U
    diy = [0, 1, 0, -1]

    for k in range(1, n*n+1):
        board[i][j] = str(k) + ' '
        i += diy[direction]
        j += dix[direction]
        if i == n or j == n or board[i][j] != 0:
            i -= diy[direction]
            j -= dix[direction]
            direction = (direction + 1) % 4  # 방향 전환
            i += diy[direction]
            j += dix[direction]

    for b in board:
        print(''.join(b))
