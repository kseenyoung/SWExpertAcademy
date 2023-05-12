def find(target):
    start = 1

    for i in range(1, target+1):
        if start <= target <= start+i:
            y = i
            x = 1
            while target != start:
                start += 1
                y -= 1
                x += 1
            return x, y
        start += i


for test in range(1, int(input())+1):  # (973/1000)
    p, q = list(map(int, input().split()))
    result = 0

    newx, newy = zip(find(p), find(q))
    newx, newy = sum(newx), sum(newy)
    for i in range(1, newx+newy-1):
        result += i
    print("#{} {}".format(test, result+newx))

