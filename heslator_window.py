from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader  # Nástroj pro načtení .ui
import zdroje_rc
import os
from heslator_logic import *
from heslator_ui import Ui_MainWindow


class Heslator(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.ui = Ui_MainWindow()  # test
        self.ui.setupUi(self)  # test

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
        # ------3 PENĚŽENKA------

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

    # ZPĚTNÉ BUTTONY DO MENU + login
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
        self.ui.penezenka_button_menu.clicked.connect(self.do_menu)
        print("penezenka")

    def do_menu(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        print("menu")

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

        # spustí na pozadí výpočet, zároveň loading animace.

        self.default_progress_bar()  # reset barvy
        heslo = self.ui.rozbor_input.text().strip()  # input hesla
        self.ui.rozbor_progressBar_sila.setRange(0, 0)  # loading animace progress baru
        self.worker_rozbor = Worker_Rozbor(Rozbor, heslo)  # worker pro výpočet(rozbpr)
        self.worker_rozbor.finished.connect(self.rozbor_dokoncen)
        # self.worker.error.connect(self.rozbor_chyba)
        self.worker_rozbor.finished.connect(self.worker_rozbor.deleteLater)
        self.ui.rozbor_label_heslo.setText(heslo)
        self.worker_rozbor.start()

    def rozbor_dokoncen(self, data):
        # výpis  hodnot po dokončení výpočtu

        # síla a progress bar
        self.ui.rozbor_label_score.setText(str(data["final_bits"]))
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
        # počty znaků (malá, velká, čísla a znaky)
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
            self.ui.rozbor_label_spec_hodnota.setText(str(data["velka"]) + "  🔴")
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

        # ------4 GENERÁTOR ------

    def generator_nabidka_heslo(self):
        self.ui.generator_widget_fraze.hide()
        self.ui.generator_widget_heslo.show()

    def generator_nabidka_fraze(self):
        self.ui.generator_widget_fraze.show()
        self.ui.generator_widget_heslo.hide()

        # ------5 INFO------
        # ------6 NASTAVENÍ------
