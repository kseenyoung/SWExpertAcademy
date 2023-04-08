T = int(input())
check = ['a', 'e', 'i', 'o', 'i']
for test in range(1, T+1):
    result = input()
    for c in check:
        result = result.replace(c, "")
    print("#"+str(test), result)
