# 내 풀이( 15 중 7)
# T = int(input())
#
# for test in range(1, T+1):
#     numbers, n = list(map(int, input().split()))
#     numbers = list(str(numbers))
#     sortedNumbers = sorted(numbers, key=lambda x: x, reverse=True)
#
#     for i in range(n):
#         maxNum = sortedNumbers[i]  # 이상적 형태의 단계
#         changeNum = numbers[i]
#         # maxIdx = numbers.index(maxNum)
#         # 최대값을 뒤에서 부터 찾는다.
#         for j, number in enumerate(sortedNumbers[::-1]):
#             if number == changeNum:
#                 maxIdx = len(numbers) - j - 1
#                 break
#
#         numbers[maxIdx], numbers[i] = numbers[i], numbers[maxIdx]
#         if numbers == sortedNumbers:
#             break
#
#     print("#"+str(test), int(''.join([str(i) for i in numbers])))
#


# 재풀이(참고)
def dfs(depth):
    global answer  # answer의 변경이 있으므로 global 선언 필요함
    if depth == N:  # 횟수 도달
        temp = ''.join(numbers)
        if temp > answer:
            answer = temp
        return

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]  # 자리 바꾸기
            temp = ''.join(numbers)
            if visited.get((temp, depth), 1):  # 중복 확인
                visited[(temp, depth)] = 0
                dfs(depth+1)
            numbers[i], numbers[j] = numbers[j], numbers[i]  # 자리 원상 복구


for test in range(1, int(input())+1):
    numbers, N = input().split()
    numbers = list(numbers)
    N = int(N)
    result = ''
    answer = '00000000'
    visited = {}

    dfs(0)
    print('#{} {}'.format(test, answer))
