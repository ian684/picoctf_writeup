aim = "104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42"

arr = list(map(int , aim.split()))
result = ""

for i in range(len(arr)):
    t = arr[i] % 41
    t = pow(t  , -1 , 41)
    if 1 <= t <= 26:
        result += chr(t + 64)
    elif t == 37:
        result += "_"
    else:
        result += str(t - 27)
print(result)
