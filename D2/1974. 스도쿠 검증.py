T = int(input())
for test in range(1, T+1):
    print("#"+str(test), end=" ")
    board = []
    checkRow = [False]*9
    checkCol = [False]*9
    checkBox = [False]*9
    for _ in range(9):
        board.append(list(map(int, input().split())))

    for i in range(9):
        for j in range(9):
            checkRow[board[i][j]-1] = True  # row
            checkCol[board[j][i]-1] = True  # colum
        if False in checkRow or False in checkCol:
            print(0)
            break
        checkRow = [False] * 9
        checkCol = [False] * 9
    else:
        temp = False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        checkBox[board[i+k][j+l]-1] = True
                if False in checkBox:
                    print(0)
                    temp = True
                    break
                checkBox = [False] * 9
            if temp:
                break
        else:
            print(1)