from collections import deque
T = int(input())

direction = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]

for test_case in range(1, T+1):
    n = int(input())
    board = []
    answer = 0
    que = deque()
    for i in range(n):
        board.append([i for i in input()])


    def cntbomb(r, c):  # 주변 8칸 폭탄 개수 확인
        cnt = 0
        for dr, dc in direction:
            row, col = r+dr, c+dc
            if -1<row<n and -1<col<n and board[row][col] == '*':
                cnt += 1
        return cnt

    # def dfs(r, c):  # 주변에 폭탄이 없을 때(0일 때) 주변 확인
    #     for dr, dc in direction:
    #         row, col = r+dr, c+dc
    #         if -1<row<n and -1<col<n and  board[row][col] == '.':
    #             cnt = cntbomb(row, col)
    #             if cnt == 0:
    #                 board[row][col] = 0
    #                 dfs(row, col)
    #             else: board[row][col] = cnt

    # 1차 순회
    for r in range(n):
        for c in range(n):
            if board[r][c] == '.':
                cnt = cntbomb(r, c)
                if cnt == 0:
                    que.append((r, c))
                    board[r][c] = 0
                    answer += 1

                    while que:
                        r2, c2 = que.popleft()
                        temp = cntbomb(r2, c2)


                        for dr, dc in direction:
                            row, col = r2+dr, c2+dc
                            if -1 < row < n and -1 < col < n and board[row][col] == '.':
                                temp2 = cntbomb(row, col)
                                board[row][col] = temp2
                                if temp2 == 0:
                                    que.append((row, col))
                        board[r2][c2] = temp


    # for r in range(n):
    #     for c in range(n):
    #         if board[r][c] == '.':
    #             answer += 1
    #             cnt = cntbomb(r, c)
    #             if cnt == 0:
    #                 que.append((r, c))
    #                 while que:
    #                     row, col = que.popleft()
    #                     board[row][col] = cntbomb(row, col)
    #                     for r2, c2 in direction:
    #                         row2, col2 = row+r2, col+c2
    #                         if -1 < row2 < n and -1 < col2 < n and board[row2][col2] == '.':
    #                             temp = cntbomb(row2, col2)
    #                             if temp == 0:
    #                                 que.append((row2, col2))
    #                             board[row2][col2] = temp
    #             else:
    #                 board[r][c] = cnt
    for i in range(n):
        answer += board[i].count('.')

    print("#{} {}".format(test_case, answer))
