for test in range(1, 11):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 100

    for i in range(N+1):  # 덤프를 추가로 수행케 함으로 평탄화 후 min, max의 차이를 반환해야 함
        maxN = max(numbers)
        minN = min(numbers)
        if maxN == minN or (maxN - minN == result and maxN - minN == 1):
            result = maxN - minN
            break
        numbers[numbers.index(maxN)] -= 1
        numbers[numbers.index(minN)] += 1
        result = maxN - minN

    print("#{} {}".format(test, result))
