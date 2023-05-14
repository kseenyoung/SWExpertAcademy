# 풀이 참고
dr = [1, 0, 1, 1]  # 아래, 오른쪽, 좌 대각선, 우 대각선
dc = [0, 1, -1, 1]


def omok():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'o':
                for d in range(4):
                    row = i
                    col = j
                    cnt = 0

                    while -1 < row < n and -1 < col < n and board[row][col] == 'o':
                        cnt += 1
                        row += dr[d]
                        col += dc[d]
                    if cnt >= 5:
                        return "YES"
    return "NO"


for test in range(1, int(input())+1):
    n = int(input())
    board = [input() for _ in range(n)]
    result = "NO"

    result = omok()

    # 내 풀이(실패)
    # for i, row in enumerate(board):
    #     for j in range(n):
    #         if board[i][j] == 'o':
    #             if j < n-4 and board[i][j:j+5] == "ooooo":  # 가로
    #                 result = "YES"
    #                 break
    #             if i < n-4:
    #                 for k in range(i, i+5):  # 세로
    #                     if board[k][j] != 'o':
    #                         break
    #                 else:
    #                     result = "YES"
    #                     break
    #                 if j < n-4:
    #                     for k in range(i, i+5):  # 우대각
    #                         if board[k][j+k] != 'o':
    #                             break
    #                     else:
    #                         result = "YES"
    #                         break
    #                 if j >= 4:
    #                     for k in range(i, i+5):  # 좌대각
    #                         if board[k][j-k] != 'o':
    #                             break
    #                     else:
    #                         result = "YES"
    #                         break

    print("#{} {}".format(test, result))
