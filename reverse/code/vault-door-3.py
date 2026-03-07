result = 'jU5t_a_sna_3lpm18gb4c_u_4_m2r640'

flag = ['*']*32
for i in range(17 , 32 , 2):
    flag[i] = result[i]
for i in range(16 , 32 , 2):
    flag[46-i] = result[i]
for i in range(8 , 16):
    flag[23-i] = result[i]
for i in range(0 , 8):
    flag[i] = result[i]
print("picoCTF{" , end="")
print(''.join(flag) , end="")
print("}")
