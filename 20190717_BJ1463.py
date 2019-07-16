num = input()
count = list()

count.append(0)
for i in range(1, int(num)):
    count.append(count[i-1] + 1)
    if i % 2 == 0 and count[i] > count[int(i/2)]+1:
        count[i] = count[int(i/2)] + 1
    if i % 3 == 0 and count[i] > count[int(i/3)]+1:
        count[i] = count[int(i/3)] + 1

print(count[int(num)-1])