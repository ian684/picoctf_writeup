from pwn import *

c = 2575135950983117315234568522857995277662113128076071837763492069763989760018604733813265929772245292223046288098298720343542517375538185662305577375746934

r = remote("titan.picoctf.net" , 60483)

r.recvuntil(b"E --> encrypt D --> decrypt.")
r.sendline(b"e")

r.recvuntil(b"enter text to encrypt (encoded length must be less than keysize):")
r.sendline(b"\x02")


r.recvuntil(b"ciphertext (m ^ e mod n)")
c2 = int(r.recvline())

r.recvuntil(b"E --> encrypt D --> decrypt.")
r.sendline(b"d")

r.recvuntil(b"Enter text to decrypt:")
r.sendline(str(c*c2).encode())

r.recvuntil(b"decrypted ciphertext as hex (c ^ d mod n):")
password = int(r.recvline() , 16) // 2
#dec

password = hex(password)[2:]
#hex

password = bytes.fromhex(password)
#bytes
print(password)
