T = int(input())
for test in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    result = sum(numbers)/len(numbers)

    print('#'+str(test), round(result))