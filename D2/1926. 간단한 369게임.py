n = int(input())
check = ['3', '6', '9']
result = ''

for i in range(1, n+1):
    number = str(i)
    count = 0
    for n in number:
        if n in check:
            count += 1
    if count:
        result += '-'*count + ' '
    else:
        result += number + ' '

print(result)