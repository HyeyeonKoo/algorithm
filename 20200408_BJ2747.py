#백준 2747 피보나치 수
#난이도 : 하
#문제유형 : DP

n = int(input())
fibo = [0, 1]
for i in range(2, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo[-1])