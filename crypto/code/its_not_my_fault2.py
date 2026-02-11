import hashlib
import itertools
import string

prefix = input("first 5 chars: ")
target_suffix = input("last 6 chars of MD5: ")

charset = string.ascii_lowercase + string.digits
flag = False
for length in range(1, 8):
    for combo in itertools.product(charset, repeat=length):
        suffix = ''.join(combo)
        s = prefix + suffix
        h = hashlib.md5(s.encode()).hexdigest()

        if h.endswith(target_suffix):
            print("find string:", s)
            print("MD5:", h)
            flag = True
            break
    if flag:break

#=======================================================

from math import gcd
e = int(input("e = "))
n = int(input("n = "))

for d_p in range(0 , 1 << 36):
    if gcd(e*d_p - 1 , n) > 1:
        print(gcd(e*d_p - 1 , n))
        break

