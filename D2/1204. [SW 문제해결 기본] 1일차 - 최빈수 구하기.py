from collections import Counter
T = int(input())
for test in range(1, T+1):
    n = int(input())
    result = 0
    alist = list(map(int, input().split()))
    counter = Counter(alist)

    print("#"+str(n), counter.most_common()[0][0])