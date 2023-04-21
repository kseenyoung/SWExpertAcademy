def promising(row):
    for i in range(row):
        if column[row] == column[i] or row - i == abs(column[row] - column[i]):
            # 퀸이 같은 대각선 또는 열에 존재한다면 탐색 중지
            return False
    return True


def dfs(row):
    global result
    if row == n:  # n 번째 행 퀸까지 결정 됐다면
        result += 1
    else:
        for col in range(n):  # row 행의 어느 열
            column[row] = col  # 퀸 배치
            if promising(row):  # (Backtracking) 더 탐색할지 결정
                dfs(row+1)


for test in range(1, int(input())+1):
    n = int(input())  # n * n 보드
    column = [-1]*n  # i번째 행에 위치한 퀸의 열 위치
    result = 0

    dfs(0)

    print("#{} {}".format(test, result))
