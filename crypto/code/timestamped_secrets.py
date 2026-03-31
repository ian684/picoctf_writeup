from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

ciphertext_hex = "6d8330b05a68848fdf4b7ab057cd6eb070810e3febd76872b4a5e7627221a396"
hint_timestamp = 1770242633
search_range = 5000

def brute_force():
    ciphertext = bytes.fromhex(ciphertext_hex)
    
    print(f"開始爆破，搜尋範圍：{hint_timestamp - search_range} 到 {hint_timestamp + search_range}")

    for ts in range(hint_timestamp - search_range, hint_timestamp + search_range):
        key = sha256(str(ts).encode()).digest()[:16]
        cipher = AES.new(key, AES.MODE_ECB)
        
        try:
            decrypted = cipher.decrypt(ciphertext)
            
            result = unpad(decrypted, AES.block_size).decode('utf-8')
            
            if "picoCTF" in result:
                print(f"\n[+] 成功找到 Flag!")
                print(f"[+] 正確的時間戳: {ts}")
                print(f"[+] 解密結果: {result}")
                return
                
        except (ValueError, UnicodeDecodeError):
            continue

    print("\n[-] 爆破結束，未找到結果。請嘗試加大 search_range。")

if __name__ == "__main__":
    brute_force()
