from pwn import *

r = remote("fickle-tempest.picoctf.net" , 57039)

for _ in range(3):
    r.recvuntil(b"Please give ")
    a = r.recvuntil(b"as")
    a = a[3:]
    print(a)
    if a[0:3] == b"the":
        a = a[3:]
        print(a)
    a = a[:len(a)-2]
    print(a)

    x = input()
    if x == "b":
        a = a.split()
        t = ""
        for i in a:
            t += chr(int(i , 2))
        print(t)
    elif x == "o":
        a = a.split()
        t = ""
        for i in a:
            t += chr(int(i[1:] , 8))
        print(t)
    elif x == "h":
        a = a.strip()
        t = ""
        for i in range(0 , len(a) , 2):
            t += chr(int(a[i:i+2] , 16))
        print(t)
    else:
        break
    r.recvuntil(b"Input:")
    r.sendline(t.encode())
    print("ok")
while True:
    print(r.recvline())
r.interactive()
