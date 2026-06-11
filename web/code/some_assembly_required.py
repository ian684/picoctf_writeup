raw_data = b"\x9d\x6e\x93\xc8\xb2\xb9\x41\x8b\x94\x90\xdd\x3e\x94\x97\x90\xdd\x3f\xc4\xc2\xc9\xdd\x34\xc2\xc5\x97\xdb\x31\x93\x92\xc0\xda\x36\x93\x93\xc1\xd9\x3e\x91\xc1\x97\x90\x00\x00"

hex_string = raw_data.hex()
flag = []
for i in range(0 , len(hex_string) , 2):
    flag.append(int(hex_string[i:i+2] , 16))
raw_key = b"\xf1\xa7\xf0\x07\xed"
raw_key = raw_key.hex()
key = []
for i in range(0 , len(raw_key) , 2):
    key.append(int(raw_key[i:i+2] , 16))
for i in range(len(flag)):
    temp = flag[i]
    j = 4-i%5
    print(chr(key[j] ^ temp) , end="")
