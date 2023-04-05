T = int(input())
for test in range(1, T+1):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    board[0][0] = 1

    for i in range(1, n):
        for j in range(i+1):
            board[i][j] = 1 if j == 0 or j == i else board[i-1][j-1] + board[i-1][j]

    print("#"+str(test))
    for i in range(n):
        result = ''
        for j in range(i+1):
            result += str(board[i][j]) + " "
        print(result)
