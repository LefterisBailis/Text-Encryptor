from cryptography.fernet import Fernet

key = Fernet.generate_key() 

with open('key.txt', 'wb') as f:
    f.write(key)
    print("Encryption Key generated and stored succesfully!")

