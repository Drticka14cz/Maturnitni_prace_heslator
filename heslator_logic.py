from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import json

dir_path = os.path.dirname(os.path.abspath(__file__))

# ZÍSKÁNÍ KLÍČE
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
    
    
# Š I F R O V Á N Í
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

# D E Š I F R O V Á N Í
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

 #načtení dat   
def load_data(heslo, user_dir_path):
    if not os.path.exists(user_dir_path):
        return None, False
    if  os.path.getsize(user_dir_path) == 0:
        return new_data(heslo, user_dir_path)
    try:
        with open(user_dir_path, "rb") as f:
            data_bytes = f.read()
        
            print(f"náhodná mrdka v user1.dat: {data_bytes}")
            desifrovana_bytes = decrypt(data_bytes, heslo)
            json_string = desifrovana_bytes.decode('utf-8')
            data = json.loads(json_string)
            return data, True
    except Exception as e:
        print(f"nelze: {e}")
        return None, False
       
#Uložení dat
def save_data(heslo: str, user_dir_path: str, data: dict, ):
    try:
        json_bytes = json.dumps(data, ensure_ascii=False).encode('utf-8')

        zasifrovano = encrypt(json_bytes, heslo)
        with open(user_dir_path, "wb") as f:
            f.write(zasifrovano)
            return True
    except Exception as e:
        print(f"Chyba při uložení: {e}")
        return False

#Pokud již uživatel má svůj soubor ale je prázdný. 
def new_data( heslo, user_dir_path):
    
    print("nová data")
    data = {
        "historie_rozbor": [],# zde bude dict kde bude heslo score čas a čas rozboru
        "ulozena_hesla":[] , # zde bude platforma jméno heslo poznámka a score
        "nastaveni":{
            "Dark_mode": True,

        },
    }
    save_data(heslo, user_dir_path, data)
    return data, True




class Login:
    def __init__(self, jmeno, heslo):
        self.jmeno = jmeno
        self.heslo = heslo
        
        self.data = None
        self.prihlasen = False
        self.poznamka  = ""
        self.prihlaseni()
    def prihlaseni(self):
        if self.jmeno and self.heslo:
            if self.jmeno == "guest" and self.heslo == "guest":
                self.prihlasen = True
                self.poznamka = "úspěšně přihlášen"
            else:
                
                user_dir_path = os.path.join(dir_path, "users",f"{self.jmeno}.dat")
                self.data, self.prihlasen = load_data(self.heslo,user_dir_path)
                if self.prihlasen:

                    self.poznamka = "úspěšně přihlášen"
                else:
                    self.poznamka = "Špatné heslo nebo poškozený soubor"
                
        else: 
            self.prihlasen = False
            self.poznamka = "problém s přihlášením"
                
        
        return(self.poznamka,self.prihlasen)
    

class New_account:
    def __init__(self, jmeno, heslo, heslo_2):
        self.jmeno = jmeno
        self.heslo = heslo
        self.heslo_2 =heslo_2
        self.zalozeni = False
        self.poznamka = ""
        self.create_new_account()


    def create_new_account(self):
        
        if self.heslo == self.heslo_2:
            new_user_dir_path = os.path.join(dir_path, "users",f"{self.jmeno}.dat")
            if  os.path.exists(new_user_dir_path):
                self.zalozeni = False
                self.poznamka = "Tento uživatel již existuje"
            else:
                self.data, self.zalozeni = new_data(self.heslo, new_user_dir_path)
                if self.zalozeni:
                    self.poznamka = "učet byl úspěšně založen"
                else:
                    self.poznamka = "nepodařilo se založit účet"
            return self.poznamka, self.zalozeni
        else:
            self.poznamka = "hesla nesedí"
            self.zalozeni = False
            return self.poznamka, self.zalozeni
        


class Rozbor:
    def __init__(self, heslo):
        import math
        import string
        self.heslo = heslo.strip()
        self.mala =0 
        self.velka = 0
        self.cislo = 0
        self.spec = 0
        self.delka = len(heslo)
        self.pot_zn = 0
        self.mala2 = " "
        self.velka2 = " "
        self.cislo2 = " "
        self.spec2 = " "
        self.delka2 = " "
        self.skore = 0 #nove
        self.minuly_znak = ""
        self.minuly_znak_presne = ""
        self.pocet_minuly_presne = 0
        self.pocet_minuly = 0
        self.score2 = ""
        self.heslo = heslo.strip()
        self.heslo2 = "Heslo: " + heslo
        self.poznamka = ""

    # def kontrola(self):
    #     for i in heslo:
    #         if minuly_znak_presne == i:
    #             pocet_minuly_presne +=1
    #             if pocet_minuly_presne == 1:
    #                 skore -= 0.5
        
    #             if pocet_minuly_presne ==2:
    #                 skore -=1
        
    #             if pocet_minuly_presne >=3:
    #                 skore -= (pocet_minuly_presne/2 + 0.5)
        
        
        
    #         else:
    #             minuly_znak_presne = i
    #             pocet_minuly_presne = 0
    #         if i.islower():
    #             mala += 1
    #             if minuly_znak == "m":
    #                 if pocet_minuly >= 6:
    #                     skore -= 2
    #                 elif pocet_minuly>= 3:
    #                     skore -= 0.5
    #                 else:
    #                     skore += 1
    #                 pocet_minuly +=1
    #             else:
    #                 skore += 1.5
    #                 minuly_znak = "m"
    #                 pocet_minuly = 0
    #         if i.isupper():
    #             velka += 1
    #             if minuly_znak == "v":
    #                 if pocet_minuly >= 6:
    #                     skore -= 2
    #                 elif pocet_minuly>= 3:
    #                     skore -=0.5
    #                 else:
    #                     skore += 1
    #                 pocet_minuly +=1
    #             else:
    #                 skore += 1.5
    #                 minuly_znak = "v"
    #                 pocet_minuly = 0
    #         if i.isdigit():
    #             cislo += 1
    #             if minuly_znak == "c":
    #                 if pocet_minuly >= 6:
    #                     skore -= 2
    #                 elif pocet_minuly>= 3:
    #                     skore -=0.5
    #                 else:
    #                     skore += 1
    #                 pocet_minuly +=1
    #             else:
    #                 skore += 1.5
    #                 minuly_znak ="c"
    #                 pocet_minuly = 0
        
    #         if i in "!@#$%^&*()_+-=[]{}|\\:;\"',.<>/?":
    #             spec += 1
    #             if minuly_znak == "s":
    #                 if pocet_minuly >= 6:
    #                     skore -= 1.5
    #                 elif pocet_minuly>= 3:
    #                     skore -=0.5
    #                 else:
    #                     skore += 1.5
    #                 pocet_minuly +=1
    #             else:
    #                 skore +=2
    #                 minuly_znak = "s"
    #                 pocet_minuly = 0
        
    #     #penalizace za chybejici typy znaku           
    #     if mala ==0:
    #         skore -= 2
    #     if velka ==0:
    #         skore -= 2
    #     if cislo ==0:
    #         skore -= 2
    #     if spec ==0:
    #         skore -= 2
        
        
    #     if mala > 0:
    #         pot_zn += len(string.ascii_lowercase)
    #     if velka > 0:
    #         pot_zn += len(string.ascii_uppercase)
    #     if cislo > 0:
    #         pot_zn+= len(string.digits)
    #     if spec >0:
    #         pot_zn += len(string.punctuation)
        
    #     bits = delka * math.log2(pot_zn)
        
    #     cas = 2**bits/ 1e9
    #     sekundy = round(cas,5)
    #     minuty = round(cas/60, 2)
    #     hodiny = round(minuty/60,2)
    #     dny = round(hodiny/24, 2)
    #     tydny = round(dny/7, 2)
    #     mesice = round(tydny/4, 2)
    #     roky = round(mesice/12,2)
        
    #     skore += bits
    #     cas_class = 0
        
    #     if roky > 1:
    #         if roky > 1000:
    #             if roky > 1000000:
    #                 if roky >1000000000:
    #                     cas_t = (f"Více jak miliarda let")
    #                     cas_class = 6
        
    #                 else:
    #                     miliony = round(roky/1000000,2)
        
    #                     cas_t = (f"{miliony} Milionů let")
    #                     cas_class = 6
    #             else:
    #                 tisicileti = round(roky /1000,2)
    #                 cas_t = (f"{tisicileti} Tisíc let")
    #                 cas_class = 6
    #         else:
    #             cas_t = (f"{roky} Roků")
    #             cas_class = 5
    #     elif mesice >1:
    #         cas_t = (f"{mesice} Měsíců")
    #         cas_class = 4
    #     elif tydny >1:
    #         cas_t = (f"{tydny} Týdnů")
    #         cas_class = 3
    #     elif dny >1:
    #         cas_t = (f"{dny} Dnů")
    #         cas_class = 2
    #     elif hodiny >1:
    #         cas_t = (f"{hodiny} Hodin")
    #         cas_class = 2
    #     elif minuty > 1:
    #         cas_t = (f"{minuty} Minut")
    #         cas_class = 1
    #     else:
    #         cas_t = (f"{sekundy} Sekund")
    #         cas_class = 1
    #     cas2 = f"Maximální doba k prolomení hesla: {cas_t}"
        
    #     #print(sekundy , minuty, hodiny, dny, tydny, mesice, roky)
        
        
    #     #predelat zakazane fraze atd - nacitani z souboru a forcyklus 
    #     if "heslo" in heslo.lower() or "123" in heslo or "abc" in heslo.lower() or "1234" in heslo or "123456789" in heslo or "qwerty" in heslo.lower() or "abcd" in heslo.lower():
    #         skore -= 6
    #         poznamka = "obsahuje jedno z základních zakázaných(slabých) slov."
        
        
        
    #     # vyhodnoceni 
    #     if int(delka) < 8:
    #         delka2 = "je kratké (alespoň 8 znaků) "
    #     if int(delka) >= 8:
    #         delka2 = "je dostatečně dlouhé. "
    #     if int(mala) < 2:
    #         mala2 = "obsahuje málo malých písmen. (alespoň 2) "
    #     if int(mala) >= 2:
    #         mala2 = "obsahuje dostatečné množství malých písmen. "
    #     if int(cislo) < 2:
    #         cislo2 = "obsahuje málo čísel. (alespoň 2) "
    #     if int(cislo) >= 2:
    #         cislo2 = "obsahuje dostatek čísel. "
    #     if int(spec) < 2:
    #         spec2 = "obsahuje málo speciálních znaků(př. !@#$%^&*()_+-=[]{}|\\:;\"',.<>/?). (alespoň 2) "
    #     if int(spec) >= 2:
    #         spec2 =  "obsahuje dostatečné množství speciálních znaků. "
    #     if int(velka) < 2:
    #         velka2 = "obsahuje málo velkých písmen. (alespoň 2) "
    #     if int(velka) >= 2:
    #         velka2 =  "obsahuje dostatečné množstvívelkých písmen. "
        
        
    #     skore = round(skore, 2)
    #     if skore < 0:
    #         skore = 0
        
    #     if skore > 100:
    #         score2 = f"Tvé heslo je extrémně silné. (score: {skore})"
    #         skore_class = 6
    #     elif skore > 80:
    #         score2 = f"Tvé heslo je velmi silné. (score: {skore})"
    #         skore_class = 5
    #     elif skore > 60:
    #         score2 = f"Tvé heslo je silné. (score: {skore})"
    #         skore_class = 4
    #     elif skore > 40:
    #         score2 = f"Tvé heslo není silné. (score: {skore})"
    #         skore_class = 3
    #     elif skore > 25:
    #         score2 = f"Tvé heslo je slabé. (score: {skore})"
    #         skore_class = 2
    #     elif skore <=25:
    #         score2 = f"Tvé heslo je velmi slabé. (score: {skore})"
    #         skore_class = 1









        

class Generator:
    def __init__(self):
        pass

class Ulozeni:
    def __init__(self):
        pass

class Nastaveni:
    def __init__(self):
        pass