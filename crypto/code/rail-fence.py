aim = "Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6"
result = ""

a , b , c , d = aim[0:10] , aim[10:29] , aim[29:47] , aim[47:56]
arr = [a , b , c , d]

now = 0
dire = 1
while True:
    try:
        result += arr[now][0]
        arr[now] = arr[now][1:]
        now += dire
        if now == 3 and dire == 1:
            dire = -1
        if now == 0 and dire == -1:
            dire = 1
    except:break
print(result)
