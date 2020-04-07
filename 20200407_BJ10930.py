
#백준 10930 SHA-256
#난이도 : 하
#유형 : 해시,구현

import hashlib

s = input()
print(hashlib.sha256(s.encode()).hexdigest())
