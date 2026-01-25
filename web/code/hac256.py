import jwt

token = input()

secret = "1234"

payload = jwt.decode(
    token,
    secret,
    algorithms=["HS256"],
    issuer="bookshelf"
)

print(payload)

