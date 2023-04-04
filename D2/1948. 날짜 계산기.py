T = int(input())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test in range(1, T+1):
    m1, d1, m2, d2 = list(map(int, input().split()))
    result = sum(month[m1:m2]) + d2 - d1 + 1

    print("#"+str(test), result)