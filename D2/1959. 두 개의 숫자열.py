T = int(input())
for test in range(1, T+1):
    result = 0
    n, m = list(map(int, input().split()))
    j = []
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    #len(j[0]) < len(j[1])
    if n < m:
        j.append(Aj)
        j.append(Bj)
    else:
        j.append(Bj)
        j.append(Aj)

    for i in range(0, max(n, m)-min(n, m)+1):  # 큰 수
        temp = []  #j[1] -> j[1][:] (주의)리스트 복사시 포인터 복사함,,,,,

        for k in range(min(n, m)):  # 작은 수
            temp.append(j[1][i+k] * j[0][k])
        result = max(result, sum(temp))

    print("#"+str(test), result)
