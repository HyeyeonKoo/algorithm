s = input()

s_list = list()
for i in range(len(s)):
    s_list.append(s[i:])

s_list.sort()

for w in s_list:
    print(w)