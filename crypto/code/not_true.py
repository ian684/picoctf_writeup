from sage.all import *

N = 48
p = 3
q = 509
h_list = [83, 440, 124, 416, 371, 240, 320, 408, 130, 337, 399, 169, 81, 354, 221, 446, 309, 97, 148, 403, 506, 163, 195, 379, 91, 354, 24, 11, 72, 264, 343, 442, 319, 10, 418, 114, 140, 68, 116, 102, 507, 347, 65, 35, 7, 273, 290, 175]
ct_list = [[266, 103, 183, 99, 223, 103, 1, 377, 148, 10, 152, 500, 110, 255, 445, 248, 419, 283, 163, 260, 241, 433, 441, 481, 166, 159, 355, 153, 270, 357, 163, 481, 52, 498, 96, 444, 433, 1, 266, 176, 263, 264, 98, 111, 28, 280, 193, 363], [482, 430, 145, 33, 17, 508, 275, 281, 114, 483, 458, 143, 277, 276, 186, 492, 277, 176, 415, 123, 274, 239, 195, 163, 275, 82, 497, 364, 494, 113, 161, 187, 229, 495, 85, 169, 58, 496, 300, 421, 191, 21, 214, 377, 488, 439, 327, 169], [197, 239, 59, 404, 152, 444, 314, 168, 193, 326, 390, 51, 139, 296, 4, 357, 64, 476, 12, 313, 207, 401, 78, 492, 401, 75, 399, 95, 27, 178, 422, 242, 105, 125, 287, 11, 93, 397, 71, 495, 275, 57, 322, 413, 363, 489, 54, 45], [304, 172, 179, 19, 250, 416, 209, 0, 431, 123, 387, 404, 102, 474, 445, 174, 229, 464, 425, 204, 233, 426, 362, 179, 252, 377, 208, 87, 451, 334, 257, 214, 222, 239, 415, 66, 299, 469, 215, 283, 87, 444, 35, 451, 141, 185, 404, 269], [287, 283, 174, 167, 453, 203, 271, 389, 278, 264, 483, 181, 453, 147, 385, 254, 338, 330, 46, 77, 229, 247, 323, 97, 323, 232, 74, 99, 364, 165, 240, 222, 405, 107, 482, 508, 174, 97, 86, 397, 468, 353, 377, 56, 407, 203, 296, 119], [280, 434, 358, 332, 155, 154, 267, 179, 181, 383, 435, 233, 157, 250, 39, 181, 37, 52, 179, 361, 132, 254, 20, 183, 99, 393, 274, 401, 144, 178, 423, 187, 44, 376, 186, 256, 485, 377, 222, 433, 87, 470, 451, 153, 216, 248, 23, 117]]

def recover_f(N, q, h_list):
    H = matrix(ZZ, N, N)
    for i in range(N):
        for j in range(N):
            H[i, j] = h_list[(j - i) % N]

    I = matrix.identity(N)
    Z = matrix(ZZ, N, N)
    M = block_matrix(ZZ, [[I, H], [Z, q * I]])

    print("[*] 正在執行 LLL 規約以尋找私鑰 f...")
    L = M.LLL()
    for row in L:
        f_vec = row[:N]
        if all(abs(x) <= 1 for x in f_vec) and any(x != 0 for x in f_vec):
            return list(f_vec)
    return None

def decrypt_block(f_list, c_list, N, p, q):
    R = PolynomialRing(ZZ, 'x')
    x = R.gen()
    Rq = R.quotient(x^N - 1)
    Rp = PolynomialRing(GF(p), 'x').quotient(x^N - 1)
    
    f_poly = Rq(f_list)
    c_poly = Rq(c_list)
    
    a = f_poly * c_poly
    
    a_coeffs = []
    for coeff in a.list():
        c = int(coeff) % q
        if c > q // 2:
            c -= q
        a_coeffs.append(c)
    
    try:
        f_p_inv = Rp(f_list)^-1
    except ZeroDivisionError:
        return None
        
    m_poly = f_p_inv * Rp(a_coeffs)
    
    m_list = m_poly.list()
    m_list += [0] * (N - len(m_list))
    return m_list

f_recovered = recover_f(N, q, h_list)

if f_recovered:
    print(f"[+] 成功找到私鑰 f: {f_recovered}")
    
    all_bits = ""
    for block in ct_list:
        m_bits = decrypt_block(f_recovered, block, N, p, q)
        if m_bits is not None:
            all_bits += "".join(map(str, m_bits))
    
    print("[*] 正在解碼二進位訊息...")
    flag = ""
    for i in range(0, len(all_bits), 8):
        byte_str = all_bits[i:i+8]
        if len(byte_str) == 8:
            char_code = int(byte_str, 2)
            if char_code == 0: continue
            flag += chr(char_code)
            
    print(f"\n[!] 破解結果: {flag}")
else:
    print("[-] 失敗：無法透過 LLL 找到私鑰。")
