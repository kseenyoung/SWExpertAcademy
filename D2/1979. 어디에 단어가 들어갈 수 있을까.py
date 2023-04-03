T = int(input())

for test in range(1, T+1):
    n, m = list(map(int, input().split()))
    board = []
    result = {}
    result1 = {}

    for i in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):  #rows
        if board[i].count(1) > 1:
            count = 0
            white = False
            for j in range(n):
                if board[i][j] == 1:
                    count += 1
                    white = True
                elif white == True:
                    result[count] = 1 if count not in result else result[count] + 1
                    white = False
                    count = 0
                if j == n-1 and count > 0:
                    if count != 1:
                        result[count] = 1 if count not in result else result[count] + 1

    for i in range(n):  #columns
        count = 0
        white = False
        for j in range(n):
            if board[j][i] == 1:
                count += 1
                white = True
            elif white == True:
                result[count] = 1 if count not in result else result[count] + 1
                white = False
                count = 0
            if j == n - 1 and count > 0:
                if count != 1:
                    result[count] = 1 if count not in result else result[count] + 1

    print("#"+str(test), result[m])
