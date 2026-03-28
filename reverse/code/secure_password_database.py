def djb2_hash(byte_array):
    h = 5381
    for b in byte_array:
        if b == 0:
            break
        h = ((h * 33) + b) & 0xFFFFFFFFFFFFFFFF
    return h

leaked_bytes = [105, 85, 98, 104, 56, 49, 33, 106, 42, 104, 110, 33] 

result = djb2_hash(leaked_bytes)
print(f"你需要输入的 Hash 值是: {result}")
