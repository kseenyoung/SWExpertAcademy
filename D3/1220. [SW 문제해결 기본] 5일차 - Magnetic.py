for test in range(1, 11):
    n = int(input())  # 100
    result = 0
    column = [0]*100

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(100):
            if column[j] == 1 and line[j] == 2:  # 이전에 N, 지금 S
                result += 1
            if line[j] != 0:
                column[j] = line[j]
    #print(column)
    print("#"+str(test), result)
