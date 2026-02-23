flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽"
for i in range(len(flag)):
    t = bin(ord(flag[i]))[2:]
    t = '0'*(16-len(t)) + t
    print(chr(int(t[0:8] , 2)) , end="") 
    print(chr(int(t[8:16] , 2)) , end="")
