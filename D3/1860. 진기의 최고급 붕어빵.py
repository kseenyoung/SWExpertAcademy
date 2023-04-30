for test in range(1, int(input()) + 1):
    N, M, K = list(map(int, input().split()))
    times = list(map(int, input().split()))
    times.sort()

    prod = 0
    time = 0

    for i in range(N):  # 아직 사람 있음
        prod += (times[i]//M)*K
        time = times[i]
        if prod < i + 1:
            print("#{} {}".format(test, "Impossible"))
            break
        prod -= 1
    else:
        print("#{} {}".format(test, "Possible"))
