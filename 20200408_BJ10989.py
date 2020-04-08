
#백준 10989 수 정렬하기3
#난이도 : 하
#문제유형 : 정렬

n = int(input())
arr = [0]*10001
for _ in range(n):
    i = int(input())
    arr[i] += 1
for i in range(1001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)