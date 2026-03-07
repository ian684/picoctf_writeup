from urllib.parse import unquote
import base64

result = b"JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM0JTYyJTYyJTMyJTMyJTM3JTMyJTMx"
result = base64.b64decode(result)
result = unquote(result)
print("picoctf{" , end="")
print(result , end="")
print("}")
