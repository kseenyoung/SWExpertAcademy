T = int(input())

for test in range(1, T+1):
    bits = input()  # input().split() 아님
    currBits = [0]*len(bits)
    result = 0

    for i, bit in enumerate(bits):
        if int(bit) != currBits[i]:
            currBits[i:] = [int(bit)]*(len(bits)-i)
            result += 1

    print("#"+str(test), result)


