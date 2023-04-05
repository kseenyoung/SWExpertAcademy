T = int(input())
for test in range(1, T+1):
    # hours = minutes = 0
    h1, m1, h2, m2 = list(map(int, input().split()))
    h1 += h2
    m1 += m2

    h1 += m1//60
    m1 %= 60

    h1 = h1 if h1 <= 12 else h1 % 12

    print("#"+str(test), h1, m1)
