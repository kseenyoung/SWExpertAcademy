T = int(input())
for test in range(1, T+1):
    P, Q, R, S, W = list(map(int, input().split()))
    result = min(W*P, Q + (W-R)*S if W > R else Q)  # min(A, B)

    print("#"+str(test), result)
