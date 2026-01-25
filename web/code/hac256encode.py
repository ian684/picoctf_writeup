import jwt
import time

secret = "1234"

payload = {"role":"Admin","iss":"bookshelf","exp":1769915661,"iat":1769310861,"userId":2,"email":"user"}
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
