T = int(input())
for test in range(1, T+1):
    string = input()
    result = 1
    for i, s in enumerate(string[::-1]):
        if s != string[i]:
            result = 0

    print("#"+str(test), result)
