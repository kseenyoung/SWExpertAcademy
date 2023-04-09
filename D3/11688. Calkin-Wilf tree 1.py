T = int(input())
for test in range(1, T+1):
    result = 0
    a, b = 1, 1
    move = input()

    for m in move:
        if m == 'R':
            a = a+b
        else:
            b = a+b

    print("#"+str(test), a, b)
