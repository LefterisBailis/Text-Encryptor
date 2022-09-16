from cryptography.fernet import Fernet

try:
  f = open("key.txt", "rb")
except IOError:
  print("No Encryption Key Detected")
  exit()

cipher_suite = Fernet(f.read())

plaintext = bytes(input("Text to encrypt: "), 'utf-8')

encoded_text = cipher_suite.encrypt(plaintext)

print(encoded_text.decode())

input("Pree Enter to Exit")
