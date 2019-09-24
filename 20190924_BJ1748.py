
# 백준 1748번

n = int(input())

l = len(str(n))
nine = 9
ten = 0
result = 0
for i in range(1, l):
    result += i * (nine - ten + 1)
    nine = int(str(nine) + "9")
    if ten == 0:
        ten = 10
    else:
        ten *= 10
result += l * (n - ten + 1) - 1
print(result)