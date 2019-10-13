
#백준 14391번
#비트마스크 코드 참조 

n, m = map(int, input().split(" "))
paper = [list(map(int, list(input()))) for _ in range(n)]

result = 0
for a in range(1 << (n*m)):
    hap = 0
    for i in range(n):
        temp = 0
        for j in range(m):
            k = i * m + j
            if a & (1 << k) == 0:
                temp = temp * 10 + paper[i][j]
            else:
                hap += temp
                temp = 0
        hap += temp
    for j in range(m):
        temp = 0
        for i in range(n):
            k = i * m + j
            if a & (1 << k) != 0:
                temp = temp * 10 + paper[i][j]
            else:
                hap += temp
                temp = 0
        hap += temp
    result = result if result > hap else hap
print(result)