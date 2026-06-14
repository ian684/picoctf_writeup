a = [
    0x18, 0x6a, 0x7c, 0x61, 0x11, 0x38, 0x69, 0x37,
    0x1f, 0x59, 0x79, 0x59, 0x3e, 0x1c, 0x56, 0x63,
    0x0d, 0x42, 0x1d, 0x7e, 0x6c, 0x39, 0x1c, 0x5a,
    0x21, 0x5d, 0x63, 0x11, 0x00, 0x62, 0x05, 0x49,
    0x4b, 0x7e, 0x61, 0x34, 0x1c, 0x57, 0x28, 0x0f,
    0x52
]

def decode():
    for i in range(0 , len(a)-1 , 2):
        a[i], a[i+1] = a[i+1], a[i]

    i = len(a) - 1
    while i >= 0:
        if i % 3 == 0:
            a[i] ^= 7
        elif i % 3 == 1:
            a[i] ^= 6
        else:  
            a[i] ^= 5

        if i % 2 == 0:
            a[i] ^= 9
        else:
            a[i] ^= 8
        
        a[i] ^= i % 10
        
        if i > 2:
            a[i] ^= a[i-3]
        if i > 0:
            a[i] ^= a[i-1]
        
        a[i] ^= 20
        
        i -= 1

    for i in range(len(a)):
        print(chr(a[i]), end="")
    print()

def encode():
    i = 0
    while i < len(a):
        a[i] ^= 20
        if i > 0:
            a[i] ^= a[i-1]
        if i > 2:
            a[i] ^= a[i-3]
        a[i] ^= i % 10
        if i % 2 == 0:
            a[i] ^= 9
        else:
            a[i] ^= 8
        if i % 3 == 0:
            a[i] ^= 7
        elif i % 3 == 1:
            a[i] ^= 6
        else:
            a[i] ^= 5
        i += 1
    for i in range(0 , len(a)-1 , 2):
        a[i], a[i+1] = a[i+1], a[i]
    
    for i in range(len(a)):
        print(chr(a[i]), end="")
    print()

decode()
