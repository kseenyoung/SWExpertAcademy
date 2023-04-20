for test in range(1, int(input())+1):
    n = int(input())
    board = []
    result = 0
    for i in range(n):
        board.append(list(int(i) for i in input()))

    a, b = n//2, 1  # 각 행의 어느 위치(a)에서 얼만큼(b)
    for i in range(n):  # 행
        result += sum(board[i][a:a+b])
        if i < n//2:
            a -= 1
            b += 2
        else:
            a += 1
            b -= 2

    print("#{} {}".format(test, result))
