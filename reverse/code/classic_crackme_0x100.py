i = 0
secret1 = 85
secret2 = 51
secret3 = 15
inp = []
flag = "kgxmwpbpuqtorzapjhfmebmccvwycyvewpxiheifvnuqsrgexl"
for a in flag:
    inp.append(a)
while i <= 2:
    for i_0 in range(0 , len(flag)):
        random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
        random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
        inp[i_0] = ord(inp[i_0]) - (random2 & secret3) - (secret3 & (random2 >> 4)) % 26
        inp[i_0] = chr(inp[i_0])
    i += 1
print(''.join(inp))
