dr = [0, 1, 0, -1]  # right, down, left up
dc = [1, 0, -1, 0]

for test in range(1, int(input())+1):
    n = int(input())
    board = [[0]*n for _ in range(n)]
    dir = 0
    row, col = 0, 0
    board[0][0] = 1

    for num in range(2, n*n+1):
        r = row + dr[dir]
        c = col + dc[dir]
        if 0 > r or r >= n or 0 > c or c >= n or board[r][c]:
            dir = dir + 1 if dir < 3 else 0
        row += dr[dir]
        col += dc[dir]
        board[row][col] = num

    print("#" + str(test))
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()