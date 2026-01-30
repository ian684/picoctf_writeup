aim = "350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213"

arr = list(map(int , aim.split()))
result = ""


for i in range(len(arr)):
    t = arr[i] % 37
    if 0 <= t <= 25:
        result += chr(t + 65)
    elif t == 36:
        result += "_"
    else:
        result += str(t - 26)
print(result)
