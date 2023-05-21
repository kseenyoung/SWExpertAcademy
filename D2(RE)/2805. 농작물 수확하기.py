for test in range(1, int(input())+1):
    n = int(input())
    ground = []
    for _ in range(n):
        string = input()
        temp = [int(i) for i in string]
        ground.append(temp)

    cnt = 1
    position = n//2
    result = 0
    for i in range(n):
        if n//2 > i:
            print(ground[i][position:position+cnt])
            result += sum(ground[i][position:position+cnt])
            cnt += 2
            position -= 1
        else:
            print(ground[i][position:position+cnt])
            result += sum(ground[i][position:position+cnt])
            cnt -= 2
            position += 1

    print("#{} {}".format(test, result))