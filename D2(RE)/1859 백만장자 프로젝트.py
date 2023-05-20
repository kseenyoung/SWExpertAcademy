for test in range(1, int(input())+1):
    n = int(input())
    result = 0
    numbers = list(map(int, input().split()))
    count = 0

    for i in range(len(numbers)):
        flag = False
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                flag = True
                break
        if flag:
            result -= numbers[i]
            count += 1
        else:
            result += count * numbers[i]
            count = 0

    print("#{} {}".format(test, result))
