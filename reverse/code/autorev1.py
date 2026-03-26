from pwn import *

r = remote("mysterious-sea.picoctf.net" ,  56249)

print(r.recvuntil(b"Welcome! I think I'm pretty good at reverse enginnering. There's NO WAY anyone's better than me. Wanna try? I have 20 binaries I'm going to send you and you have 1 second EACH to get the secret in each one. Good luck >:)\n"))
i = 0
while i < 20:

    a = r.recvline()
    print(a)
    r.sendafter(b"What's the secret?:" , a)
    print(r.recvline())
    i += 1
r.interactive()
