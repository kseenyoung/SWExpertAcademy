T = int(input())
for test in range(1, T+1):
    N = 0
    m = n = int(input())
    check = [False]*10  # 0-9 발견 여부
    while False in check:  # 모두 발견할 때 까지 반복
        for i in str(m):
            check[int(i)] = True
        N += 1
        m = n*N

    print("#"+str(test), (N-1)*n)
