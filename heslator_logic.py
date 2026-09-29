from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import json
import sys
import string
import math

sys.stdout.reconfigure(encoding="utf-8")  # pro změnu šifrování znaků v terminálu


dir_path = os.path.dirname(os.path.abspath(__file__))
work_dir = os.path.join(dir_path, "work_files")
large_slovnik = os.path.join(work_dir, "Pwdb_top-10000000.txt")


# ZÍSKÁNÍ KLÍČE
def derive_key(password: str, salt: bytes) -> bytes:
    password  # .encode() zjistit proč encode - encode se dává pokud chcem dát string na nějkou věc - utf-8 ascii atd. proč? idk
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=1_200_000
    )

    key = kdf.derive(password.encode())
    print(f"{key.hex()} je klic")
    return key


# Š I F R O V Á N Í
def encrypt(data: bytes, password: str):  # šifrování
    print("Sifruji")

    salt = os.urandom(16)  # generuju salt, 16 bitů

    key = derive_key(
        password, salt
    )  # generuju klíč přes volání funkce, zadávám heslo a salt(může být veřejný)

    nonce = os.urandom(
        12
    )  # generuji nonce - číslo co je jen jednou použito při šifrování

    aes = AESGCM(key)

    crypted_text = aes.encrypt(nonce, data, None)
    print(f"Crypted text: {crypted_text}")
    print(
        f"vracím:{salt+nonce+crypted_text} kde salt je: {salt} nonce je {nonce} a crypted text je {crypted_text}"
    )
    return salt + nonce + crypted_text  # vracím salt nonce a šifrovaný text


# D E Š I F R O V Á N Í
def decrypt(encrypted_data: bytes, password: str) -> bytes:  # dešifrování
    print("desifruji")
    salt = encrypted_data[0:16]
    print(f"SALT: {salt}")
    nonce = encrypted_data[16:28]
    print(f"NONCE: {nonce}")
    data = encrypted_data[28:]
    print(f"DATAAA: {data}")

    key = derive_key(password, salt)

    aes = AESGCM(key)

    return aes.decrypt(nonce, data, None)


# načtení dat
def load_data(heslo, user_dir_path):
    if not os.path.exists(user_dir_path):
        return None, False
    if os.path.getsize(user_dir_path) == 0:
        return new_data(heslo, user_dir_path)
    try:
        with open(user_dir_path, "rb") as f:
            data_bytes = f.read()

            print(f"náhodná mrdka v user1.dat: {data_bytes}")
            desifrovana_bytes = decrypt(data_bytes, heslo)
            json_string = desifrovana_bytes.decode("utf-8")
            data = json.loads(json_string)
            return data, True
    except Exception as e:
        print(f"nelze: {e}")
        return None, False


# Uložení dat
def save_data(
    heslo: str,
    user_dir_path: str,
    data: dict,
):
    try:
        json_bytes = json.dumps(data, ensure_ascii=False).encode("utf-8")

        zasifrovano = encrypt(json_bytes, heslo)
        with open(user_dir_path, "wb") as f:
            f.write(zasifrovano)
            return True
    except Exception as e:
        print(f"Chyba při uložení: {e}")
        return False


# Pokud již uživatel má svůj soubor ale je prázdný.
def new_data(heslo, user_dir_path):

    print("nová data")
    data = {
        "historie_rozbor": [],  # zde bude dict kde bude heslo score čas a čas rozboru
        "ulozena_hesla": [],  # zde bude platforma jméno heslo poznámka a score
        "nastaveni": {
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
        self.poznamka = ""
        self.prihlaseni()

    def prihlaseni(self):
        if self.jmeno and self.heslo:
            if self.jmeno == "guest" and self.heslo == "guest":
                self.prihlasen = True
                self.poznamka = "úspěšně přihlášen"
            else:

                user_dir_path = os.path.join(dir_path, "users", f"{self.jmeno}.dat")
                self.data, self.prihlasen = load_data(self.heslo, user_dir_path)
                if self.prihlasen:

                    self.poznamka = "úspěšně přihlášen"
                else:
                    self.poznamka = "Špatné heslo nebo poškozený soubor"

        else:
            self.prihlasen = False
            self.poznamka = "problém s přihlášením"

        return (self.poznamka, self.prihlasen)


class New_account:
    def __init__(self, jmeno, heslo, heslo_2):
        self.jmeno = jmeno
        self.heslo = heslo
        self.heslo_2 = heslo_2
        self.zalozeni = False
        self.poznamka = ""
        self.create_new_account()

    def create_new_account(self):

        if self.heslo == self.heslo_2:
            new_user_dir_path = os.path.join(dir_path, "users", f"{self.jmeno}.dat")
            if os.path.exists(new_user_dir_path):
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
        print(f"Přijímám rozbor - {heslo}")
        self.heslo = heslo.strip()
        self.mala = 0
        self.velka = 0
        self.cislo = 0
        self.spec = 0
        self.delka = len(self.heslo)
        self.pot_zn = 0
        # self.mala2 = " "
        # self.velka2 = " "
        # self.cislo2 = " "
        # self.spec2 = " "
        # self.delka2 = " "
        self.score = 0  # nove
        self.minuly_znak = ""
        self.minuly_znak_presne = ""
        self.pocet_minuly_presne = 0
        self.pocet_minuly = 0
        self.score2 = ""
        self.heslo2 = "Heslo: " + self.heslo
        self.poznamka = ""
        self.score_class = 0
        self.raw_bits = 0.0
        self.final_bits = 0.0
        # rozbor hesla - znaky
        self.znaky = {}

        # slovnikový rozbor
        self.penalized_bits = 0.0
        self.penalized_coeficient = 1.0
        self.nalezena_slova = []
        self.slova = False

        if self.delka > 0:
            self.kontrola()
        else:
            self.score2 = "Heslo je prázdné"
            print("heslo je prázdné!")
            pass

    def kontrola(self):
        # běh funkce kontrola
        self.rozbor_pismen()
        self.potencialni_znaky()
        self.obsah_slovnikoveho_slova()
        self.entropie_znaku()
        self.penalizace()
        # for i in self.znaky:
        #     print(f"{i} je {self.znaky[i]}krát")

    def potencialni_znaky(self):
        if self.mala > 0:
            self.pot_zn += len(string.ascii_lowercase)
        if self.velka > 0:
            self.pot_zn += len(string.ascii_uppercase)
        if self.cislo > 0:
            self.pot_zn += len(string.digits)
        if self.spec > 0:
            self.pot_zn += len(string.punctuation)
        print(f"Potencialnich znaku je {self.pot_zn}")
        self.raw_bits = self.delka * math.log2(self.pot_zn)
        print(f"Entropie hesla je: {self.raw_bits}")

    def obsah_slovnikoveho_slova(self):

        with open(large_slovnik, "r", encoding="utf-8") as f:
            slovnik = f.read().splitlines()

        velikost_slovniku = len(slovnik)
        minimal_lenght = 3
        nalezeno = False

        heslo_lower = self.heslo.lower()
        self.slovnikova_penalizace = 0
        while True:
            nalezeno = False
            for slovo in slovnik:
                slovo_lower = slovo.lower()
                # print(slovo)
                if len(slovo) <= minimal_lenght:
                    continue
                elif slovo_lower in heslo_lower:
                    idx = slovnik.index(slovo) + 1
                    entropie_slova = (
                        math.log2(velikost_slovniku / idx) if idx > 1 else 1
                    )
                    self.nalezena_slova.append(
                        {"slovo": slovo, "index": idx, "entropie": entropie_slova}
                    )
                    heslo_lower = heslo_lower.replace(slovo_lower, "", 1)
                    nalezeno = True
                    self.penalized_bits += entropie_slova

                    # print(f"Slovo: {slovo}  a heslo {heslo_lower}")  # smazat
                    # print(f"index slova: {idx}")  # smazat
                    # print(f"Entropie: {entropie_slova}")  # smazat
                    # print(f"penalizace slovníke  m je: {self.penalized_bits}")  # smazat

            if not nalezeno:
                break

    def entropie_znaku(self):
        celkova_entropie_znaku = 0
        maximalni_entropie_znaku = -math.log2(1 / self.delka)

        print(f"max je asi {maximalni_entropie_znaku}")
        for i in self.znaky:
            p = self.znaky[i] / self.delka
            # print(f"Pecko je {p}")
            soucin = p * math.log2(p)
            # print(f"soucin je {soucin}")
            soucin = -soucin
            celkova_entropie_znaku += soucin
            # print(f"Celkova entropie znaku {celkova_entropie_znaku}")

        # vypocet procenta
        print(f"Celkova entropie znaku {celkova_entropie_znaku}")
        procento = celkova_entropie_znaku / maximalni_entropie_znaku
        self.penalized_coeficient = procento
        procento = procento * 100
        print(f"procento je {procento}%")

    # def potencialni_cas(self):
    #     self.cas = 2**self.raw_bits / 1e9
    #     self.sekundy = round(self.cas, 5)
    #     self.minuty = round(self.cas / 60, 2)
    #     self.hodiny = round(self.minuty / 60, 2)
    #     self.dny = round(self.hodiny / 24, 2)
    #     self.tydny = round(self.dny / 7, 2)
    #     self.mesice = round(self.tydny / 4, 2)
    #     self.roky = round(self.mesice / 12, 2)

    #     self.score += self.raw_bits
    #     self.cas_class = 0

    #     if self.roky > 1:
    #         if self.roky > 1000:
    #             if self.roky > 1000000:
    #                 if self.roky > 1000000000:
    #                     self.cas_t = f"Více jak miliarda let"
    #                     self.cas_class = 6

    #                 else:
    #                     miliony = round(self.roky / 1000000, 2)

    #                     self.cas_t = f"{miliony} Milionů let"
    #                     self.cas_class = 6
    #             else:
    #                 tisicileti = round(self.roky / 1000, 2)
    #                 self.cas_t = f"{tisicileti} Tisíc let"
    #                 self.cas_class = 6
    #         else:
    #             self.cas_t = f"{self.roky} Roků"
    #             self.cas_class = 5
    #     elif self.mesice > 1:
    #         self.cas_t = f"{self.mesice} Měsíců"
    #         self.cas_class = 4
    #     elif self.tydny > 1:
    #         self.cas_t = f"{self.tydny} Týdnů"
    #         self.cas_class = 3
    #     elif self.dny > 1:
    #         self.cas_t = f"{self.dny} Dnů"
    #         self.cas_class = 2
    #     elif self.hodiny > 1:
    #         self.cas_t = f"{self.hodiny} Hodin"
    #         self.cas_class = 2
    #     elif self.minuty > 1:
    #         self.cas_t = f"{self.minuty} Minut"
    #         self.cas_class = 1
    #     else:
    #         self.cas_t = f"{self.sekundy} Sekund"
    #         self.cas_class = 1
    #     self.cas2 = f"Maximální doba k prolomení hesla: {self.cas_t}"

    # print(sekundy , minuty, hodiny, dny, tydny, mesice, roky)

    def rozbor_pismen(self):
        for i in self.heslo:
            # print(self.znaky)
            if i in self.znaky:
                self.znaky[i] += 1
            else:
                self.znaky[i] = 1
            if self.minuly_znak_presne == i:
                self.pocet_minuly_presne += 1

            else:
                self.minuly_znak_presne = i
                self.pocet_minuly_presne = 0
            if i.islower():
                self.mala += 1
                if self.minuly_znak == "m":

                    self.pocet_minuly += 1
                else:

                    self.minuly_znak = "m"
                    self.pocet_minuly = 0
            if i.isupper():
                self.velka += 1
                if self.minuly_znak == "v":

                    self.pocet_minuly += 1
                else:

                    self.minuly_znak = "v"
                    self.pocet_minuly = 0
            if i.isdigit():
                self.cislo += 1
                if self.minuly_znak == "c":

                    self.pocet_minuly += 1
                else:

                    self.minuly_znak = "c"
                    self.pocet_minuly = 0

            if i in string.punctuation:
                self.spec += 1
                if self.minuly_znak == "s":

                    self.pocet_minuly += 1
                else:

                    self.minuly_znak = "s"
                    self.pocet_minuly = 0

    def penalizace(self):
        print(f"penalizace slovníkem je: {self.penalized_bits}")
        self.final_bits = self.raw_bits * self.penalized_coeficient
        self.final_bits = self.final_bits - self.penalized_bits
        print(f"Finální bity jsou: {self.final_bits}")

    # def vyhodnoceni(self):
    #     # vyhodnoceni
    #     if int(self.delka) < 8:
    #         self.delka2 = "je kratké (alespoň 8 znaků) "
    #     if int(self.delka) >= 8:
    #         self.delka2 = "je dostatečně dlouhé. "
    #     if int(self.mala) < 2:
    #         self.mala2 = "obsahuje málo malých písmen. (alespoň 2) "
    #     if int(self.mala) >= 2:
    #         self.mala2 = "obsahuje dostatečné množství malých písmen. "
    #     if int(self.cislo) < 2:
    #         self.cislo2 = "obsahuje málo čísel. (alespoň 2) "
    #     if int(self.cislo) >= 2:
    #         self.cislo2 = "obsahuje dostatek čísel. "
    #     if int(self.spec) < 2:
    #         self.spec2 = "obsahuje málo speciálních znaků(př. !@#$%^&*()_+-=[]{}|\\:;\"',.<>/?). (alespoň 2) "
    #     if int(self.spec) >= 2:
    #         self.spec2 = "obsahuje dostatečné množství speciálních znaků. "
    #     if int(self.velka) < 2:
    #         self.velka2 = "obsahuje málo velkých písmen. (alespoň 2) "
    #     if int(self.velka) >= 2:
    #         self.velka2 = "obsahuje dostatečné množstvívelkých písmen. "

    #     self.score = round(self.score, 2)
    #     if self.score < 0:
    #         self.score = 0

    #     if self.score > 100:
    #         self.score2 = f"Tvé heslo je extrémně silné. (score: {self.score})"
    #         self.score_class = 6
    #     elif self.score > 80:
    #         self.score2 = f"Tvé heslo je velmi silné. (score: {self.score})"
    #         self.score_class = 5
    #     elif self.score > 60:
    #         self.score2 = f"Tvé heslo je silné. (score: {self.score})"
    #         self.score_class = 4
    #     elif self.score > 40:
    #         self.score2 = f"Tvé heslo není silné. (score: {self.score})"
    #         self.score_class = 3
    #     elif self.score > 25:
    #         self.score2 = f"Tvé heslo je slabé. (score: {self.score})"
    #         self.score_class = 2
    #     elif self.score <= 25:
    #         self.score2 = f"Tvé heslo je velmi slabé. (score: {self.score})"
    #         self.score_class = 1


class Generator:
    def __init__(self):
        pass


class Ulozeni:
    def __init__(self):
        pass


class Nastaveni:
    def __init__(self):
        pass
