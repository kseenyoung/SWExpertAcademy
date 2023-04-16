for test in range(1, 11):
    result = 0
    n = int(input())
    buildings = list(map(int, input().split()))

    for i in range(2, n-2):
        sideMax = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])  # 양 옆 2빌딩 중 큰 값
        if buildings[i] - sideMax > 0:  # 확보 가능 조망권 있음
            result += buildings[i] - sideMax

    print("#"+str(test), result)
