from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
heslo = "kokot123"
zprava = b"kokotko jeden vymrdana"
salt = os.urandom(16)
nonce = os.urandom(12)
dir_path = os.path.dirname(os.path.abspath(__file__))
user_dir_path = os.path.join(dir_path, "users", "user1.dat")
print(user_dir_path)

def derive_key(password:str, salt:bytes) -> bytes:
    password# .encode() zjistit proč encode - encode se dává pokud chcem dát string na nějkou věc - utf-8 ascii atd. proč? idk
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000

    )
    
    key = kdf.derive(password.encode())
    print(f"{key.hex()} je klic")
    return key
    
    

def encrypt(data:bytes, password:str):#šifrování
    print("Sifruji")

    salt = os.urandom(16)#generuju salt, 16 bitů

    key = derive_key(password, salt)#generuju klíč přes volání funkce, zadávám heslo a salt(může být veřejný)

    nonce = os.urandom(12)#generuji nonce - číslo co je jen jednou použito při šifrování

    aes = AESGCM(key)
   
    crypted_text = aes.encrypt(
        nonce, 
        data, 
        None
    )
    print(f"Crypted text: {crypted_text}")
    print(f"vracím:{salt+nonce+crypted_text} kde salt je: {salt} nonce je {nonce} a crypted text je {crypted_text}")
    return salt+nonce+crypted_text #vracím salt nonce a šifrovaný text 

    
def decrypt(encrypted_data:bytes, password:str) -> bytes:#dešifrování
    print("desifruji")
    salt = encrypted_data[0:16]
    print(f"SALT: {salt}")
    nonce = encrypted_data[16:28]
    print(f"NONCE: {nonce}")
    data = encrypted_data[28:]
    print(f"DATAAA: {data}")

    key = derive_key(password, salt)

    aes = AESGCM(key)
    
    return aes.decrypt(
        nonce,
        data,
        None
    )
with open(user_dir_path, "wb") as f:
    awd = encrypt(zprava, heslo)
    
    f.write(awd)

    
with open(user_dir_path, "rb") as f:
    data = f.read()
    print(f"náhodná mrdka v user1.dat: {data}")
    try:
        wad = decrypt(awd, heslo)
        print(wad)
    except:
        print("nelze")
    

