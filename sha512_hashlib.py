import hashlib

str = hashlib.sha512 (b"SuperSecretPassword")
str_hex = str.hexdigest()
print (str_hex)
