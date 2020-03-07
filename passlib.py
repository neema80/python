from passlib.hash import pbkdf2_sha512

# returns the algorithm's name and hash result
def hash_password(password):
    return pbkdf2_sha512.hash(password)

# returns a boolean
def check_hashed_password(password, hashed_password):
    return pbkdf2_sha512.verify(password, hashed_password)

my_password = 'admin123'

print(hashed)

if check_hashed_password('admin123', hashed):
    print('password is valid')
else:
    print('invalid password')