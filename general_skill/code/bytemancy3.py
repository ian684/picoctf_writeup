from pwn import *

r = remote("green-hill.picoctf.net" , 58889)

table = {b"astral_spark":0x080491c1 , b"glyph_conflux":0x0804919a,b"ember_sigil":0x08049176,b"binding_word":0x080491e3}
for i in range(3):
    print(r.recvuntil(b"Send the 4-byte little-endian address for procedure"))

    aim = r.recvline().strip()[1:-2]
    print(aim)
    response = p32(table[aim])
    
    r.sendafter(b"==> " , response)
r.interactive()
