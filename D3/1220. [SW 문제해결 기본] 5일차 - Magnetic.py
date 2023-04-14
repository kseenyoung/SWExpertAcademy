for test in range(1, 11):
    n = int(input())  # 100
    result = 0
    board = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    print("#"+str(test), result)
