def steplfsr(lfsr):
    b7 = (lfsr >> 7) & 1
    b5 = (lfsr >> 5) & 1
    b4 = (lfsr >> 4) & 1
    b3 = (lfsr >> 3) & 1

    feedback = b7 ^ b5 ^ b4 ^ b3
    lfsr = (feedback << 7) | (lfsr >> 1)
    return lfsr
ans = 1000642226001692253839954048527111901419821797818129746146647649137154449226190505
ans = ans.to_bytes(34 , byteorder="big")
for lfsr in range(0 , 256):
    new = lfsr
    flag = ""
    for c in ans:
        new = steplfsr(new)
        flag += chr(c^new)
    if "pico" in flag:
        print(flag)
        break
