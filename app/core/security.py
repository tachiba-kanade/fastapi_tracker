# Password hashing and JWT

"""
password
   ↓
hash it in security.py
   ↓
store the result in hash_password

"""

from argon2 import PasswordHasher
from pwdlib import PasswordHash


password_hasher= PasswordHash.recommended()

def hash_password(plain_password:str) ->str:
    """
    Convert a plain password into a secure hash.
    """

    return password_hasher.hash(plain_password)


def verify(plain_password:str, hashed_password:str)->bool:
    """
    Check whether a plain password matches a stored hash.
    """
    return password_hasher(plain_password, hashed_password)    