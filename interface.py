# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_header = QtWidgets.QFrame(self.frame)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_header.setAutoFillBackground(False)
        self.frame_header.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: rgb(73, 103, 199);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(199, 199, 199);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(150, 150, 150);\n"
"    border-radius: 5px;\n"
"    opacity: 0;\n"
"}")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_header)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_menu = QtWidgets.QPushButton(self.frame_header)
        self.bt_menu.setMinimumSize(QtCore.QSize(200, 40))
        self.bt_menu.setStyleSheet("")
        self.bt_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu.setDefault(False)
        self.bt_menu.setFlat(False)
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout.addWidget(self.bt_menu)
        spacerItem = QtWidgets.QSpacerItem(351, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_minimize = QtWidgets.QPushButton(self.frame_header)
        self.bt_minimize.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_minimize.setStyleSheet("")
        self.bt_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/minimize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimize.setIcon(icon1)
        self.bt_minimize.setIconSize(QtCore.QSize(38, 38))
        self.bt_minimize.setDefault(False)
        self.bt_minimize.setFlat(False)
        self.bt_minimize.setObjectName("bt_minimize")
        self.horizontalLayout.addWidget(self.bt_minimize)
        self.bt_minimun = QtWidgets.QPushButton(self.frame_header)
        self.bt_minimun.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_minimun.setStyleSheet("")
        self.bt_minimun.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/minimize_size.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimun.setIcon(icon2)
        self.bt_minimun.setIconSize(QtCore.QSize(38, 38))
        self.bt_minimun.setDefault(False)
        self.bt_minimun.setFlat(False)
        self.bt_minimun.setObjectName("bt_minimun")
        self.horizontalLayout.addWidget(self.bt_minimun)
        self.bt_maximun = QtWidgets.QPushButton(self.frame_header)
        self.bt_maximun.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_maximun.setStyleSheet("")
        self.bt_maximun.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/maximize_size.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_maximun.setIcon(icon3)
        self.bt_maximun.setIconSize(QtCore.QSize(38, 38))
        self.bt_maximun.setDefault(False)
        self.bt_maximun.setFlat(False)
        self.bt_maximun.setObjectName("bt_maximun")
        self.horizontalLayout.addWidget(self.bt_maximun)
        self.bt_close = QtWidgets.QPushButton(self.frame_header)
        self.bt_close.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_close.setStyleSheet("")
        self.bt_close.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_close.setIcon(icon4)
        self.bt_close.setIconSize(QtCore.QSize(38, 38))
        self.bt_close.setDefault(False)
        self.bt_close.setFlat(False)
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout.addWidget(self.bt_close)
        self.verticalLayout_2.addWidget(self.frame_header)
        self.frame_main = QtWidgets.QFrame(self.frame)
        self.frame_main.setStyleSheet("#frame_menu {    \n"
"    background-color: rgb(73, 103, 199);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(199, 199, 199);\n"
"    border-radius: 5px;\n"
"    color: rgb(28, 39, 76);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-radius: 5px;\n"
"    color:rgb(28, 39, 76);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_main)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_menu = QtWidgets.QFrame(self.frame_main)
        self.frame_menu.setMinimumSize(QtCore.QSize(210, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_database = QtWidgets.QPushButton(self.frame_menu)
        self.bt_database.setMinimumSize(QtCore.QSize(0, 35))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_database.setIcon(icon5)
        self.bt_database.setObjectName("bt_database")
        self.verticalLayout_3.addWidget(self.bt_database)
        self.bt_register = QtWidgets.QPushButton(self.frame_menu)
        self.bt_register.setMinimumSize(QtCore.QSize(0, 35))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/register.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_register.setIcon(icon6)
        self.bt_register.setObjectName("bt_register")
        self.verticalLayout_3.addWidget(self.bt_register)
        self.bt_update = QtWidgets.QPushButton(self.frame_menu)
        self.bt_update.setMinimumSize(QtCore.QSize(0, 35))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_update.setIcon(icon7)
        self.bt_update.setObjectName("bt_update")
        self.verticalLayout_3.addWidget(self.bt_update)
        self.bt_delete = QtWidgets.QPushButton(self.frame_menu)
        self.bt_delete.setMinimumSize(QtCore.QSize(0, 35))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_delete.setIcon(icon8)
        self.bt_delete.setObjectName("bt_delete")
        self.verticalLayout_3.addWidget(self.bt_delete)
        self.horizontalLayout_2.addWidget(self.frame_menu)
        self.frame_page = QtWidgets.QFrame(self.frame_main)
        self.frame_page.setStyleSheet("""
    QFrame {
        background-color: #ffffff;
    }

    QLabel {
        color: rgb(26, 39, 76);
        font: 75 12pt "Arial";
    }

    QLineEdit {
        background-color: rgb(230, 230, 230);
        color: rgb(26, 39, 76);
        border: 0;
        border-bottom: 1px solid rgb(150, 150, 150);
        font: 75 12pt "Arial";
    }

    QPushButton {
        background-color: rgb(199, 199, 199);
        border-radius: 5px;
        color: rgb(28, 39, 76);
        font: 12pt "Arial";
    }

    QPushButton:hover {
        background-color: rgb(150, 150, 150);
        border-radius: 5px;
        color: rgb(28, 39, 76);
        font: 12pt "Arial";
    }

    QTableWidget {
        background-color: rgb(199, 199, 199);
        border: 1px solid #000;
        color: #000;
        font: 10pt "Arial";
    }


    QTableWidget QTableCornerButton::section {
        background-color: rgb(199, 199, 199);
        border: 1px solid rgb(0, 199, 199);
    }
""")
        self.frame_page.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_page.setObjectName("frame_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_page)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_page)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_database = QtWidgets.QWidget()
        self.page_database.setObjectName("page_database")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_database)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.page_database)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.table_products = QtWidgets.QTableWidget(self.page_database)
        self.table_products.setMinimumSize(QtCore.QSize(529, 0))
        self.table_products.setAutoFillBackground(False)
        self.table_products.setShowGrid(False)
        self.table_products.setObjectName("table_products")
        self.table_products.setColumnCount(5)
        self.table_products.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(4, item)
        self.table_products.horizontalHeader().setCascadingSectionResizes(False)
        self.table_products.horizontalHeader().setMinimumSectionSize(39)
        self.table_products.horizontalHeader().setStretchLastSection(True)
        self.table_products.verticalHeader().setDefaultSectionSize(30)
        self.table_products.verticalHeader().setMinimumSectionSize(23)
        self.table_products.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.table_products)
        self.stackedWidget.addWidget(self.page_database)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_register)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.page_register)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.page_register)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.page_register)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.page_register)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.page_register)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.page_register)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.ln_register_id = QtWidgets.QLineEdit(self.page_register)
        self.ln_register_id.setMinimumSize(QtCore.QSize(400, 30))
        self.ln_register_id.setObjectName("ln_register_id")
        self.ln_register_id.setReadOnly(True)
        self.verticalLayout_6.addWidget(self.ln_register_id)
        self.ln_register_name = QtWidgets.QLineEdit(self.page_register)
        self.ln_register_name.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_register_name.setObjectName("ln_register_name")
        self.verticalLayout_6.addWidget(self.ln_register_name)
        self.ln_register_category = QtWidgets.QLineEdit(self.page_register)
        self.ln_register_category.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_register_category.setObjectName("ln_register_category")
        self.verticalLayout_6.addWidget(self.ln_register_category)
        self.ln_register_price = QtWidgets.QLineEdit(self.page_register)
        self.ln_register_price.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_register_price.setObjectName("ln_register_price")
        self.verticalLayout_6.addWidget(self.ln_register_price)
        self.ln_register_quantity = QtWidgets.QLineEdit(self.page_register)
        self.ln_register_quantity.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_register_quantity.setObjectName("ln_register_quantity")
        self.verticalLayout_6.addWidget(self.ln_register_quantity)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 49, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_save_register = QtWidgets.QPushButton(self.page_register)
        self.bt_save_register.setMinimumSize(QtCore.QSize(140, 30))
        self.bt_save_register.setObjectName("bt_save_register")
        self.horizontalLayout_4.addWidget(self.bt_save_register)
        spacerItem4 = QtWidgets.QSpacerItem(298, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.notification_register = QtWidgets.QLabel(self.page_register)
        self.notification_register.setMinimumSize(QtCore.QSize(200, 0))
        self.notification_register.setText("")
        self.notification_register.setAlignment(QtCore.Qt.AlignCenter)
        self.notification_register.setObjectName("notification_register")
        self.horizontalLayout_4.addWidget(self.notification_register)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.page_register)
        self.page_update = QtWidgets.QWidget()
        self.page_update.setObjectName("page_update")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_update)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.page_update)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_12.addWidget(self.label_15)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.label_16 = QtWidgets.QLabel(self.page_update)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.ln_upadate_search = QtWidgets.QLineEdit(self.page_update)
        self.ln_upadate_search.setMinimumSize(QtCore.QSize(260, 30))
        self.ln_upadate_search.setObjectName("ln_upadate_search")
        self.horizontalLayout_8.addWidget(self.ln_upadate_search)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.page_update)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.page_update)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.page_update)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.page_update)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.page_update)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.ln_update_id = QtWidgets.QLineEdit(self.page_update)
        self.ln_update_id.setMinimumSize(QtCore.QSize(400, 30))
        self.ln_update_id.setObjectName("ln_update_id")
        self.verticalLayout_11.addWidget(self.ln_update_id)
        self.ln_update_name = QtWidgets.QLineEdit(self.page_update)
        self.ln_update_name.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_update_name.setObjectName("ln_update_name")
        self.verticalLayout_11.addWidget(self.ln_update_name)
        self.ln_update_category = QtWidgets.QLineEdit(self.page_update)
        self.ln_update_category.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_update_category.setObjectName("ln_update_category")
        self.verticalLayout_11.addWidget(self.ln_update_category)
        self.ln_update_price = QtWidgets.QLineEdit(self.page_update)
        self.ln_update_price.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_update_price.setObjectName("ln_update_price")
        self.verticalLayout_11.addWidget(self.ln_update_price)
        self.ln_update_quantity = QtWidgets.QLineEdit(self.page_update)
        self.ln_update_quantity.setMinimumSize(QtCore.QSize(0, 30))
        self.ln_update_quantity.setObjectName("ln_update_quantity")
        self.verticalLayout_11.addWidget(self.ln_update_quantity)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bt_save_update = QtWidgets.QPushButton(self.page_update)
        self.bt_save_update.setMinimumSize(QtCore.QSize(140, 30))
        self.bt_save_update.setObjectName("bt_save_update")
        self.horizontalLayout_7.addWidget(self.bt_save_update)
        spacerItem10 = QtWidgets.QSpacerItem(298, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.notification_update = QtWidgets.QLabel(self.page_update)
        self.notification_update.setMinimumSize(QtCore.QSize(200, 0))
        self.notification_update.setText("")
        self.notification_update.setAlignment(QtCore.Qt.AlignCenter)
        self.notification_update.setObjectName("notification_update")
        self.horizontalLayout_7.addWidget(self.notification_update)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_update)
        self.page_eliminate = QtWidgets.QWidget()
        self.page_eliminate.setObjectName("page_eliminate")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_eliminate)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.page_eliminate)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_13.addWidget(self.label_21)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.label_19 = QtWidgets.QLabel(self.page_eliminate)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_11.addWidget(self.label_19)
        self.ln_delete_search = QtWidgets.QLineEdit(self.page_eliminate)
        self.ln_delete_search.setMinimumSize(QtCore.QSize(260, 30))
        self.ln_delete_search.setObjectName("ln_delete_search")
        self.horizontalLayout_11.addWidget(self.ln_delete_search)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.table_products_delete = QtWidgets.QTableWidget(self.page_eliminate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_products_delete.sizePolicy().hasHeightForWidth())
        self.table_products_delete.setSizePolicy(sizePolicy)
        self.table_products_delete.setMinimumSize(QtCore.QSize(529, 0))
        self.table_products_delete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_products_delete.setAutoFillBackground(False)
        self.table_products_delete.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table_products_delete.setTextElideMode(QtCore.Qt.ElideRight)
        self.table_products_delete.setShowGrid(False)
        self.table_products_delete.setCornerButtonEnabled(True)
        self.table_products_delete.setObjectName("table_products_delete")
        self.table_products_delete.setColumnCount(5)
        self.table_products_delete.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_products_delete.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products_delete.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products_delete.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products_delete.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products_delete.setHorizontalHeaderItem(4, item)
        self.table_products_delete.horizontalHeader().setVisible(False)
        self.table_products_delete.horizontalHeader().setCascadingSectionResizes(False)
        self.table_products_delete.horizontalHeader().setDefaultSectionSize(105)
        self.table_products_delete.horizontalHeader().setMinimumSectionSize(39)
        self.table_products_delete.horizontalHeader().setSortIndicatorShown(False)
        self.table_products_delete.horizontalHeader().setStretchLastSection(True)
        self.table_products_delete.verticalHeader().setCascadingSectionResizes(False)
        self.table_products_delete.verticalHeader().setDefaultSectionSize(30)
        self.table_products_delete.verticalHeader().setHighlightSections(True)
        self.table_products_delete.verticalHeader().setMinimumSectionSize(23)
        self.table_products_delete.verticalHeader().setSortIndicatorShown(False)
        self.table_products_delete.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_13.addWidget(self.table_products_delete)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.bt_save_delete = QtWidgets.QPushButton(self.page_eliminate)
        self.bt_save_delete.setMinimumSize(QtCore.QSize(140, 30))
        self.bt_save_delete.setObjectName("bt_save_delete")
        self.horizontalLayout_12.addWidget(self.bt_save_delete)
        spacerItem13 = QtWidgets.QSpacerItem(298, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.notification_delete = QtWidgets.QLabel(self.page_eliminate)
        self.notification_delete.setMinimumSize(QtCore.QSize(200, 0))
        self.notification_delete.setText("")
        self.notification_delete.setAlignment(QtCore.Qt.AlignCenter)
        self.notification_delete.setObjectName("notification_delete")
        self.horizontalLayout_12.addWidget(self.notification_delete)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.stackedWidget.addWidget(self.page_eliminate)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_page)
        self.verticalLayout_2.addWidget(self.frame_main)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_database.setText(_translate("MainWindow", "Base de Datos"))
        self.bt_register.setText(_translate("MainWindow", "Registrar"))
        self.bt_update.setText(_translate("MainWindow", "Actualizar"))
        self.bt_delete.setText(_translate("MainWindow", "Eliminar"))
        self.label.setText(_translate("MainWindow", "Productos"))
        self.table_products.setSortingEnabled(False)
        item = self.table_products.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.table_products.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.table_products.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.table_products.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.table_products.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cantidad"))
        self.label_7.setText(_translate("MainWindow", "Registrar un producto"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.label_3.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Categoría"))
        self.label_5.setText(_translate("MainWindow", "Precio"))
        self.label_6.setText(_translate("MainWindow", "Cantidad"))
        self.bt_save_register.setText(_translate("MainWindow", "Guardar registro"))
        self.label_15.setText(_translate("MainWindow", "Actualizar datos de un producto"))
        self.label_16.setText(_translate("MainWindow", "Buacar Producto"))
        self.label_9.setText(_translate("MainWindow", "ID"))
        self.label_10.setText(_translate("MainWindow", "Nombre"))
        self.label_11.setText(_translate("MainWindow", "Categoría"))
        self.label_12.setText(_translate("MainWindow", "Precio"))
        self.label_13.setText(_translate("MainWindow", "Cantidad"))
        self.bt_save_update.setText(_translate("MainWindow", "Actualizar"))
        self.label_21.setText(_translate("MainWindow", "Eliminar un producto"))
        self.label_19.setText(_translate("MainWindow", "Buacar Producto a eliminar"))
        self.table_products_delete.setSortingEnabled(False)
        item = self.table_products_delete.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_products_delete.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.table_products_delete.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Categoria"))
        item = self.table_products_delete.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.table_products_delete.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cantidad"))
        self.bt_save_delete.setText(_translate("MainWindow", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
