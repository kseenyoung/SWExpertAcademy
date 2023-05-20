n = int(input())
result = ''

for i in range(1, n+1):
    number = str(i)
    cnt = 0
    flag = False
    for num in number:
        if num in ['3', '6', '9']:
            cnt += 1
            flag = True
    if flag:
        result += '-'*cnt + " "
    else:
        result += number + " "

print(result)