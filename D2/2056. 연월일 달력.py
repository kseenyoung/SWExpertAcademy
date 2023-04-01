
T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    date = input()
    year = date[:4]
    if 0 < int(date[4:6]) < 13:
        month = int(date[4:6])
        if days[month-1] >= int(date[6:]):
            print("#"+str(test_case), year+'/'+date[4:6]+'/'+date[6:])
        else:
            print("#" + str(test_case), -1)
    else:
        print("#"+str(test_case), -1)

