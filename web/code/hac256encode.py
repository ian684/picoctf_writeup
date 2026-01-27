import jwt
import time

secret = "ilovepico"

payload = {"user":"admin"}

token = jwt.encode(
    payload,
    secret,
    algorithm="HS256",
    headers={
        "typ": "JWT"
    }
)

print(token)

import datetime
token = jwt.encode(
  {
    'iss': 'bookshelf',
    'iat': datetime.datetime.utcnow(),
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
    'userId': 2,
    'email': 'user',
    'role': 'Admin'
  },
  '1234',
  algorithm='HS256'
)
print(token)
