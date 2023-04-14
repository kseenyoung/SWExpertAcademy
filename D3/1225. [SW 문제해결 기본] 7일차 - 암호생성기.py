for _ in range(1, 11):
    test = int(input())
    minus = 1
    numbers = list(map(int, input().split()))
    while numbers[-1] > 0:
        numbers.append(numbers.pop(0) - minus)
        minus = minus + 1 if minus < 5 else 1

    numbers[-1] = 0
    print("#"+str(test), ' '.join([str(n) for n in numbers]))
