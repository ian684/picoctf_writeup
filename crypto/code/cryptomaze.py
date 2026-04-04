from Crypto.Cipher import AES

INITIAL_STATE_BITS = [
    0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0,
    1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1,
    0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1,
    1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1
]
TAPS = [63, 61, 60, 58]
CT_HEX = "8f0e6d0f5b0dc1db201948b9e0cebd8f81d250455a05ee7c9e2ba57a1bc5428938338e7e04fbddef0c6260a4eb758417"

def bits_to_int(bits):
    state = 0
    for b in bits:
        state = (state << 1) | b
    return state

def lfsr(state, taps, n_bits):
    out = []
    mask = (1 << 64) - 1
    for _ in range(n_bits):
        out.append((state >> 63) & 1)
        feedback = 0
        for t in taps:
            feedback ^= (state >> (63 - t)) & 1
        state = ((state << 1) & mask) | feedback
    return out

def bits_to_bytes(bits):
    return bytes(
        int(''.join(map(str, bits[i:i+8])), 2)
        for i in range(0, len(bits), 8)
    )

state = bits_to_int(INITIAL_STATE_BITS)
ks = lfsr(state, TAPS, 128)
key = bits_to_bytes(ks)

ct = bytes.fromhex(CT_HEX)
pt = AES.new(key, AES.MODE_ECB).decrypt(ct)

print("key =", key.hex())
print("pt  =", pt)
print("flag =", pt[:-pt[-1]].decode())
