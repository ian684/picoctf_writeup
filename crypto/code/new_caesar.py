import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

def b16_decode(enc):
	dec = ""
	for i in range(0, len(enc), 2):
		first = ALPHABET.index(enc[i])
		second = ALPHABET.index(enc[i+1])
		binary = "{0:04b}{1:04b}".format(first, second)
		dec += chr(int(binary, 2))
	return dec
def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]
enc = "fegdeogdgecoeocgcgchcfcffccfca"
dec = ""
for a in ALPHABET:
	for i, c in enumerate(enc):
		dec += unshift(c, a)
	print(a, b16_decode(dec))
	dec = ""
