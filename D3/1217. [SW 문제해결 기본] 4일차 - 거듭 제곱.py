for _ in range(10):
    n = int(input())
    a, b = list(map(int, input().split()))

    print("#"+str(n), a**b)
