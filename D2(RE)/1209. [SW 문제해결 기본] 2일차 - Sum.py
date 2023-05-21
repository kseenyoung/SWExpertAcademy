for test in range(1, 11):
    test = int(input())
    board = []

    for _ in range(100):
        board.append(list(map(int, input().split())))

    result = 0
    column = [0]*100
    right, left = 0, 0
    for i in range(100):
        row = 0
        for j in range(100):
            column[j] += board[i][j]
            row += board[i][j]
            if i == j:
                right += board[i][j]
            if i + j == 99:
                left += board[i][j]
        result = max(result, row)

    for i in range(100):
        result = max(result, column[i])
    print("right, left", right, left)
    result = max(result, right, left)

    print("#{} {}".format(test, result))