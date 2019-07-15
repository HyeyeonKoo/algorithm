s = input()
result = ""

for i in range(len(s)):
    if (s[i]>="a" and s[i]<="z") or (s[i]>="A" and s[i]<="Z"):
        asciiNum = ord(s[i]) + 13
        code = chr(asciiNum)
        if (code>="a" and code<="z") or (code>="A" and code<="Z"):
            result += chr(asciiNum)
        else:
            result += chr(asciiNum - 26)
    else:
        result += s[i]

print(result)