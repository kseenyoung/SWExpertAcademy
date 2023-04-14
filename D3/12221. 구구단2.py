T = int(input())
for test in range(1, T+1):
    a, b = list(map(int, input().split()))
    if a > 9 or b > 9:
        print("#"+str(test), -1)
    else:
        print("#"+str(test), a*b)