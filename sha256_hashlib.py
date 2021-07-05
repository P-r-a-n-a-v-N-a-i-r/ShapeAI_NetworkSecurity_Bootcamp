import hashlib

str = hashlib.sha256 (b"SuperSecretPassword")
str_hex = str.hexdigest()
print (str_hex)
