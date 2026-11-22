from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader  # Nástroj pro načtení .ui

import zdroje_rc
import os
from heslator_logic import *
from heslator_ui import Ui_MainWindow
import pyperclip


class Heslator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Přihlášeno = None
        # //------ NAČTENÍ UI + LOAD PROGRAMU------\\

        # STARÉ NAČÍTÁNÍ
        # adresar_skriptu = os.path.dirname(os.path.abspath(__file__))
        # cesta_k_ui = os.path.join(adresar_skriptu, "heslator.ui")
        # loader = QUiLoader()
        # ui_soubor = QFile(cesta_k_ui)
        # ui_soubor.open(QFile.ReadOnly)
        # self.ui = loader.load(ui_soubor)
        # ui_soubor.close()
        # self.resize(self.ui.size())
        # self.setWindowTitle(self.ui.windowTitle())
        # self.setCentralWidget(self.ui)

        # NOVÉ NAČÍTÁNÍ
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # //------NAČTENÍ ELEMENTŮ------\\
        self.ui.stackedWidget.setCurrentIndex(0)  # INDEX STRÁNKY

        # ------0 LOGIN------
        self.ui.login_button_do_zalozeni.clicked.connect(self.do_zalozeni)
        self.ui.login_button_prihlasit.clicked.connect(self.login)
        # ------- 7 ZALOŽENÍ ------
        self.ui.zalozeni_button_do_prihlaseni.clicked.connect(self.do_prihlaseni)
        self.ui.zalozeni_button_zalozit.clicked.connect(self.zalozeni)
        # ------1 MENU------
        self.ui.menu_button_generator.clicked.connect(self.do_generator)
        self.ui.menu_button_rozbor.clicked.connect(self.do_rozbor)
        self.ui.menu_button_info.clicked.connect(self.do_info)
        self.ui.menu_button_nastaveni.clicked.connect(self.do_nastaveni)
        self.ui.menu_button_penezenka.clicked.connect(self.do_penezenka)
        # ------2 ROZBOR------
        self.ui.rozbor_button_rozebrat.clicked.connect(self.rozbor)
        self.zobrazit_historii = False
        self.ui.rozbor_button_historie_zobrazit.clicked.connect(
            self.rozbor_prepnout_historii
        )
        self.ui.rozbor_button_historie_delete.clicked.connect(self.smazat_historii)

        self.historie_rozbor_widget = (
            self.ui.scrollAreaWidgetContents
        )  # pro zobrazení historie rozboru - definice layoutu atd
        self.historie_rozbor_widget_laout = QVBoxLayout(self.historie_rozbor_widget)
        # ------3 PENĚŽENKA------
        self.ui.penezenka_button_ulozit.clicked.connect(self.penezenka)
        self.penezenka_widget_laout = QVBoxLayout(self.ui.penezenka_widget)

        # ------4 GENERÁTOR ------
        self.ui.generator_radioButton_heslo.toggled.connect(
            self.generator_nabidka_heslo
        )
        self.ui.generator_radioButton_fraze.toggled.connect(
            self.generator_nabidka_fraze
        )
        # připojení zpětného tlačítka do menu
        # self.ui.generator_widget_fraze.hide()
        self.ui.generator_widget_heslo.hide()
        # ------5 INFO------
        # ------6 NASTAVENÍ------

    #
    # ZPĚTNÉ BUTTONY DO MENU + login
    #
    def do_prihlaseni(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def do_zalozeni(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def do_generator(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.generator_button_menu.clicked.connect(self.do_menu)
        print("generator")

    def do_rozbor(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.rozbor_button_menu.clicked.connect(self.do_menu)
        print("rozbor")

    def do_info(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.info_button_menu.clicked.connect(self.do_menu)
        print("info")

    def do_nastaveni(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.nastaveni_button_menu.clicked.connect(self.do_menu)
        print("nastaveni")

    def do_penezenka(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.zobrazit_penezenku()
        self.ui.penezenka_button_menu.clicked.connect(self.do_menu)
        print("penezenka")

    def do_menu(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        print("menu")

    # //----- FUNKCE JEDNOTLIVÝCH STRÁNEK -----\\

    # ------0 LOGIN------

    def login(self):
        self.ui.login_label_poznamka.setText("Přihlašuji...")
        QApplication.processEvents()  # <--- Donutí UI aktualizovat text ihned
        jmeno = self.ui.login_lineEdit_jmeno.text().strip()
        heslo = self.ui.login_lineEdit_heslo.text().strip()
        if jmeno and heslo:
            print("pokouším se přihlásit")
            lg = Login(jmeno, heslo)
            poznamka = lg.poznamka
            prihlasen = lg.prihlasen
            self.Přihlášeno = lg.Prihlaseno
            print(f"self.přihlášeno: {self.Přihlášeno.key}")

            if prihlasen:
                self.ui.stackedWidget.setCurrentIndex(1)
            else:

                self.ui.login_label_poznamka.setText(poznamka)
        else:
            self.ui.login_label_poznamka.setText("Nebylo vyplněno jméno a heslo")

            # ------7 ZALOŽENÍ ------

    def zalozeni(self):
        print("wadawd")
        jmeno = self.ui.zalozeni_lineEdit_jmeno.text().strip()
        heslo = self.ui.zalozeni_lineEdit_heslo.text().strip()
        heslo_2 = self.ui.zalozeni_lineEdit_heslo_znovu.text().strip()

        if jmeno and heslo and heslo_2:
            print("zakládám...")
            self.ui.zalozeni_label_poznamka.setText("Zakládám...")
            QApplication.processEvents()  # <--- Donutí UI aktualizovat text ihned
            zl = New_account(jmeno, heslo, heslo_2)
            poznamka = zl.poznamka
            zalozeno = zl.zalozeni
            if zalozeno:
                print("Založeno")
            else:
                print("nezaloženo")
        # ------1 MENU------
        # ------2 ROZBOR------

    def rozbor(self):
        # Funkce která se sputsí hned po kliku na button
        if self.zobrazit_historii == True:
            self.rozbor_zobrazit_historii()
        # Loadnutí již kontrolovaných dat

        # spustí na pozadí výpočet, zároveň loading animace.

        self.default_progress_bar()  # reset barvy
        heslo = self.ui.rozbor_input.text().strip()  # input hesla
        self.ui.rozbor_progressBar_sila.setRange(0, 0)
        self.ui.rozbor_progressBar_delka.setRange(0, 0)
        self.ui.rozbor_progressBar_cas.setRange(0, 0)  # loading animace progress baru
        self.worker_rozbor = Worker_Rozbor(
            Rozbor, heslo, self.Přihlášeno
        )  # worker pro výpočet(rozbpr)
        self.worker_rozbor.finished.connect(self.rozbor_dokoncen)
        # self.worker.error.connect(self.rozbor_chyba)
        self.worker_rozbor.finished.connect(self.worker_rozbor.deleteLater)
        self.ui.rozbor_label_heslo.setText(heslo)
        self.worker_rozbor.start()

    def smazat_historii(self):
        data, uspech, klic, salt = load_data(
            self.Přihlášeno.user_dir_path,
            key=self.Přihlášeno.key,
            salt=self.Přihlášeno.salt,
        )
        data["historie_rozbor"] = []
        save_data(
            self.Přihlášeno.user_dir_path,
            data,
            self.Přihlášeno.key,
            self.Přihlášeno.salt,
            heslo=None,
        )
        self.zobrazit_historii = True
        self.rozbor_zobrazit_historii()

    def rozbor_prepnout_historii(self):
        if self.Přihlášeno is None:
            pass
        else:
            self.zobrazit_historii = not self.zobrazit_historii
            self.rozbor_zobrazit_historii()

    def rozbor_zobrazit_historii(self):
        if self.zobrazit_historii == False:
            self.ui.scrollAreaWidgetContents.setVisible(False)
            return

        ######
        self.ui.scrollAreaWidgetContents.setVisible(True)
        data, uspech, klic, salt = load_data(
            self.Přihlášeno.user_dir_path,
            key=self.Přihlášeno.key,
            salt=self.Přihlášeno.salt,
        )
        print(f"Načetl jsem data: {data}")
        # print(
        #     f" rozbor zobrazení load vrací data: {data}\n pak vrací uspech: {uspech} \n pak klic {klic} \n pak sul {salt}"
        # )

        while self.historie_rozbor_widget_laout.count():
            polozka = self.historie_rozbor_widget_laout.takeAt(0)
            widget = polozka.widget()
            if widget is not None:
                widget.deleteLater()
        index = -1
        for i in data["historie_rozbor"]:
            index += 1
            print(f"i = {i}")

            radek_kontrola = QFrame()
            layout = QHBoxLayout(radek_kontrola)

            radek_kontrola.setStyleSheet("""
            QFrame {
            background-color: #494948;
            border: 1px solid  #3a3a39;
            border-radius: 8px;
            margin:2px;
            margin-bottom: 5px;
        }
        QLabel{
        font-size:10px;
        color:#ffffff;
        border: 0px solid black
        }
    """)

            zobrazene_heslo = QLabel(i["heslo"])
            zobrazena_sila = QLabel(str(i["final_bits"]))
            zobrazeny_cas = QLabel(i["cas"])
            kopirovat = QPushButton("Kopírovat")
            kopirovat.clicked.connect(
                lambda checked=False, heslo=i[
                    "heslo"
                ], w=radek_kontrola: self.kopirovat_radek_historie(heslo)
            )
            smazat = QPushButton("Smazat")
            smazat.clicked.connect(
                lambda checked=False, cas_zaznamu=i[
                    "cas"
                ], w=radek_kontrola: self.smazat_radek_historie(w, cas_zaznamu)
            )
            layout.addWidget(zobrazene_heslo)
            layout.addWidget(zobrazena_sila)
            layout.addWidget(zobrazeny_cas)
            layout.addWidget(kopirovat)
            layout.addWidget(smazat)

            self.historie_rozbor_widget_laout.addWidget(radek_kontrola)

    ######
    def smazat_radek_historie(self, w, cas_zaznamu):
        # 1. Načteme aktuální data
        data, uspech, klic, salt = load_data(
            self.Přihlášeno.user_dir_path,
            key=self.Přihlášeno.key,
            salt=self.Přihlášeno.salt,
        )

        if data and "historie_rozbor" in data:
            # 2. Smažeme prvek podle unikátního času (zabrání IndexError)
            data["historie_rozbor"] = [
                zaznam
                for zaznam in data["historie_rozbor"]
                if zaznam["cas"] != cas_zaznamu
            ]

            # 3. Uložíme změny
            save_data(
                user_dir_path=self.Přihlášeno.user_dir_path,
                data=data,
                key=self.Přihlášeno.key,
                salt=self.Přihlášeno.salt,
                heslo=None,
            )

        w.deleteLater()
        self.rozbor_zobrazit_historii()

    def kopirovat_radek_historie(self, heslo):
        QApplication.clipboard().setText(heslo)

    def rozbor_dokoncen(self, data):
        # výpis  hodnot po dokončení výpočtu

        print(f"V rozbor dokončen jsme dostali data což je: {data}")

        # síla a progress bar
        self.ui.rozbor_label_score.setText(f"Síla: {data['final_bits']} bitů")
        self.ui.rozbor_progressBar_sila.setRange(
            0, 150
        )  # nastaví minimální a maximální hodnotu pro progressbar

        self.ui.rozbor_progressBar_sila.setValue(data["final_bits"])
        self.ui.rozbor_progressBar_sila.setFormat("%v")
        self.ui.rozbor_progressBar_sila.setStyleSheet(f"""
        /* PROGRESS BAR*/
QProgressBar{{
border: 2px solid  black;
border-radius:8px;
height:5px;
text-align: center
}}
QProgressBar::chunk{{
background-color:{data["barva_sily"]};/* Mění barvu progress baru*/
width:5px;
}}


""")
        # ČAS - progressbar a popisek
        self.ui.rozbor_progressBar_cas.setRange(0, 7)
        self.ui.rozbor_progressBar_cas.setValue(data["cas_class"])
        self.ui.rozbor_progressBar_cas.setFormat("%v")
        self.ui.rozbor_progressBar_cas.setStyleSheet(f"""
        /* PROGRESS BAR*/
        QProgressBar{{
        border: 2px solid  black;
        border-radius:8px;
        height:5px;
        text-align: center
        }}
        QProgressBar::chunk{{
        background-color:{data["barva_sily"]};/* Mění barvu progress baru*/
        width:5px;
        }}""")

        self.ui.rozbor_label_cas.setText(data["cas"])

        # počty znaků (malá, velká, čísla a znaky)

        self.ui.rozbor_progressBar_delka.setRange(0, 40)
        self.ui.rozbor_progressBar_delka.setValue(data["delka"])
        self.ui.rozbor_progressBar_delka.setFormat("%v")
        self.ui.rozbor_progressBar_delka.setStyleSheet(f"""
        /* PROGRESS BAR*/
        QProgressBar{{
        border: 2px solid  black;
        border-radius:8px;
        height:5px;
        text-align: center
        }}
        QProgressBar::chunk{{
        background-color:{data["barva_sily"]};/* Mění barvu progress baru*/
        width:5px;
        }}""")

        if data["mala"] > 0:
            self.ui.rozbor_label_mala_hodnota.setText(str(data["mala"]) + "  🟢")
        else:
            self.ui.rozbor_label_mala_hodnota.setText(str(data["mala"]) + "  🔴")
        if data["velka"] > 0:
            self.ui.rozbor_label_velka_hodnota.setText(str(data["velka"]) + "  🟢")
        else:
            self.ui.rozbor_label_velka_hodnota.setText(str(data["velka"]) + "  🔴")
        if data["spec"] > 0:
            self.ui.rozbor_label_spec_hodnota.setText(str(data["spec"]) + "  🟢")
        else:
            self.ui.rozbor_label_spec_hodnota.setText(str(data["spec"]) + "  🔴")
        if data["cisla"] > 0:
            self.ui.rozbor_label_cisla_hodnota.setText(str(data["cisla"]) + "  🟢")
        else:
            self.ui.rozbor_label_cisla_hodnota.setText(str(data["cisla"]) + "  🔴")
        # slovníková slova
        nalezena_slova = ""
        # print("nacházím slova: \n \n \n")
        # print(str(data["nalezena_slova"]["slovo"]))
        for i in data["nalezena_slova"]:
            # print(i["slovo"])
            if nalezena_slova == "":
                nalezena_slova = i["slovo"]
            else:
                nalezena_slova = nalezena_slova + ", " + i["slovo"]

        self.ui.rozbor_label_slovnikova_hodnota.setText(nalezena_slova)
        print("Volám zobrazit historii v dokončeném rozboru")
        self.rozbor_zobrazit_historii()

    def default_progress_bar(self):
        self.ui.rozbor_progressBar_sila.setStyleSheet(f"""
                /* PROGRESS BAR*/
        QProgressBar{{
        border: 2px solid  black;
        border-radius:8px;
        height:5px;
        text-align: center
        }}
        QProgressBar::chunk{{
        background-color:black;/* Mění barvu progress baru*/
        width:5px;
        }}
        
        
        """)

    def rozbor_chyba(self):
        print("chyba v rozboru")

        # ------3 PENĚŽENKA------

    def penezenka(self):
        heslo = self.ui.penezenka_heslo_input.text().strip()
        jmeno = self.ui.penezenka_jmeno_input.text().strip()
        poznamka = self.ui.penezenka_poznamka_poznamka.text().strip()
        platforma = self.ui.penezenka_platforma_input.text().strip()
        print("posílám uložit... Prayge")
        Ulozeni(jmeno, heslo, platforma, poznamka, self.Přihlášeno, False)
        self.zobrazit_penezenku()

    def zobrazit_penezenku(self):
        data, uspech, klic, salt = load_data(
            self.Přihlášeno.user_dir_path,
            key=self.Přihlášeno.key,
            salt=self.Přihlášeno.salt,
        )
        print(f"Načetl jsem data: {data}")
        while self.penezenka_widget_laout.count():
            polozka = self.penezenka_widget_laout.takeAt(0)
            widget = polozka.widget()
            if widget is not None:
                widget.deleteLater()
        index = -1
        for i in data["ulozena_hesla"]:
            index += 1
            print(f"i = {i}")

            ulozeny_radek = QFrame()  # něco se zde nezobrazuje, idk co
            ulozeny_radek.setMinimumHeight(48)
            layout = QHBoxLayout(ulozeny_radek)

            ulozeny_radek.setStyleSheet("""
            QFrame {
            background-color: #494948;
            border: 1px solid  #3a3a39;
            border-radius: 8px;
            margin:2px;
            margin-bottom: 5px;
            }
            QLabel{
            font-size:12px;
            color:#ffffff;
            border: 0px solid black
            }
            QPushButton{
            background-color: #494948;
            font-size:10px;
            color:#ffffff;
            border: 0px solid black
            }
            """)

            zobrazene_heslo = QPushButton(i["heslo"])
            zobrazene_jmeno = QPushButton(i["jmeno"])
            zobrazena_platforma = QPushButton(i["platforma"])
            zobrazeny_poznamka = QPushButton(i["poznamka"])

            zobrazene_heslo.clicked.connect(
                lambda checked=False, heslo=i[
                    "heslo"
                ], w=ulozeny_radek: self.kopirovat_radek_historie(heslo)
            )
            smazat = QPushButton("Smazat")
            smazat.clicked.connect(
                lambda checked=False, cas_zaznamu=i[
                    "cas"
                ], w=ulozeny_radek: self.smazat_radek_historie(w, cas_zaznamu)
            )
            layout.addWidget(zobrazena_platforma)
            layout.addWidget(zobrazene_jmeno)
            layout.addWidget(zobrazene_heslo)

            layout.addWidget(zobrazeny_poznamka)

            layout.addWidget(smazat)

            self.penezenka_widget_laout.addWidget(ulozeny_radek)

        # ------4 GENERÁTOR ------

    def generator_nabidka_heslo(self):
        self.ui.generator_widget_fraze.hide()
        self.ui.generator_widget_heslo.show()

    def generator_nabidka_fraze(self):
        self.ui.generator_widget_fraze.show()
        self.ui.generator_widget_heslo.hide()

        # ------5 INFO------
        # ------6 NASTAVENÍ------
