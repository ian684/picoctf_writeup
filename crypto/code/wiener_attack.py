import math
from typing import Optional, List, Tuple

def is_perfect_square(x: int) -> bool:
    if x < 0:
        return False
    r = int(math.isqrt(x))
    return r * r == x

def continued_fraction(numer: int, denom: int) -> List[int]:
    """Return continued fraction expansion of numer/denom."""
    cf = []
    while denom:
        a = numer // denom
        cf.append(a)
        numer, denom = denom, numer - a * denom
    return cf

def convergents_from_cf(cf: List[int]) -> List[Tuple[int, int]]:
    """Return list of convergents (k, d) from continued fraction terms."""
    conv = []
    # h[-2]=0, h[-1]=1 ; k[-2]=1, k[-1]=0 (standard recurrence)
    p0, p1 = 0, 1
    q0, q1 = 1, 0
    for a in cf:
        p = a * p1 + p0
        q = a * q1 + q0
        conv.append((p, q))  # (numerator, denominator)
        p0, p1 = p1, p
        q0, q1 = q1, q
    return conv

def wiener_attack(e: int, n: int) -> Optional[int]:
    """
    Try Wiener attack on RSA public key (e, n).
    Return private exponent d if vulnerable, else None.
    """
    cf = continued_fraction(e, n)
    for k, d in convergents_from_cf(cf):
        if k == 0:
            continue
        # ed ≡ 1 (mod phi)  =>  ed - 1 = k * phi
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k

        # For RSA: phi = (p-1)(q-1) = n - (p+q) + 1
        # So p+q = n - phi + 1
        s = n - phi + 1
        discr = s * s - 4 * n
        if discr < 0 or not is_perfect_square(discr):
            continue

        t = int(math.isqrt(discr))
        p = (s + t) // 2
        q = (s - t) // 2
        if p * q == n and p > 1 and q > 1:
            return d
    return None

if __name__ == "__main__":
    # 範例用法：把 e, n 換成你的
    e = int(input("e = ").strip())
    n = int(input("n = ").strip())

    d = wiener_attack(e, n)
    if d is None:
        print("Not vulnerable to Wiener (or parameters not RSA).")
    else:
        print("VULNERABLE! d =", d)

