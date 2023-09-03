import sys
import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from connect import Connect
from interface import Ui_MainWindow


class MainInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mousePress = None
        self.bt_minimun.hide()
        self.database = Connect()
        self.set_page_database()

        self.bt_close.clicked.connect(lambda: self.close())
        self.bt_maximun.clicked.connect(self.maximun_window)
        self.bt_minimun.clicked.connect(self.minimun_window)
        self.bt_minimize.clicked.connect(self.minimize_window)

        self.bt_database.clicked.connect(self.set_page_database)
        self.bt_register.clicked.connect(self.set_page_register)
        self.bt_update.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_update))
        self.bt_delete.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminate))

        self.bt_save_register.clicked.connect(self.save_register)
        self.bt_save_update.clicked.connect(self.save_update)
        self.bt_save_delete.clicked.connect(self.save_delete)

        self.frame_header.mouseMoveEvent = self.move_window
        self.table_products.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.windowOpacity()

    def maximun_window(self):
        self.showMaximized()
        self.bt_maximun.hide()
        self.bt_minimun.show()

    def minimun_window(self):
        self.showNormal()
        self.bt_minimun.hide()
        self.bt_maximun.show()

    def minimize_window(self):
        self.showMinimized()

    def mousePressEvent(self, event):
        self.mousePress = event.globalPos()

    def move_window(self, event):
        if not self.isMaximized():
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.mousePress)
                self.mousePress = event.globalPos()
                event.accept()

        if event.globalPos().y() < 1:
            self.maximun_window()
        else:
            self.minimun_window()

    def set_page_database(self):
        self.stackedWidget.setCurrentWidget(self.page_database)
        data_products = self.database.show()

        self.table_products.setRowCount(len(data_products))
        for row, data_product in enumerate(data_products):
            for col, data in enumerate(data_product):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.table_products.setItem(row, col, item)

    def set_page_register(self):
        self.stackedWidget.setCurrentWidget(self.page_register)
        self.ln_register_id.setText(str(len(self.database.show()) + 1))

    def save_register(self):
        self.ln_register_id.text()
        name = self.ln_register_name.text()
        category = self.ln_register_category.text()
        price = self.ln_register_price.text()
        quantity = self.ln_register_quantity.text()
        if name == "" or category == "" or price == "" or quantity == "":
            self.notification_register.setText("Hay campos vacios")
            return
        else:
            self.notification_register.setText("Se registro el Producto")

        self.database.insert(name, price, category, quantity)

        self.ln_register_id.clear()
        self.ln_register_name.clear()
        self.ln_register_category.clear()
        self.ln_register_price.clear()
        self.ln_register_quantity.clear()



    def save_update(self):
        print(7)

    def save_delete(self):
        print(9)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainInterface()
    window.show()
    sys.exit(app.exec_())
