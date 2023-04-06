T = int(input())
rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test in range(1, T+1):
    n, k = list(map(int, input().split()))
    result = []
    for i in range(n):
        scores = list(map(int, input().split()))
        result.append((i+1, scores[0]*0.35 + scores[1]*0.45 + scores[2]*0.2))  # (학생 번호, 학생별 총점) 저장 # 총점 주의
    result.sort(key=lambda x: -x[1])  # 총점 기준 내림차순 정렬

    for i, a in enumerate(result):
        if a[0] == k:  # 해당 하는 학생을 발견
            print("#"+str(test), rank[i // (len(result)//10)])  # rank[순위 // 학점 별 학생 수]
            break