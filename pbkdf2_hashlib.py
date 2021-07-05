import hashlib, binascii 

hash = hashlib.pbkdf2_hmac('sha512', b'SuperSecretPassword', b'saltthepassword', 10000)

print(binascii.hexlify(hash))