def promising(i):  # 해당 위치에 놓아도 되는지 판단
    for j in range(i):  # i(row)기준, 이미 배치된 이전 row만 확인하면 됨
        if abs(i-j) == abs(column[i] - column[j]) or column[i] == column[j]:  # 같은 대각선(same diagonal)이나 열에 위치함
            return False
    return True


def dfs(count):
    global result
    if count == n:
        result += 1
        return
    for i in range(n):  # 행 별로 구하기
        column[count] = i  # count 행 i 열에 배치
        if promising(count):  # 아직 배치 안된 열(count), not i
            dfs(count + 1)


for test in range(1, int(input())+1):
    result = 0
    n = int(input())
    column = [0]*n  # 해당하는 index(row)에 위치한 column 값을 저장, 0이라면 배치되지 않음

    dfs(0)
    print("#{} {}".format(test, result))
