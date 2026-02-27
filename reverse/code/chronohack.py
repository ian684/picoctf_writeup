from pwn import *
import time , random


alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
length = 20


for attempt in range(-50 , 1000 , 50):

    base = int(time.time()*1000)
    r = remote("verbal-sleep.picoctf.net" , 57709)

    for i in range(50):

        r.recvuntil(b"(or exit):")
        t = base + attempt + i
        random.seed(int(t))

        result = ""
        for _ in range(length):
            result += random.choice(alph)

        r.sendline(result.encode())

        response = r.recvline()
        print(attempt , response)
        if b"Congratulations" in response:
            print(r.recvline().decode())
            exit()
    r.close()
