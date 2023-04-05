T = int(input())
for test in range(1, T+1):
    n = int(input())
    speed = 0
    distance = 0
    for i in range(n):
        alist = list(map(int, input().split()))
        if alist[0] == 0:  # 속도 유지
            distance += speed
        elif alist[0] == 1:  # 가속
            speed += alist[1]
            distance += speed
        elif alist[0] == 2:  # 감속
            speed -= alist[1]
            if speed < 0: speed = 0
            distance += speed

    print("#"+str(test), distance)