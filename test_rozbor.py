import string
import math
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

dir_path = os.path.dirname(os.path.abspath(__file__))
work_dir = os.path.join(dir_path, "work_files")
large_slovnik = os.path.join(work_dir, "Pwdb_top-10000000.txt")
# with open(large_slovnik, "r", encoding="utf-8") as f:
#     slovnikk = f.read()
#     print(slovnikk)


class Rozbor:
    def __init__(self, heslo):

        self.heslo = heslo.strip()
        self.mala = 0
        self.velka = 0
        self.cislo = 0
        self.spec = 0
        self.delka = len(self.heslo)
        self.pot_zn = 0
        self.mala2 = " "
        self.velka2 = " "
        self.cislo2 = " "
        self.spec2 = " "
        self.delka2 = " "
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

        # slovnikový rozbor
        self.penalized_bits = 0.0
        self.nalezena_slova = []
        self.slova = False

        if self.delka > 0:
            self.kontrola()
        else:
            self.score2 = "Heslo je prázdné"
            pass

    def kontrola(self):
        # běh funkce kontrola
        self.rozbor_pismen()
        self.potencialni_znaky()
        self.obsah_slovnikoveho_slova()

    def potencialni_znaky(self):
        if self.mala > 0:
            self.pot_zn += len(string.ascii_lowercase)
        if self.velka > 0:
            self.pot_zn += len(string.ascii_uppercase)
        if self.cislo > 0:
            self.pot_zn += len(string.digits)
        if self.spec > 0:
            self.pot_zn += len(string.punctuation)
        print(self.pot_zn)
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

                    print(f"Slovo: {slovo}  a heslo {heslo_lower}")  # smazat
                    print(f"index slova: {idx}")  # smazat
                    print(f"Entropie: {entropie_slova}")  # smazat
                    print(f"penalizace slovníkem je: {self.penalized_bits}")  # smazat
            if not nalezeno:
                break

    def potencialni_cas(self):
        self.cas = 2**self.raw_bits / 1e9
        self.sekundy = round(self.cas, 5)
        self.minuty = round(self.cas / 60, 2)
        self.hodiny = round(self.minuty / 60, 2)
        self.dny = round(self.hodiny / 24, 2)
        self.tydny = round(self.dny / 7, 2)
        self.mesice = round(self.tydny / 4, 2)
        self.roky = round(self.mesice / 12, 2)

        self.score += self.raw_bits
        self.cas_class = 0

        if self.roky > 1:
            if self.roky > 1000:
                if self.roky > 1000000:
                    if self.roky > 1000000000:
                        self.cas_t = f"Více jak miliarda let"
                        self.cas_class = 6

                    else:
                        miliony = round(self.roky / 1000000, 2)

                        self.cas_t = f"{miliony} Milionů let"
                        self.cas_class = 6
                else:
                    tisicileti = round(self.roky / 1000, 2)
                    self.cas_t = f"{tisicileti} Tisíc let"
                    self.cas_class = 6
            else:
                self.cas_t = f"{self.roky} Roků"
                self.cas_class = 5
        elif self.mesice > 1:
            self.cas_t = f"{self.mesice} Měsíců"
            self.cas_class = 4
        elif self.tydny > 1:
            self.cas_t = f"{self.tydny} Týdnů"
            self.cas_class = 3
        elif self.dny > 1:
            self.cas_t = f"{self.dny} Dnů"
            self.cas_class = 2
        elif self.hodiny > 1:
            self.cas_t = f"{self.hodiny} Hodin"
            self.cas_class = 2
        elif self.minuty > 1:
            self.cas_t = f"{self.minuty} Minut"
            self.cas_class = 1
        else:
            self.cas_t = f"{self.sekundy} Sekund"
            self.cas_class = 1
        self.cas2 = f"Maximální doba k prolomení hesla: {self.cas_t}"

        # print(sekundy , minuty, hodiny, dny, tydny, mesice, roky)

    def rozbor_pismen(self):
        for i in self.heslo:
            if self.minuly_znak_presne == i:
                self.pocet_minuly_presne += 1
                if self.pocet_minuly_presne == 1:
                    self.score -= 0.5

                if self.pocet_minuly_presne == 2:
                    self.score -= 1

                if self.pocet_minuly_presne >= 3:
                    self.score -= self.pocet_minuly_presne / 2 + 0.5

            else:
                self.minuly_znak_presne = i
                self.pocet_minuly_presne = 0
            if i.islower():
                self.mala += 1
                if self.minuly_znak == "m":
                    if self.pocet_minuly >= 6:
                        self.score -= 2
                    elif self.pocet_minuly >= 3:
                        self.score -= 0.5
                    else:
                        self.score += 1
                    self.pocet_minuly += 1
                else:
                    self.score += 1.5
                    self.minuly_znak = "m"
                    self.pocet_minuly = 0
            if i.isupper():
                self.velka += 1
                if self.minuly_znak == "v":
                    if self.pocet_minuly >= 6:
                        self.score -= 2
                    elif self.pocet_minuly >= 3:
                        self.score -= 0.5
                    else:
                        self.score += 1
                    self.pocet_minuly += 1
                else:
                    self.score += 1.5
                    self.minuly_znak = "v"
                    self.pocet_minuly = 0
            if i.isdigit():
                self.cislo += 1
                if self.minuly_znak == "c":
                    if self.pocet_minuly >= 6:
                        self.score -= 2
                    elif self.pocet_minuly >= 3:
                        self.score -= 0.5
                    else:
                        self.score += 1
                    self.pocet_minuly += 1
                else:
                    self.score += 1.5
                    self.minuly_znak = "c"
                    self.pocet_minuly = 0

            if i in string.punctuation:
                self.spec += 1
                if self.minuly_znak == "s":
                    if self.pocet_minuly >= 6:
                        self.score -= 1.5
                    elif self.pocet_minuly >= 3:
                        self.score -= 0.5
                    else:
                        self.score += 1.5
                    self.pocet_minuly += 1
                else:
                    self.score += 2
                    self.minuly_znak = "s"
                    self.pocet_minuly = 0

    # penalizace za chybejici typy znaku
    def penalizace(self):
        if self.mala == 0:
            self.score -= 2
        if self.velka == 0:
            self.score -= 2
        if self.cislo == 0:
            self.score -= 2
        if self.spec == 0:
            self.score -= 2

    def vyhodnoceni(self):
        # vyhodnoceni
        if int(self.delka) < 8:
            self.delka2 = "je kratké (alespoň 8 znaků) "
        if int(self.delka) >= 8:
            self.delka2 = "je dostatečně dlouhé. "
        if int(self.mala) < 2:
            self.mala2 = "obsahuje málo malých písmen. (alespoň 2) "
        if int(self.mala) >= 2:
            self.mala2 = "obsahuje dostatečné množství malých písmen. "
        if int(self.cislo) < 2:
            self.cislo2 = "obsahuje málo čísel. (alespoň 2) "
        if int(self.cislo) >= 2:
            self.cislo2 = "obsahuje dostatek čísel. "
        if int(self.spec) < 2:
            self.spec2 = "obsahuje málo speciálních znaků(př. !@#$%^&*()_+-=[]{}|\\:;\"',.<>/?). (alespoň 2) "
        if int(self.spec) >= 2:
            self.spec2 = "obsahuje dostatečné množství speciálních znaků. "
        if int(self.velka) < 2:
            self.velka2 = "obsahuje málo velkých písmen. (alespoň 2) "
        if int(self.velka) >= 2:
            self.velka2 = "obsahuje dostatečné množstvívelkých písmen. "

        self.score = round(self.score, 2)
        if self.score < 0:
            self.score = 0

        if self.score > 100:
            self.score2 = f"Tvé heslo je extrémně silné. (score: {self.score})"
            self.score_class = 6
        elif self.score > 80:
            self.score2 = f"Tvé heslo je velmi silné. (score: {self.score})"
            self.score_class = 5
        elif self.score > 60:
            self.score2 = f"Tvé heslo je silné. (score: {self.score})"
            self.score_class = 4
        elif self.score > 40:
            self.score2 = f"Tvé heslo není silné. (score: {self.score})"
            self.score_class = 3
        elif self.score > 25:
            self.score2 = f"Tvé heslo je slabé. (score: {self.score})"
            self.score_class = 2
        elif self.score <= 25:
            self.score2 = f"Tvé heslo je velmi slabé. (score: {self.score})"
            self.score_class = 1


Rozbor("slaviajakub123passwordheslo")
