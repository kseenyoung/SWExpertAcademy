dic = {1: 3, 2: 1, 3: 2}

for a, b in dic.items():
    len_b = len(dic)
    print(a, b)

print(len_b)

i = 777
for i in range(1, 5):
    print(i)
print(i)

for i in range(1, 5):
    answer = '00000000' + str(i)
    print(answer)

print(answer)

# 결론
# for in문 안에 선언된 변수를 전역 변수로 인식
# 전역 변수를 지역에서 변경시 global/ nonlocal 선행자 필요
# dictionary 다양한 함수 : get(key, <default>), items, values ...  => 블로그
# DFS/BFS
