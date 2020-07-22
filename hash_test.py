from passlib.hash import pbkdf2_sha256

password= '1234'

hash_pw = pbkdf2_sha256.hash(password)
print(hash_pw)
print(pbkdf2_sha256.verify(password, hash_pw))
# print(hash_pw == '$pbkdf2-sha256$29000$PYfwnjOGUMr5v7dWKuUcIw$lKkyG1F8vidDLqJaT0P2BoBgBmKb9fC/Ku2UMiLbp50')
