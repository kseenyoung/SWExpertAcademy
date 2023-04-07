T = int(input())
for test in range(1, T+1):
    a, b = list(map(int, input().split()))
    print("#"+str(test), a + b if a + b < 24 else (a+b)%24)