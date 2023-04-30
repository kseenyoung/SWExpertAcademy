for test in range(1, int(input()) + 1):
    N, M, K = list(map(int, input().split()))
    times = list(map(int, input().split()))
    times.sort()  # 먼저 오는 손님 정렬

    for i in range(N):  # 아직 사람 있음
        prod = (times[i]//M)*K  # 해당 시간까지 만들 수 있는 붕어빵
        if prod < i + 1:  # 몇 번째 손님
            print("#{} {}".format(test, "Impossible"))
            break
    else:
        print("#{} {}".format(test, "Possible"))
