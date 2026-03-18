def solve():
    v3 = [0xE1, 0xA7, 0x1E, 0xF8, 0x75, 0x23, 0x7B, 0x61]
    v4_0 = [0xB9, 0x9D, 0xFC, 0x5A, 0x5B, 0xDF, 0x69, 0xD2]
    v4_7 = [0xD2, 0xFE, 0x1B, 0xED, 0xF4, 0xED, 0x67, 0xF4]
    
    data = v3 + v4_0 + v4_7[1:]
    
    flag = [0] * 27
    v11 = 0
    v10 = 0
    
    for i in range(23):
        for j in range(8):
            if v10 == 0:
                v10 = 1
            
            target_byte = data[i]
            target_bit = (target_byte >> (7 - j)) & 1
            
            if target_bit:
                flag[v11] |= (1 << (7 - v10))
            v10 += 1
            if v10 == 8:
                v10 = 0
                v11 += 1
            
    return "".join(map(chr, flag))
print("还原出的 Flag 为:", solve())
