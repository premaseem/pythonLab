# $ pip install PyJWT
# https://github.com/jpadilla/pyjwt/

import jwt

encodedJWT = jwt.encode({"Header": {
    "alg": "HS256",
    "typ": "JWT"
}, "payload": {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
},"footer": {"line":"item"}}, "secret", algorithm="HS256")
print(encodedJWT)

decodedJWT = jwt.decode(encodedJWT, "secret", algorithms=["HS256"])
print(decodedJWT)