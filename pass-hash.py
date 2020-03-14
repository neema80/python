# import the hash algorithm
from passlib.hash import pbkdf2_sha256
# from passlib.hash import pbkdf2_sha256
# generate new salt, and hash a password
# hash = pbkdf2_sha256.hash("toomanysecrets")
# print(hash)

# verifying the password
# pbkdf2_sha256.verify("toomanysecrets", hash)

# pbkdf2_sha256.verify("joshua", hash)

# returns the algorithm's name and hash result
def hash_password(password):
    return pbkdf2_sha256.hash(password)


# returns a boolean
def check_hashed_password(password, hashed_password):
    return pbkdf2_sha256.verify(password, hashed_password)

my_password = 'admin123'
hashed = hash_password(my_password)

print(hashed)

if check_hashed_password(input('Enter password: '), hashed):
    print('password is valid')
else:
    print('invalid password')