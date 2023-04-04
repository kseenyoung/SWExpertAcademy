T = int(input())

# 풀이1(runtimeError, 3/10)
# for test in range(1, T+1):
#     n, m = list(map(int, input().split()))
#     board = []
#     result = {}
#
#     for i in range(n):
#         board.append(list(map(int, input().split())))
#
#     for i in range(n):  # rows
#         if board[i].count(1) > 1:
#             count = 0
#             white = False
#             for j in range(n):
#                 if board[i][j] == 1:
#                     count += 1
#                     white = True
#                 elif white == True:
#                     result[count] = 1 if count not in result else result[count] + 1
#                     white = False
#                     count = 0
#                 if j == n-1 and count > 0:
#                     if count != 1:
#                         result[count] = 1 if count not in result else result[count] + 1
#
#     for i in range(n):  # columns
#         count = 0
#         white = False
#         for j in range(n):
#             if board[j][i] == 1:
#                 count += 1
#                 white = True
#             elif white == True:
#                 result[count] = 1 if count not in result else result[count] + 1
#                 white = False
#                 count = 0
#             if j == n - 1 and count > 0:
#                 if count != 1:
#                     result[count] = 1 if count not in result else result[count] + 1
#
#     print("#"+str(test), result[m])


# 풀이2(참고)
for test in range(1, T+1):
    result = 0
    n, k = list(map(int, input().split()))
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):  #rows
        count = 0
        for j in range(n):
            if board[i][j] == 0:
                if count == k:
                    result += 1
                count = 0
                continue
            # board[i][j] == 1
            count += 1
        if count == k:
            result += 1

    for i in range(n):  #cloumns
        count = 0
        for j in range(n):
            if board[j][i] == 0:
                if count == k:
                    result += 1
                count = 0
                continue
            # board[i][j] == 1
            count += 1
        if count == k:
            result += 1

    print("#"+str(test), result)
