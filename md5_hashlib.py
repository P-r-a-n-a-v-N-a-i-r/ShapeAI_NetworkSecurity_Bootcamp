import hashlib

print(hashlib.md5("SuperSecretPassword".encode('UTF-8')).hexdigest())
