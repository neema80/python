# import the hash algorithm
from passlib.hash import pbkdf2_sha256
# from passlib.hash import pbkdf2_sha256
# generate new salt, and hash a password
hash = pbkdf2_sha256.hash("toomanysecrets")
print(hash)

# verifying the password
pbkdf2_sha256.verify("toomanysecrets", hash)

pbkdf2_sha256.verify("joshua", hash)
