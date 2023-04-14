# import numpy

def checkPal(string):
    stringLen = len(string)
    for i in range(stringLen // 2):
        if string[i] != string[stringLen - i - 1]:
            return False
    else:
        return True

T = int(input())
for test in range(1, T+1):
    a, b = list(map(int, input().split()))
    result = 0
    for i in range(a, b+1):
        if checkPal(str(i)):
            # a1, a2 = numpy.modf(int(i)**0.5)  # 소수, 정수 분리
            a2 = int(i)**0.5
            a1 = a2 - int(a2)

            if a1 == 0.0 and checkPal(str(int(a2))):
                result += 1
    print("#"+str(test), result)