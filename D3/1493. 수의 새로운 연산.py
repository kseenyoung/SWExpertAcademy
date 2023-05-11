numbers = [[] for _ in range(10000)]
n = 1
for row in range(10000):
    for column in range(0, row+1):
        numbers[row].append(n)
        n += 1
# print(numbers)

for test in range(1, int(input())+1):
    p, q = list(map(int, input().split()))

    print(numbers[q-1][p-1])

