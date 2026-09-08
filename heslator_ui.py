# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'heslator.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import zdroje_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"\n"
"/* TEXT NORMAL*/\n"
"QLabel{\n"
"font-size:11pt;\n"
"padding:1px;\n"
"\n"
"}\n"
"\n"
"/* PUSH BUTTON*/\n"
"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:800;\n"
"background-color:#3a3a39;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"}\n"
"\n"
"/* CHECCK BOX CSS*/\n"
"QCheckBox {\n"
"    padding: 5px;\n"
" font-size: 11pt;\n"
"\n"
"}\n"
"QCheckBox::indicator {\n"
"    background-color: #F0F7F4;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border: 2px solid #3a3a39;\n"
"    border-radius: 4px;\n"
"    transition: width 400ms ease-in-out, height 400ms ease-in-out, border 400ms ease-in-out;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    width: 19px;         \n"
"    height: 19px;\n"
"   border: none;    \n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/check_3.png);\n"
"    border: 2px solid #3a3a39;\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    borde"
                        "r: none;\n"
"}\n"
"/*RADIO BUTTON CSS */\n"
"QRadioButton{\n"
"spacing:5px;\n"
"color:black;\n"
"font-size: 11pt;\n"
"}\n"
"QRadioButton::indicator{\n"
"width: 15px;\n"
"height:15px;\n"
"border: 2px solid #3a3a39;\n"
"border-radius: 9px;\n"
"background-color: #F0F7F4;\n"
"transition: background-color 400ms ease-in-out, border 400ms ease-in-out;\n"
"}\n"
"QRadioButton:indicator:hover{\n"
"border-color:none\n"
"}\n"
"\n"
"QRadioButton:indicator:checked{\n"
"	image: url(:/icons/radio_2.png);\n"
"}\n"
"\n"
"/* LINE EDIT	*/\n"
"QLineEdit{\n"
"background-color:#F0F7F4;\n"
"border: 1px solid #3a3a39;\n"
"border-radius: 3px;\n"
"padding:2px 4px;;\n"
"selection-background-color: #3a3a39;\n"
"transition: 400ms ease-in-out;\n"
"}\n"
"/* hover a nakliknut\u00ed */\n"
"QLineEdit:focus, QLineEdit:hover{\n"
"border:none;\n"
"}\n"
"\n"
"/* SLIDER */\n"
"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    background: #3a3a39;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"/* 2. Nevypln\u011bn\u00e1 \u010d\u00e1st (vprav"
                        "o od \u00fachytu) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #F0F7F4 ;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/* 3. Vypln\u011bn\u00e1 \u010d\u00e1st (vlevo od \u00fachytu - ukazuje hodnotu) */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #3a3a39;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* 4. \u00dachyt / Kole\u010dko, za kter\u00e9 se tah\u00e1 */\n"
"QSlider::handle:horizontal {\n"
"    background: #F0F7F4;\n"
"    border: 3px solid #3a3a39 ;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"         margin: -4px 0;           /* Vyrovn\u00e1n\u00ed: posune \u00fachyt na st\u0159ed li\u0161ty */\n"
"    border-radius:6px;              /* Ud\u011bl\u00e1 z \u00fachytu kruh */\n"
"}\n"
"\n"
"/* 5. Hover efekt pro \u00fachyt */\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #3a3a39;\n"
"    border: 3px solid #F0F7F4;\n"
"border-radius:6px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(800, 400))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"\n"
"#stackedWidget{\n"
"background-color: #3a3a39;\n"
"\n"
"}\n"
"#stackedWidget > QWidget{\n"
"background-color: #3a3a39;\n"
"\n"
"}")
        self.log_in = QWidget()
        self.log_in.setObjectName(u"log_in")
        self.gridLayout = QGridLayout(self.log_in)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_58 = QWidget(self.log_in)
        self.widget_58.setObjectName(u"widget_58")
        self.gridLayout_22 = QGridLayout(self.widget_58)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setHorizontalSpacing(0)
        self.gridLayout_22.setVerticalSpacing(50)
        self.gridLayout_22.setContentsMargins(100, 80, 100, 80)
        self.widget_59 = QWidget(self.widget_58)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setStyleSheet(u"#widget_59{\n"
"\n"
"    background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_59)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.widget_61 = QWidget(self.widget_59)
        self.widget_61.setObjectName(u"widget_61")
        self.verticalLayout_4 = QVBoxLayout(self.widget_61)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_9 = QLabel(self.widget_61)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.login_lineEdit_jmeno = QLineEdit(self.widget_61)
        self.login_lineEdit_jmeno.setObjectName(u"login_lineEdit_jmeno")

        self.verticalLayout_4.addWidget(self.login_lineEdit_jmeno)


        self.verticalLayout.addWidget(self.widget_61)

        self.widget_60 = QWidget(self.widget_59)
        self.widget_60.setObjectName(u"widget_60")
        self.verticalLayout_3 = QVBoxLayout(self.widget_60)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.widget_60)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.login_lineEdit_heslo = QLineEdit(self.widget_60)
        self.login_lineEdit_heslo.setObjectName(u"login_lineEdit_heslo")

        self.verticalLayout_3.addWidget(self.login_lineEdit_heslo)


        self.verticalLayout.addWidget(self.widget_60)

        self.login_label_poznamka = QLabel(self.widget_59)
        self.login_label_poznamka.setObjectName(u"login_label_poznamka")

        self.verticalLayout.addWidget(self.login_label_poznamka, 0, Qt.AlignmentFlag.AlignHCenter)

        self.login_button_prihlasit = QPushButton(self.widget_59)
        self.login_button_prihlasit.setObjectName(u"login_button_prihlasit")

        self.verticalLayout.addWidget(self.login_button_prihlasit)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)

        self.gridLayout_22.addWidget(self.widget_59, 0, 0, 1, 1)

        self.widget_62 = QWidget(self.widget_58)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setStyleSheet(u"#widget_62{\n"
"\n"
"    background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.widget_62)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_21 = QLabel(self.widget_62)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_5.addWidget(self.label_21, 0, Qt.AlignmentFlag.AlignHCenter)

        self.login_button_do_zalozeni = QPushButton(self.widget_62)
        self.login_button_do_zalozeni.setObjectName(u"login_button_do_zalozeni")

        self.verticalLayout_5.addWidget(self.login_button_do_zalozeni)


        self.gridLayout_22.addWidget(self.widget_62, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_58, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.log_in)
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"#menu > QWidget{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.menu)
        self.gridLayout_4.setSpacing(40)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(30, 15, 30, 15)
        self.widget_5 = QWidget(self.menu)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"QLabel{\n"
"color:black	;\n"
"	font: 500 18pt \"Verdana\";\n"
"}")

        self.horizontalLayout_7.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_4.addWidget(self.widget_5, 0, 0, 1, 2)

        self.widget_4 = QWidget(self.menu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget{\n"
"background-color:none;\n"
"}\n"
"#widget_4 > QWidget{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setSpacing(20)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_8 = QGridLayout(self.widget_6)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:800;\n"
"background-color:#3a3a39;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.widget_11)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.menu_button_quickGen = QPushButton(self.widget_11)
        self.menu_button_quickGen.setObjectName(u"menu_button_quickGen")

        self.verticalLayout_7.addWidget(self.menu_button_quickGen)

        self.menu_button_quickCopy = QPushButton(self.widget_11)
        self.menu_button_quickCopy.setObjectName(u"menu_button_quickCopy")

        self.verticalLayout_7.addWidget(self.menu_button_quickCopy)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.gridLayout_8.addWidget(self.widget_11, 1, 0, 2, 1)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 1, 1, 2, 2)


        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_9 = QGridLayout(self.widget_7)
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(10, 10, 10, 10)
        self.widget_12 = QWidget(self.widget_7)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:800;\n"
"background-color:#3a3a39;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.widget_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_6 = QSpacerItem(20, 55, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.menu_button_quickSave = QPushButton(self.widget_12)
        self.menu_button_quickSave.setObjectName(u"menu_button_quickSave")

        self.verticalLayout_8.addWidget(self.menu_button_quickSave)

        self.menu_button_quickReset = QPushButton(self.widget_12)
        self.menu_button_quickReset.setObjectName(u"menu_button_quickReset")

        self.verticalLayout_8.addWidget(self.menu_button_quickReset)

        self.verticalSpacer_5 = QSpacerItem(20, 54, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)


        self.gridLayout_9.addWidget(self.widget_12, 1, 0, 1, 1)

        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.widget_13 = QWidget(self.widget_7)
        self.widget_13.setObjectName(u"widget_13")

        self.gridLayout_9.addWidget(self.widget_13, 1, 1, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 1)
        self.gridLayout_9.setColumnStretch(1, 2)

        self.gridLayout_3.addWidget(self.widget_7, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 1, 1, 4, 1)

        self.widget_14 = QWidget(self.menu)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_9 = QVBoxLayout(self.widget_14)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_25)

        self.widget = QWidget(self.widget_14)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.menu_button_generator = QPushButton(self.widget)
        self.menu_button_generator.setObjectName(u"menu_button_generator")

        self.gridLayout_5.addWidget(self.menu_button_generator, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.widget_2 = QWidget(self.widget_14)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.menu_button_penezenka = QPushButton(self.widget_2)
        self.menu_button_penezenka.setObjectName(u"menu_button_penezenka")

        self.gridLayout_6.addWidget(self.menu_button_penezenka, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.widget_3 = QWidget(self.widget_14)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.menu_button_rozbor = QPushButton(self.widget_3)
        self.menu_button_rozbor.setObjectName(u"menu_button_rozbor")

        self.gridLayout_7.addWidget(self.menu_button_rozbor, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_3)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_10)

        self.widget_8 = QWidget(self.widget_14)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.menu_button_nastaveni = QPushButton(self.widget_9)
        self.menu_button_nastaveni.setObjectName(u"menu_button_nastaveni")

        self.horizontalLayout_9.addWidget(self.menu_button_nastaveni)


        self.horizontalLayout_3.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.menu_button_info = QPushButton(self.widget_10)
        self.menu_button_info.setObjectName(u"menu_button_info")

        self.horizontalLayout_10.addWidget(self.menu_button_info)


        self.horizontalLayout_3.addWidget(self.widget_10)


        self.verticalLayout_9.addWidget(self.widget_8)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_11)


        self.gridLayout_4.addWidget(self.widget_14, 1, 0, 4, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 4)
        self.gridLayout_4.setRowStretch(2, 4)
        self.gridLayout_4.setRowStretch(3, 4)
        self.gridLayout_4.setRowStretch(4, 4)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.stackedWidget.addWidget(self.menu)
        self.rozbor = QWidget()
        self.rozbor.setObjectName(u"rozbor")
        self.verticalLayout_19 = QVBoxLayout(self.rozbor)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.rozbor)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_12 = QGridLayout(self.widget_15)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(40)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(30, 15, 30, 15)
        self.scrollArea_2 = QScrollArea(self.widget_15)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea{\n"
"background-color:#3a3a39;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 384, 730))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"#scrollAreaWidgetContents_4 >QWidget{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}\n"
"#scrollAreaWidgetContents_4 {\n"
"background-color:#3a3a39;\n"
"}\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.widget_17 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 700))
        self.verticalLayout_12 = QVBoxLayout(self.widget_17)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.widget_nadpis = QWidget(self.widget_17)
        self.widget_nadpis.setObjectName(u"widget_nadpis")
        self.widget_nadpis.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_nadpis)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(4, 4, 4, 16)
        self.label_12 = QLabel(self.widget_nadpis)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.rozbor_label_heslo = QLabel(self.widget_nadpis)
        self.rozbor_label_heslo.setObjectName(u"rozbor_label_heslo")

        self.horizontalLayout_11.addWidget(self.rozbor_label_heslo)


        self.verticalLayout_12.addWidget(self.widget_nadpis)

        self.widget_24 = QWidget(self.widget_17)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_13 = QVBoxLayout(self.widget_24)
        self.verticalLayout_13.setSpacing(8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_24)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_13.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.rozbor_progressBar_sila = QProgressBar(self.widget_24)
        self.rozbor_progressBar_sila.setObjectName(u"rozbor_progressBar_sila")
        self.rozbor_progressBar_sila.setValue(24)

        self.verticalLayout_13.addWidget(self.rozbor_progressBar_sila)

        self.rozbor_label_score = QLabel(self.widget_24)
        self.rozbor_label_score.setObjectName(u"rozbor_label_score")

        self.verticalLayout_13.addWidget(self.rozbor_label_score)

        self.rozbor_label_popisSily = QLabel(self.widget_24)
        self.rozbor_label_popisSily.setObjectName(u"rozbor_label_popisSily")

        self.verticalLayout_13.addWidget(self.rozbor_label_popisSily)


        self.verticalLayout_12.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_17)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_14 = QVBoxLayout(self.widget_25)
        self.verticalLayout_14.setSpacing(8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_25)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_14.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.rozbor_progressBar_cas = QProgressBar(self.widget_25)
        self.rozbor_progressBar_cas.setObjectName(u"rozbor_progressBar_cas")
        self.rozbor_progressBar_cas.setValue(24)

        self.verticalLayout_14.addWidget(self.rozbor_progressBar_cas)

        self.rozbor_label_cas = QLabel(self.widget_25)
        self.rozbor_label_cas.setObjectName(u"rozbor_label_cas")

        self.verticalLayout_14.addWidget(self.rozbor_label_cas)

        self.rozbor_label_popisCasu = QLabel(self.widget_25)
        self.rozbor_label_popisCasu.setObjectName(u"rozbor_label_popisCasu")

        self.verticalLayout_14.addWidget(self.rozbor_label_popisCasu)


        self.verticalLayout_12.addWidget(self.widget_25)

        self.widget_27 = QWidget(self.widget_17)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_15 = QVBoxLayout(self.widget_27)
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_27)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.rozbor_label_delka = QLabel(self.widget_16)
        self.rozbor_label_delka.setObjectName(u"rozbor_label_delka")

        self.horizontalLayout_8.addWidget(self.rozbor_label_delka)


        self.verticalLayout_15.addWidget(self.widget_16)

        self.widget_31 = QWidget(self.widget_27)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.rozbor_label_mala = QLabel(self.widget_31)
        self.rozbor_label_mala.setObjectName(u"rozbor_label_mala")

        self.horizontalLayout_13.addWidget(self.rozbor_label_mala)


        self.verticalLayout_15.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.widget_27)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.rozbor_label_velka = QLabel(self.widget_32)
        self.rozbor_label_velka.setObjectName(u"rozbor_label_velka")

        self.horizontalLayout_15.addWidget(self.rozbor_label_velka)


        self.verticalLayout_15.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.widget_27)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.rozbor_label_cisla = QLabel(self.widget_33)
        self.rozbor_label_cisla.setObjectName(u"rozbor_label_cisla")

        self.horizontalLayout_16.addWidget(self.rozbor_label_cisla)


        self.verticalLayout_15.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.widget_27)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.rozbor_label_spec = QLabel(self.widget_34)
        self.rozbor_label_spec.setObjectName(u"rozbor_label_spec")

        self.horizontalLayout_17.addWidget(self.rozbor_label_spec)


        self.verticalLayout_15.addWidget(self.widget_34)

        self.widget_35 = QWidget(self.widget_27)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.rozbor_label_slovnikova = QLabel(self.widget_35)
        self.rozbor_label_slovnikova.setObjectName(u"rozbor_label_slovnikova")

        self.horizontalLayout_18.addWidget(self.rozbor_label_slovnikova)


        self.verticalLayout_15.addWidget(self.widget_35)


        self.verticalLayout_12.addWidget(self.widget_27)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 3)
        self.verticalLayout_12.setStretch(2, 3)
        self.verticalLayout_12.setStretch(3, 4)

        self.verticalLayout_16.addWidget(self.widget_17)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_9)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_12.addWidget(self.scrollArea_2, 0, 1, 1, 1)

        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_2 = QVBoxLayout(self.widget_18)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_10 = QVBoxLayout(self.widget_19)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 10)
        self.widget_21 = QWidget(self.widget_19)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_11 = QVBoxLayout(self.widget_21)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.widget_21)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setStyleSheet(u"QWidget{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.widget_28)
        self.gridLayout_16.setSpacing(10)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(10, 10, 10, 10)
        self.rozbor_button_menu = QPushButton(self.widget_28)
        self.rozbor_button_menu.setObjectName(u"rozbor_button_menu")
        self.rozbor_button_menu.setMinimumSize(QSize(35, 35))
        self.rozbor_button_menu.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"font-weight:800;\n"
"border: 5px solid  #3a3a39;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:1600;\n"
"background-color:#3a3a39;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"\n"
"\n"
"}")

        self.gridLayout_16.addWidget(self.rozbor_button_menu, 1, 0, 1, 1)

        self.widget_30 = QWidget(self.widget_28)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_5 = QLabel(self.widget_30)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"color:black	;\n"
"	font: 500 18pt \"Verdana\";\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_16.addWidget(self.widget_30, 1, 1, 1, 1)

        self.gridLayout_16.setColumnStretch(0, 1)
        self.gridLayout_16.setColumnStretch(1, 5)

        self.verticalLayout_11.addWidget(self.widget_28, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_29 = QWidget(self.widget_21)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setStyleSheet(u"#widget_29{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.widget_29)
        self.verticalLayout_17.setSpacing(20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(15, 15, 15, 15)
        self.rozbor_input = QLineEdit(self.widget_29)
        self.rozbor_input.setObjectName(u"rozbor_input")

        self.verticalLayout_17.addWidget(self.rozbor_input)

        self.rozbor_button_rozebrat = QPushButton(self.widget_29)
        self.rozbor_button_rozebrat.setObjectName(u"rozbor_button_rozebrat")

        self.verticalLayout_17.addWidget(self.rozbor_button_rozebrat)


        self.verticalLayout_11.addWidget(self.widget_29)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 5)

        self.verticalLayout_10.addWidget(self.widget_21)


        self.verticalLayout_2.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_18)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setStyleSheet(u"#widget_20{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}\n"
"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:800;\n"
"background-color:#3a3a39;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"}")
        self.gridLayout_13 = QGridLayout(self.widget_20)
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.label_13 = QLabel(self.widget_20)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_13.addWidget(self.label_13, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.rozbor_button_historie_zobrazit = QPushButton(self.widget_22)
        self.rozbor_button_historie_zobrazit.setObjectName(u"rozbor_button_historie_zobrazit")

        self.horizontalLayout_12.addWidget(self.rozbor_button_historie_zobrazit)

        self.rozbor_button_historie_delete = QPushButton(self.widget_22)
        self.rozbor_button_historie_delete.setObjectName(u"rozbor_button_historie_delete")
        self.rozbor_button_historie_delete.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.rozbor_button_historie_delete)


        self.gridLayout_13.addWidget(self.widget_22, 1, 0, 1, 1)

        self.widget_23 = QWidget(self.widget_20)
        self.widget_23.setObjectName(u"widget_23")
        self.gridLayout_14 = QGridLayout(self.widget_23)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.rozbor_historie_scrollArea = QScrollArea(self.widget_23)
        self.rozbor_historie_scrollArea.setObjectName(u"rozbor_historie_scrollArea")
        self.rozbor_historie_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 256, 205))
        self.rozbor_historie_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_14.addWidget(self.rozbor_historie_scrollArea, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_23, 2, 0, 1, 1)

        self.gridLayout_13.setRowStretch(0, 1)
        self.gridLayout_13.setRowStretch(1, 2)
        self.gridLayout_13.setRowStretch(2, 10)

        self.verticalLayout_2.addWidget(self.widget_20)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)

        self.gridLayout_12.addWidget(self.widget_18, 0, 0, 1, 1)

        self.gridLayout_12.setColumnStretch(0, 3)
        self.gridLayout_12.setColumnStretch(1, 4)

        self.verticalLayout_19.addWidget(self.widget_15)

        self.stackedWidget.addWidget(self.rozbor)
        self.penezenka = QWidget()
        self.penezenka.setObjectName(u"penezenka")
        self.verticalLayout_26 = QVBoxLayout(self.penezenka)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.background = QWidget(self.penezenka)
        self.background.setObjectName(u"background")
        self.gridLayout_15 = QGridLayout(self.background)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(40)
        self.gridLayout_15.setVerticalSpacing(20)
        self.gridLayout_15.setContentsMargins(30, 15, 30, 15)
        self.widget_26 = QWidget(self.background)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"#widget_26 >QWidget{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget_26)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.widget_38 = QWidget(self.widget_26)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.penezenka_button_menu = QPushButton(self.widget_38)
        self.penezenka_button_menu.setObjectName(u"penezenka_button_menu")
        self.penezenka_button_menu.setMinimumSize(QSize(35, 35))
        self.penezenka_button_menu.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"font-weight:800;\n"
"border: 5px solid  #3a3a39;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:1600;\n"
"background-color:#3a3a39;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"\n"
"\n"
"}")

        self.horizontalLayout_19.addWidget(self.penezenka_button_menu)

        self.label_11 = QLabel(self.widget_38)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel{\n"
"color:black	;\n"
"	font: 500 18pt \"Verdana\";\n"
"}")

        self.horizontalLayout_19.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 10)

        self.verticalLayout_6.addWidget(self.widget_38)

        self.widget_37 = QWidget(self.widget_26)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_23 = QVBoxLayout(self.widget_37)
        self.verticalLayout_23.setSpacing(20)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.widget_39 = QWidget(self.widget_37)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_18 = QVBoxLayout(self.widget_39)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_13)

        self.label_16 = QLabel(self.widget_39)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_18.addWidget(self.label_16)

        self.lineEdit_2 = QLineEdit(self.widget_39)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_18.addWidget(self.lineEdit_2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_12)

        self.verticalLayout_18.setStretch(1, 1)
        self.verticalLayout_18.setStretch(2, 2)

        self.verticalLayout_23.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget_37)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_20 = QVBoxLayout(self.widget_40)
        self.verticalLayout_20.setSpacing(10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_15)

        self.label_15 = QLabel(self.widget_40)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_20.addWidget(self.label_15)

        self.lineEdit_4 = QLineEdit(self.widget_40)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_20.addWidget(self.lineEdit_4)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_14)

        self.verticalLayout_20.setStretch(1, 1)
        self.verticalLayout_20.setStretch(2, 2)

        self.verticalLayout_23.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.widget_37)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_21 = QVBoxLayout(self.widget_41)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_17)

        self.label_18 = QLabel(self.widget_41)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_21.addWidget(self.label_18)

        self.lineEdit_5 = QLineEdit(self.widget_41)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_21.addWidget(self.lineEdit_5)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_16)

        self.verticalLayout_21.setStretch(1, 1)
        self.verticalLayout_21.setStretch(2, 2)

        self.verticalLayout_23.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget_37)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_22 = QVBoxLayout(self.widget_42)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_19)

        self.label_19 = QLabel(self.widget_42)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_22.addWidget(self.label_19)

        self.lineEdit_6 = QLineEdit(self.widget_42)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_22.addWidget(self.lineEdit_6)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_18)

        self.verticalLayout_22.setStretch(1, 1)
        self.verticalLayout_22.setStretch(2, 2)

        self.verticalLayout_23.addWidget(self.widget_42)

        self.widget_43 = QWidget(self.widget_37)
        self.widget_43.setObjectName(u"widget_43")
        self.verticalLayout_28 = QVBoxLayout(self.widget_43)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_20)

        self.pushButton = QPushButton(self.widget_43)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_28.addWidget(self.pushButton)


        self.verticalLayout_23.addWidget(self.widget_43)


        self.verticalLayout_6.addWidget(self.widget_37)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 20)

        self.gridLayout_15.addWidget(self.widget_26, 0, 0, 1, 1)

        self.widget_36 = QWidget(self.background)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setStyleSheet(u"QWidget{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout_24 = QVBoxLayout(self.widget_36)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(self.widget_36)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_area_vypis_hesel = QWidget()
        self.scroll_area_vypis_hesel.setObjectName(u"scroll_area_vypis_hesel")
        self.scroll_area_vypis_hesel.setGeometry(QRect(0, 0, 435, 718))
        self.verticalLayout_27 = QVBoxLayout(self.scroll_area_vypis_hesel)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.penezenka_widget = QWidget(self.scroll_area_vypis_hesel)
        self.penezenka_widget.setObjectName(u"penezenka_widget")
        self.penezenka_widget.setMinimumSize(QSize(0, 700))

        self.verticalLayout_27.addWidget(self.penezenka_widget)

        self.scrollArea.setWidget(self.scroll_area_vypis_hesel)

        self.verticalLayout_24.addWidget(self.scrollArea)


        self.gridLayout_15.addWidget(self.widget_36, 0, 1, 1, 1)

        self.gridLayout_15.setColumnStretch(0, 2)
        self.gridLayout_15.setColumnStretch(1, 4)

        self.verticalLayout_26.addWidget(self.background)

        self.stackedWidget.addWidget(self.penezenka)
        self.generator = QWidget()
        self.generator.setObjectName(u"generator")
        self.gridLayout_11 = QGridLayout(self.generator)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_44 = QWidget(self.generator)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setStyleSheet(u"#widget_44{\n"
"background-color: #3a3a39;\n"
"}")
        self.gridLayout_17 = QGridLayout(self.widget_44)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setHorizontalSpacing(40)
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setContentsMargins(30, 15, 30, 15)
        self.widget_45 = QWidget(self.widget_44)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(300, 500))
        self.widget_45.setStyleSheet(u"#widget_45> QWidget {\n"
"    background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"\n"
"}\n"
"QLabel{\n"
"font-size:11pt;\n"
"padding:1px;\n"
"\n"
"}\n"
"/* CHECCK BOX CSS*/\n"
"QCheckBox {\n"
"    padding: 5px;\n"
" font-size: 11pt;\n"
"\n"
"}\n"
"QCheckBox::indicator {\n"
"    background-color: #F0F7F4;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border: 2px solid #3a3a39;\n"
"    border-radius: 4px;\n"
"    transition: width 400ms ease-in-out, height 400ms ease-in-out, border 400ms ease-in-out;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    width: 19px;         \n"
"    height: 19px;\n"
"   border: none;    \n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/check_3.png);\n"
"    border: 2px solid #3a3a39;\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: none;\n"
"}\n"
"/*RADIO BUTTON CSS */\n"
"QRadioButton{\n"
"spacing:5px;\n"
"color:black;\n"
"font-size: 11pt;\n"
"}\n"
"QRadioButton::indicator{\n"
"width: 15px;\n"
"height:15px;\n"
"border: 2px solid #3a3a39;\n"
""
                        "border-radius: 9px;\n"
"background-color: #F0F7F4;\n"
"transition: background-color 400ms ease-in-out, border 400ms ease-in-out;\n"
"}\n"
"QRadioButton:indicator:hover{\n"
"border-color:none\n"
"}\n"
"\n"
"QRadioButton:indicator:checked{\n"
"	image: url(:/icons/radio_2.png);\n"
"}\n"
"\n"
"/* LINE EDIT	*/\n"
"QLineEdit{\n"
"background-color:#F0F7F4;\n"
"border: 1px solid #3a3a39;\n"
"border-radius: 3px;\n"
"padding:2px 4px;;\n"
"selection-background-color: #3a3a39;\n"
"transition: 400ms ease-in-out;\n"
"}\n"
"/* hover a nakliknut\u00ed */\n"
"QLineEdit:focus, QLineEdit:hover{\n"
"border:none;\n"
"}\n"
"\n"
"/* SLIDER */\n"
"QSlider::groove:horizontal {\n"
"    height: 4px;\n"
"    background: #3a3a39;\n"
"    border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"/* 2. Nevypln\u011bn\u00e1 \u010d\u00e1st (vpravo od \u00fachytu) */\n"
"QSlider::add-page:horizontal {\n"
"    background: #F0F7F4 ;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/* 3. Vypln\u011bn\u00e1 \u010d\u00e1st (vlevo od \u00fachytu - ukazuje hodnotu) */\n"
"Q"
                        "Slider::sub-page:horizontal {\n"
"    background: #3a3a39;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"/* 4. \u00dachyt / Kole\u010dko, za kter\u00e9 se tah\u00e1 */\n"
"QSlider::handle:horizontal {\n"
"    background: #F0F7F4;\n"
"    border: 3px solid #3a3a39 ;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"         margin: -4px 0;           /* Vyrovn\u00e1n\u00ed: posune \u00fachyt na st\u0159ed li\u0161ty */\n"
"    border-radius:6px;              /* Ud\u011bl\u00e1 z \u00fachytu kruh */\n"
"}\n"
"\n"
"/* 5. Hover efekt pro \u00fachyt */\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #3a3a39;\n"
"    border: 3px solid #F0F7F4;\n"
"border-radius:6px;\n"
"}\n"
"")
        self.verticalLayout_25 = QVBoxLayout(self.widget_45)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.widget_47 = QWidget(self.widget_45)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.generator_button_menu = QPushButton(self.widget_47)
        self.generator_button_menu.setObjectName(u"generator_button_menu")
        self.generator_button_menu.setMinimumSize(QSize(35, 35))
        font = QFont()
        font.setWeight(QFont.ExtraBold)
        font.setItalic(False)
        self.generator_button_menu.setFont(font)
        self.generator_button_menu.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"font-weight:800;\n"
"border: 5px solid  #3a3a39;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:1600;\n"
"background-color:#3a3a39;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"\n"
"\n"
"}")

        self.horizontalLayout_20.addWidget(self.generator_button_menu, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_2 = QLabel(self.widget_47)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"color:black	;\n"
"	\n"
"	font: 500 18pt \"Verdana\";\n"
"}")

        self.horizontalLayout_20.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 10)

        self.verticalLayout_25.addWidget(self.widget_47)

        self.widget_48 = QWidget(self.widget_45)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setStyleSheet(u"")
        self.verticalLayout_32 = QVBoxLayout(self.widget_48)
        self.verticalLayout_32.setSpacing(20)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.gridLayout_18 = QGridLayout(self.widget_49)
        self.gridLayout_18.setSpacing(5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(5, 5, 5, 10)
        self.generator_radioButton_fraze = QRadioButton(self.widget_49)
        self.generator_radioButton_fraze.setObjectName(u"generator_radioButton_fraze")

        self.gridLayout_18.addWidget(self.generator_radioButton_fraze, 4, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_21, 5, 0, 1, 1)

        self.generator_radioButton_heslo = QRadioButton(self.widget_49)
        self.generator_radioButton_heslo.setObjectName(u"generator_radioButton_heslo")

        self.gridLayout_18.addWidget(self.generator_radioButton_heslo, 3, 0, 1, 1)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_23, 2, 0, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_22, 0, 0, 1, 1)

        self.label_20 = QLabel(self.widget_49)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"QLabel{\n"
"font-size:14pt;\n"
"}")

        self.gridLayout_18.addWidget(self.label_20, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_32.addWidget(self.widget_49)

        self.generator_widget_heslo = QWidget(self.widget_48)
        self.generator_widget_heslo.setObjectName(u"generator_widget_heslo")
        self.verticalLayout_30 = QVBoxLayout(self.generator_widget_heslo)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(5, 5, 5, 5)
        self.widget_51 = QWidget(self.generator_widget_heslo)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMinimumSize(QSize(0, 0))
        self.verticalLayout_34 = QVBoxLayout(self.widget_51)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(2, 2, 2, 2)
        self.generator_label_pocet_znaku = QLabel(self.widget_51)
        self.generator_label_pocet_znaku.setObjectName(u"generator_label_pocet_znaku")

        self.verticalLayout_34.addWidget(self.generator_label_pocet_znaku)

        self.generator_pocet_znaminek = QSlider(self.widget_51)
        self.generator_pocet_znaminek.setObjectName(u"generator_pocet_znaminek")
        self.generator_pocet_znaminek.setMinimum(1)
        self.generator_pocet_znaminek.setMaximum(50)
        self.generator_pocet_znaminek.setSliderPosition(1)
        self.generator_pocet_znaminek.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_34.addWidget(self.generator_pocet_znaminek)


        self.verticalLayout_30.addWidget(self.widget_51)

        self.generator_check_mala = QCheckBox(self.generator_widget_heslo)
        self.generator_check_mala.setObjectName(u"generator_check_mala")

        self.verticalLayout_30.addWidget(self.generator_check_mala)

        self.generator_check_velka = QCheckBox(self.generator_widget_heslo)
        self.generator_check_velka.setObjectName(u"generator_check_velka")

        self.verticalLayout_30.addWidget(self.generator_check_velka)

        self.generator_check_cisla = QCheckBox(self.generator_widget_heslo)
        self.generator_check_cisla.setObjectName(u"generator_check_cisla")

        self.verticalLayout_30.addWidget(self.generator_check_cisla)

        self.generator_check_spec = QCheckBox(self.generator_widget_heslo)
        self.generator_check_spec.setObjectName(u"generator_check_spec")

        self.verticalLayout_30.addWidget(self.generator_check_spec)

        self.generator_check_slovnikova = QCheckBox(self.generator_widget_heslo)
        self.generator_check_slovnikova.setObjectName(u"generator_check_slovnikova")

        self.verticalLayout_30.addWidget(self.generator_check_slovnikova)

        self.widget_50 = QWidget(self.generator_widget_heslo)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(0, 0))
        self.verticalLayout_33 = QVBoxLayout(self.widget_50)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.generator_lineEdit_vlastni = QLineEdit(self.widget_50)
        self.generator_lineEdit_vlastni.setObjectName(u"generator_lineEdit_vlastni")

        self.verticalLayout_33.addWidget(self.generator_lineEdit_vlastni)


        self.verticalLayout_30.addWidget(self.widget_50)


        self.verticalLayout_32.addWidget(self.generator_widget_heslo)

        self.generator_widget_fraze = QWidget(self.widget_48)
        self.generator_widget_fraze.setObjectName(u"generator_widget_fraze")
        self.generator_widget_fraze.setEnabled(True)
        self.verticalLayout_29 = QVBoxLayout(self.generator_widget_fraze)
        self.verticalLayout_29.setSpacing(30)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.widget_52 = QWidget(self.generator_widget_fraze)
        self.widget_52.setObjectName(u"widget_52")
        self.verticalLayout_35 = QVBoxLayout(self.widget_52)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_52)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_35.addWidget(self.label_22)

        self.generator_pocet_slov = QSlider(self.widget_52)
        self.generator_pocet_slov.setObjectName(u"generator_pocet_slov")
        self.generator_pocet_slov.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.generator_pocet_slov.setMinimum(1)
        self.generator_pocet_slov.setMaximum(25)
        self.generator_pocet_slov.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_35.addWidget(self.generator_pocet_slov)


        self.verticalLayout_29.addWidget(self.widget_52)

        self.generator_check_upravaFraze = QCheckBox(self.generator_widget_fraze)
        self.generator_check_upravaFraze.setObjectName(u"generator_check_upravaFraze")
        self.generator_check_upravaFraze.setStyleSheet(u"QCheckBox{\n"
"font-size:11pt;\n"
"}")

        self.verticalLayout_29.addWidget(self.generator_check_upravaFraze)


        self.verticalLayout_32.addWidget(self.generator_widget_fraze)

        self.generator_button_generovat = QPushButton(self.widget_48)
        self.generator_button_generovat.setObjectName(u"generator_button_generovat")
        self.generator_button_generovat.setMinimumSize(QSize(100, 0))
        self.generator_button_generovat.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:800;\n"
"background-color:#3a3a39;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"}")

        self.verticalLayout_32.addWidget(self.generator_button_generovat)

        self.horizontalSpacer = QSpacerItem(40, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_32.addItem(self.horizontalSpacer)


        self.verticalLayout_25.addWidget(self.widget_48)

        self.horizontalSpacer_2 = QSpacerItem(40, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_25.addItem(self.horizontalSpacer_2)

        self.verticalSpacer_24 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_24)

        self.verticalLayout_25.setStretch(0, 1)
        self.verticalLayout_25.setStretch(1, 10)

        self.gridLayout_17.addWidget(self.widget_45, 0, 0, 1, 1)

        self.widget_46 = QWidget(self.widget_44)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setStyleSheet(u"#widget_46{\n"
"background-color: #05C1FF;\n"
"border-radius:16px;\n"
"\n"
"}\n"
"")
        self.verticalLayout_36 = QVBoxLayout(self.widget_46)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(10, 10, 10, 10)
        self.generator_label_vysledek = QLabel(self.widget_46)
        self.generator_label_vysledek.setObjectName(u"generator_label_vysledek")

        self.verticalLayout_36.addWidget(self.generator_label_vysledek)

        self.generator_button_kopirovat = QPushButton(self.widget_46)
        self.generator_button_kopirovat.setObjectName(u"generator_button_kopirovat")
        self.generator_button_kopirovat.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:800;\n"
"background-color:#3a3a39;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"}")

        self.verticalLayout_36.addWidget(self.generator_button_kopirovat)


        self.gridLayout_17.addWidget(self.widget_46, 0, 1, 1, 1)

        self.gridLayout_17.setColumnStretch(0, 2)
        self.gridLayout_17.setColumnStretch(1, 3)
        self.gridLayout_17.setColumnMinimumWidth(0, 1)
        self.gridLayout_17.setColumnMinimumWidth(1, 2)

        self.gridLayout_11.addWidget(self.widget_44, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.generator)
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.gridLayout_19 = QGridLayout(self.info)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_53 = QWidget(self.info)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setStyleSheet(u"#widget_53 > #widget_55{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.gridLayout_20 = QGridLayout(self.widget_53)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(40)
        self.gridLayout_20.setVerticalSpacing(8)
        self.gridLayout_20.setContentsMargins(30, 15, 30, 15)
        self.widget_54 = QWidget(self.widget_53)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setStyleSheet(u"#widget_54 > QWidget{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout_31 = QVBoxLayout(self.widget_54)
        self.verticalLayout_31.setSpacing(20)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 10, 10, 10)
        self.widget_56 = QWidget(self.widget_54)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.info_button_menu = QPushButton(self.widget_56)
        self.info_button_menu.setObjectName(u"info_button_menu")
        self.info_button_menu.setMinimumSize(QSize(35, 35))
        self.info_button_menu.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"font-weight:800;\n"
"border: 5px solid  #3a3a39;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:1600;\n"
"background-color:#3a3a39;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"\n"
"\n"
"}")

        self.horizontalLayout_21.addWidget(self.info_button_menu)

        self.label_6 = QLabel(self.widget_56)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"color:black	;\n"
"	\n"
"	font: 500 18pt \"Verdana\";\n"
"}")

        self.horizontalLayout_21.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 10)

        self.verticalLayout_31.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.widget_54)
        self.widget_57.setObjectName(u"widget_57")
        self.verticalLayout_37 = QVBoxLayout(self.widget_57)
        self.verticalLayout_37.setSpacing(20)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(10, 10, 10, 10)
        self.pushButton_3 = QPushButton(self.widget_57)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_37.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget_57)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_37.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget_57)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_37.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_57)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_37.addWidget(self.pushButton_6)


        self.verticalLayout_31.addWidget(self.widget_57)

        self.verticalLayout_31.setStretch(0, 1)
        self.verticalLayout_31.setStretch(1, 10)

        self.gridLayout_20.addWidget(self.widget_54, 0, 0, 1, 1)

        self.widget_55 = QWidget(self.widget_53)
        self.widget_55.setObjectName(u"widget_55")
        self.gridLayout_21 = QGridLayout(self.widget_55)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(10)
        self.gridLayout_21.setContentsMargins(10, 10, 10, 10)
        self.scrollArea_3 = QScrollArea(self.widget_55)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 473, 525))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_21.addWidget(self.scrollArea_3, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.widget_55, 0, 1, 1, 1)

        self.gridLayout_20.setColumnStretch(0, 1)
        self.gridLayout_20.setColumnStretch(1, 3)

        self.gridLayout_19.addWidget(self.widget_53, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.info)
        self.Nastaveni = QWidget()
        self.Nastaveni.setObjectName(u"Nastaveni")
        self.Nastaveni.setStyleSheet(u"#Nastaveni > QWidget{\n"
"\n"
"    background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Nastaveni)
        self.gridLayout_2.setSpacing(40)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(30, 15, 30, 15)
        self.widget_63 = QWidget(self.Nastaveni)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout = QHBoxLayout(self.widget_63)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.nastaveni_button_menu = QPushButton(self.widget_63)
        self.nastaveni_button_menu.setObjectName(u"nastaveni_button_menu")
        self.nastaveni_button_menu.setMinimumSize(QSize(35, 35))
        self.nastaveni_button_menu.setStyleSheet(u"QPushButton{\n"
"background-color:#494948;\n"
"color:white;\n"
"font-size: 16px;\n"
"font-weight:800;\n"
"border: 5px solid  #3a3a39;\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"font-weight:1600;\n"
"background-color:#3a3a39;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"font-weight:400;\n"
"background-color:#2c2c2b;\n"
"\n"
"\n"
"}")

        self.horizontalLayout.addWidget(self.nastaveni_button_menu)

        self.label_7 = QLabel(self.widget_63)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"color:black	;\n"
"	\n"
"	font: 500 18pt \"Verdana\";\n"
"}")

        self.horizontalLayout.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)

        self.gridLayout_2.addWidget(self.widget_63, 0, 0, 1, 1)

        self.widget_64 = QWidget(self.Nastaveni)
        self.widget_64.setObjectName(u"widget_64")
        self.gridLayout_23 = QGridLayout(self.widget_64)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_23 = QLabel(self.widget_64)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_23.addWidget(self.label_23, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_64, 1, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 6)
        self.stackedWidget.addWidget(self.Nastaveni)
        self.zalozeni = QWidget()
        self.zalozeni.setObjectName(u"zalozeni")
        self.gridLayout_24 = QGridLayout(self.zalozeni)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_65 = QWidget(self.zalozeni)
        self.widget_65.setObjectName(u"widget_65")
        self.gridLayout_25 = QGridLayout(self.widget_65)
        self.gridLayout_25.setSpacing(20)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(50, 40, 50, 40)
        self.widget_66 = QWidget(self.widget_65)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setStyleSheet(u"#widget_66{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.widget_66)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.widget_68 = QWidget(self.widget_66)
        self.widget_68.setObjectName(u"widget_68")
        self.verticalLayout_40 = QVBoxLayout(self.widget_68)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_24 = QLabel(self.widget_68)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_40.addWidget(self.label_24)

        self.zalozeni_lineEdit_jmeno = QLineEdit(self.widget_68)
        self.zalozeni_lineEdit_jmeno.setObjectName(u"zalozeni_lineEdit_jmeno")

        self.verticalLayout_40.addWidget(self.zalozeni_lineEdit_jmeno)


        self.verticalLayout_39.addWidget(self.widget_68)

        self.widget_70 = QWidget(self.widget_66)
        self.widget_70.setObjectName(u"widget_70")
        self.verticalLayout_41 = QVBoxLayout(self.widget_70)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_26 = QLabel(self.widget_70)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_41.addWidget(self.label_26)

        self.zalozeni_lineEdit_heslo = QLineEdit(self.widget_70)
        self.zalozeni_lineEdit_heslo.setObjectName(u"zalozeni_lineEdit_heslo")

        self.verticalLayout_41.addWidget(self.zalozeni_lineEdit_heslo)


        self.verticalLayout_39.addWidget(self.widget_70)

        self.widget_69 = QWidget(self.widget_66)
        self.widget_69.setObjectName(u"widget_69")
        self.verticalLayout_42 = QVBoxLayout(self.widget_69)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_25 = QLabel(self.widget_69)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_42.addWidget(self.label_25)

        self.zalozeni_lineEdit_heslo_znovu = QLineEdit(self.widget_69)
        self.zalozeni_lineEdit_heslo_znovu.setObjectName(u"zalozeni_lineEdit_heslo_znovu")

        self.verticalLayout_42.addWidget(self.zalozeni_lineEdit_heslo_znovu)


        self.verticalLayout_39.addWidget(self.widget_69)

        self.widget_71 = QWidget(self.widget_66)
        self.widget_71.setObjectName(u"widget_71")
        self.verticalLayout_43 = QVBoxLayout(self.widget_71)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_29 = QLabel(self.widget_71)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 80))
        self.label_29.setStyleSheet(u"QLabel{\n"
"font-size:9pt;\n"
"}")
        self.label_29.setWordWrap(True)

        self.verticalLayout_43.addWidget(self.label_29)

        self.zalozeni_label_poznamka = QLabel(self.widget_71)
        self.zalozeni_label_poznamka.setObjectName(u"zalozeni_label_poznamka")

        self.verticalLayout_43.addWidget(self.zalozeni_label_poznamka)


        self.verticalLayout_39.addWidget(self.widget_71)

        self.zalozeni_button_zalozit = QPushButton(self.widget_66)
        self.zalozeni_button_zalozit.setObjectName(u"zalozeni_button_zalozit")

        self.verticalLayout_39.addWidget(self.zalozeni_button_zalozit)


        self.gridLayout_25.addWidget(self.widget_66, 0, 0, 1, 1)

        self.widget_67 = QWidget(self.widget_65)
        self.widget_67.setObjectName(u"widget_67")
        self.widget_67.setStyleSheet(u"#widget_67{\n"
" background-color: #05C1FF;\n"
"    border-radius: 16px;\n"
"}")
        self.verticalLayout_38 = QVBoxLayout(self.widget_67)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_27 = QLabel(self.widget_67)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_38.addWidget(self.label_27, 0, Qt.AlignmentFlag.AlignHCenter)

        self.zalozeni_button_do_prihlaseni = QPushButton(self.widget_67)
        self.zalozeni_button_do_prihlaseni.setObjectName(u"zalozeni_button_do_prihlaseni")

        self.verticalLayout_38.addWidget(self.zalozeni_button_do_prihlaseni)


        self.gridLayout_25.addWidget(self.widget_67, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_65, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.zalozeni)

        self.gridLayout_10.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hesl\u00e1tor", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"P\u0159ihla\u0161ovac\u00ed jm\u00e9no/e-mail", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Heslo", None))
        self.login_label_poznamka.setText("")
        self.login_button_prihlasit.setText(QCoreApplication.translate("MainWindow", u"P\u0159ihl\u00e1sit se", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Nem\u00e1te \u00fa\u010det? Zalo\u017ete si nov\u00fd!", None))
        self.login_button_do_zalozeni.setText(QCoreApplication.translate("MainWindow", u"Zalo\u017eit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"HESL\u00c1TOR", None))
        self.menu_button_quickGen.setText(QCoreApplication.translate("MainWindow", u"Generuj", None))
        self.menu_button_quickCopy.setText(QCoreApplication.translate("MainWindow", u"Kop\u00edrovat", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rychlo-gener\u00e1tor", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menu_button_quickSave.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017e", None))
        self.menu_button_quickReset.setText(QCoreApplication.translate("MainWindow", u"Resetovat", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Rychlo uklada\u010d", None))
        self.menu_button_generator.setText(QCoreApplication.translate("MainWindow", u"Gener\u00e1tor", None))
        self.menu_button_penezenka.setText(QCoreApplication.translate("MainWindow", u"Pen\u011b\u017eenka", None))
        self.menu_button_rozbor.setText(QCoreApplication.translate("MainWindow", u"Rozbor", None))
        self.menu_button_nastaveni.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed", None))
        self.menu_button_info.setText(QCoreApplication.translate("MainWindow", u"Jak na hesla?", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Rozbor hesela:", None))
        self.rozbor_label_heslo.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Celkov\u00e1 s\u00edla hesla", None))
        self.rozbor_label_score.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        self.rozbor_label_popisSily.setText(QCoreApplication.translate("MainWindow", u"Popis s\u00edly", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Odhadovan\u00fd \u010das pot\u0159ebn\u00fd k prolomen\u00ed hesla", None))
        self.rozbor_label_cas.setText(QCoreApplication.translate("MainWindow", u"\u010cas", None))
        self.rozbor_label_popisCasu.setText(QCoreApplication.translate("MainWindow", u"popis", None))
        self.rozbor_label_delka.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka", None))
        self.rozbor_label_mala.setText(QCoreApplication.translate("MainWindow", u"Mal\u00e1 p\u00edsmena", None))
        self.rozbor_label_velka.setText(QCoreApplication.translate("MainWindow", u"Velk\u00e1 p\u00edsmena", None))
        self.rozbor_label_cisla.setText(QCoreApplication.translate("MainWindow", u"\u010c\u00edsla", None))
        self.rozbor_label_spec.setText(QCoreApplication.translate("MainWindow", u"Speci\u00e1ln\u00ed znaky", None))
        self.rozbor_label_slovnikova.setText(QCoreApplication.translate("MainWindow", u"Slovn\u00edkov\u00e1 slova", None))
        self.rozbor_button_menu.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Rozbor hesel", None))
        self.rozbor_button_rozebrat.setText(QCoreApplication.translate("MainWindow", u"Rozebrat", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Historie kontrolov\u00e1n\u00ed hesel", None))
        self.rozbor_button_historie_zobrazit.setText(QCoreApplication.translate("MainWindow", u"Zobrazit", None))
        self.rozbor_button_historie_delete.setText(QCoreApplication.translate("MainWindow", u"Smazat", None))
        self.penezenka_button_menu.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Pene\u017eenka", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"P\u0159ihla\u0161ovac\u00ed jm\u00e9no/ e-mail:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Heslo:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Platforma:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Pozn\u00e1mka:", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nepovinn\u00e9", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit", None))
        self.generator_button_menu.setText(QCoreApplication.translate("MainWindow", u"\u02c2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gener\u00e1tor", None))
        self.generator_radioButton_fraze.setText(QCoreApplication.translate("MainWindow", u"Generovat heslovou fr\u00e1zi", None))
        self.generator_radioButton_heslo.setText(QCoreApplication.translate("MainWindow", u"Generovat heslo", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed gener\u00e1toru", None))
        self.generator_label_pocet_znaku.setText(QCoreApplication.translate("MainWindow", u"Po\u010det znak\u016f", None))
        self.generator_check_mala.setText(QCoreApplication.translate("MainWindow", u"Mal\u00e1 p\u00edsmenka", None))
        self.generator_check_velka.setText(QCoreApplication.translate("MainWindow", u"Velk\u00e1 p\u00edsmenka", None))
        self.generator_check_cisla.setText(QCoreApplication.translate("MainWindow", u"\u010c\u00edsla", None))
        self.generator_check_spec.setText(QCoreApplication.translate("MainWindow", u"Speci\u00e1ln\u00ed znaky", None))
        self.generator_check_slovnikova.setText(QCoreApplication.translate("MainWindow", u"Slovn\u00edkov\u00e1 slova", None))
        self.generator_lineEdit_vlastni.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vlastn\u00ed slovo", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Po\u010det slov", None))
        self.generator_check_upravaFraze.setText(QCoreApplication.translate("MainWindow", u"Speci\u00e1ln\u00ed \u00faprava pro siln\u011bj\u0161\u00ed fr\u00e1zi", None))
        self.generator_button_generovat.setText(QCoreApplication.translate("MainWindow", u"Generovat", None))
        self.generator_label_vysledek.setText(QCoreApplication.translate("MainWindow", u"vygenerovan\u00e9 heslo:", None))
        self.generator_button_kopirovat.setText(QCoreApplication.translate("MainWindow", u"kop\u00edrovat", None))
        self.info_button_menu.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Vzd\u011bl\u00e1n\u00ed", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Funkce hesl\u00e1toru", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"O hesl\u00e1toru", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"jak na siln\u00e9 heslo", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"heslov\u00e1 fr\u00e1ze", None))
        self.nastaveni_button_menu.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nastaven\u00ed", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Zat\u00edm nen\u00ed co nastavovat", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"P\u0159ihla\u0161ovac\u00ed jm\u00e9no/e-mail", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Heslo", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"znovu heslo", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Zalo\u017ete si nov\u00fd \u00fa\u010det v aplikaci hesl\u00e1tor. Vlo\u017ete p\u0159ihla\u0161ovac\u00ed jm\u00e9no a heslo. Pou\u017eit\u00e9 heslo si zapamatujte, jinak byste mohli p\u0159ij\u00edt o d\u016fle\u017eit\u00e1 data. Pokud chcete pou\u017e\u00edvat hesl\u00e1tor bez ukl\u00e1d\u00e1n\u00ed dat, m\u016f\u017eete pou\u017e\u00edt p\u0159ihla\u0161ovac\u00ed"
                        " \u00fadaje: jm\u00e9no: guest, heslo:guest.</span></p></body></html>", None))
        self.zalozeni_label_poznamka.setText(QCoreApplication.translate("MainWindow", u"Pozn\u00e1mka:", None))
        self.zalozeni_button_zalozit.setText(QCoreApplication.translate("MainWindow", u"Zalo\u017eit", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"M\u00e1te ji\u017e \u00fa\u010det na tomto za\u0159\u00edzen\u00ed? tak se p\u0159ihla\u0161te!", None))
        self.zalozeni_button_do_prihlaseni.setText(QCoreApplication.translate("MainWindow", u"P\u0159ihl\u00e1sit se", None))
    # retranslateUi

