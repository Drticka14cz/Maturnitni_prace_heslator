from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader # Nástroj pro načtení .ui
import zdroje_rc
import os
from heslator_logic import *
from heslator_ui import Ui_MainWindow

class Heslator(QMainWindow):
    def __init__(self):
        super().__init__()
        #//------ NAČTENÍ UI + LOAD PROGRAMU------\\

        #STARÉ NAČÍTÁNÍ
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

        #NOVÉ NAČÍTÁNÍ
        self.ui = Ui_MainWindow()#test
        self.ui.setupUi(self)#test

        # //------NAČTENÍ ELEMENTŮ------\\
        self.ui.stackedWidget.setCurrentIndex(0 ) #INDEX STRÁNKY

        
        
        
        


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
        # ------3 PENĚŽENKA------



        # ------4 GENERÁTOR ------
        self.ui.generator_radioButton_heslo.toggled.connect(self.generator_nabidka_heslo)
        self.ui.generator_radioButton_fraze.toggled.connect(self.generator_nabidka_fraze)
        #připojení zpětného tlačítka do menu
        # self.ui.generator_widget_fraze.hide()
        self.ui.generator_widget_heslo.hide()
        # ------5 INFO------
        # ------6 NASTAVENÍ------
        
        
       
      
    #ZPĚTNÉ BUTTONY DO MENU + login    
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
        QApplication.processEvents() # <--- Donutí UI aktualizovat text ihned
        jmeno = self.ui.login_lineEdit_jmeno.text().strip()
        heslo = self.ui.login_lineEdit_heslo.text().strip()
        if jmeno and heslo:
            print("pokouším se přihlásit")
            lg = Login(jmeno, heslo)
            poznamka = lg.poznamka
            prihlasen = lg.prihlasen
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
            QApplication.processEvents() # <--- Donutí UI aktualizovat text ihned
            zl = New_account(jmeno, heslo, heslo_2)
            poznamka = zl.poznamka
            zalozeno = zl.zalozeni
            if zalozeno:
                print("Založeno")
            else:
                print("nezaloženo")
        # ------1 MENU------
        # ------2 ROZBOR------
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