T = int(input())
for test in range(1, T+1):
    n = int(input())
    alist = list(map(int, input().split()))
    average = sum(alist) // n
    print("#"+str(test), len([i for i in alist if i <= average]))