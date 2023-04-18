import config
import os

ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")

def encrypt(plaintext):
  # use ENCRYPTION_KEY to encrypt a password
  ciphertext = plaintext
  return ciphertext


def decrypt(ciphertext):
  # use ENCRYPTION_KEY to decrypt a password
  plaintext = ciphertext
  return plaintext