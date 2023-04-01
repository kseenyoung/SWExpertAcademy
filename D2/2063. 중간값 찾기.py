import sys
input = sys.stdin.readline
T = int(input())
line = list(map(int, input().split()))

line.sort()
print(line[T//2])