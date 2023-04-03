T = int(input())
for test in range(1, T+1):
    string = input()
    count = 0
    temp = string[0]
    for i, s in enumerate(string):
        if i != 0 and s == string[0] and string[i:i+count] == string[:i]:  # 반복 발견
            break
        else:
            temp += s
            count += 1

    print("#"+str(test), count)
