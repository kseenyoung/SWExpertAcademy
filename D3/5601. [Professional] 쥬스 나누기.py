T = int(input())
for test in range(1, T+1):
    n = int(input())
    result = ('1/'+str(n)+' ')*n

    print("#"+str(test), result)