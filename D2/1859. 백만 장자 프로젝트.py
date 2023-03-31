# 풀이1(9/10)
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    line = list(map(int, input().split()))
    count = 0
    result = 0
    maxNum = max(line)

    for i, l in enumerate(line):
        if l < maxNum:
            count += 1
            result -= l
        elif i < n-1 and maxNum == l:
            maxNum = max(line[i+1:])
            result += count*l
            count = 0
        if i == n-1: # 마지막 원소
            result += count*l

    print("#"+str(test_case), result)


# 풀이2(참고)
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    line = list(map(int, input().split()))[::-1]
    result = 0
    maxNum = line[0]

    for i in range(n):
        if line[i] <= maxNum:
            result += maxNum - line[i]
        else:
            maxNum = line[i]
        print(result)

    print("#"+str(test_case), result)
