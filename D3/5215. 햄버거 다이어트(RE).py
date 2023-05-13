def dfs(num, kcal, grad):
    global result
    if num == N:
        if kcal <= L:
            result = grad if grad > result else result
    else:
        if kcal < L:
            dfs(num+1, kcal+cal[num], grad+ing[num])
            dfs(num+1, kcal, grad)

for test in range(1, int(input())+1):
    N, L = list(map(int, input().split()))
    ing = [0]*N
    cal = [0]*N
    result = 0

    for j in range(N):
        i, c = list(map(int, input().split()))
        ing[j] = i
        cal[j] = c

    dfs(0, 0, 0)

    print("#{} {}".format(test, result))
