T = int(input())
charges = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for test in range(1, T+1):
    n = int(input())
    result = ''
    charge = 50000

    for i in range(8):
        result += str(n // charges[i]) + " "
        n %= charges[i]

    print("#"+str(test), '\n', result)