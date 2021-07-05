import hashlib

str = hashlib.sha1(b"SuperSecretPassword")
str_hex = str.hexdigest()
print (str_hex)
