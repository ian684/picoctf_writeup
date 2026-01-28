chars = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_f85729e7}"

key = "CYLAB" * 10

i = 0
j = 0
while i < len(chars):
    if 65 <= ord(chars[i]) <= 90:
        print(chr(((ord(chars[i]) - ord(key[j]) + 26) % 26) + 65) , end="")
        i += 1
        j += 1
    elif 97 <= ord(chars[i]) <= 122:
        print(chr((((ord(chars[i]) - 97) - (ord(key[j]) - 65)+ 26 )% 26) + 97) , end="")
        i += 1
        j += 1
    #elif 48 <= ord(chars[i]) <= 57:
    #    print(chr((((ord(chars[i]) - 48) - (ord(key[i]) - 65) + 10 )% 10) + 48) , end="")
    else:
        print(chars[i] , end="")
        i += 1

