T = int(input())
for test in range(1, T+1):
    print("#"+str(test))

    doc = ''
    n = int(input())
    for i in range(n):
        d, count = input().split()
        doc += d*int(count)

    for i in range(0, len(doc), 10):
        print(doc[i:i+10])



