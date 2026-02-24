def decode(scrambled_L):
    res = []
     # 遍歷 L 中的每一個子列表 (A[0], A[1], A[2]...)
    for sublist in scrambled_L:
        # 只提取子列表中的字串元素，忽略嵌套的 list
        for item in sublist:
             if isinstance(item, str):
                 # 將 '0x..' 轉回字元
                 res.append(chr(int(item, 16)))
    return "".join(res)

if __name__ == "__main__":
    arr = []
    ans = decode(arr)
    print(ans)
