T = int(input())
for test in range(1, T+1):
    U, L, X = list(map(int, input().split()))
    result = 0 if U <= X <= L else U - X if X < U else -1
    print("#"+str(test), result)