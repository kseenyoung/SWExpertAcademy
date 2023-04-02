T = int(input())
divide = [2, 3, 5, 7, 11]
for test_case in range(1, T + 1):
    n = int(input())
    result = ''
    print("#" + str(test_case), end=' ')

    for d in divide:
        count = 0
        while n % d == 0:
            count += 1
            n //= d
        result += str(count) + ' '
    print(result)