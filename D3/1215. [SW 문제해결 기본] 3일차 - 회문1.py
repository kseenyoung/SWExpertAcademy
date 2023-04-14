for n in range(1, 11):
    test = int(input())
    result = 0
    board = []

    for _ in range(8):
        board.append(list(input()))

    for i in range(8):  # row
        for j in range(8-test+1):
            for k in range(test//2):
                if board[i][j+k] != board[i][j+test-k-1]:
                    break
            else:
                result += 1

    for j in range(8):  # column
        for i in range(8-test+1):
            for k in range(test//2):
                if board[i+k][j] != board[i+test-k-1][j]:
                    break
            else:
                # print([a[j] for a in board[i:i+4]])
                result += 1

    print("#"+str(n), result)
