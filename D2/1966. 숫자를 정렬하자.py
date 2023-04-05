T = int(input())
for test in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    print("#"+str(test), ' '.join([str(n) for n in numbers]))