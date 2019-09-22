
#백준 11048번

n, m = list(map(int, input().split()))

candies = [[0]*(m+1)]*(n+1)
max_candies = [[0]*(m+1)]*(n+1)

for i in range(1, n+1):
    candies[i] = [0] + list(map(int, input().split()))
    for j in range(1, m+1):
        max_candies[i][j] = max(max_candies[i-1][j], max_candies[i][j-1], max_candies[i-1][j-1]) + candies[i][j]

print(max_candies[-1][-1])