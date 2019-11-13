import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class ADD(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add_btn.clicked.connect(self.d)

    def d(self):
        con = sqlite3.connect("coffees.db")
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO coffee(Name, degree_of_roasting, ground, taste, cost, volume)"
            f" VALUES('{self.lineEdit.text()}', '{self.lineEdit_2.text()}', '{self.lineEdit_3.text()}',"
            f" '{self.lineEdit_4.text()}', '{self.lineEdit_5.text()}', '{self.lineEdit_6.text()}')")
        con.commit()
        con.close()
        self.up = MyWidget()
        self.up.show()
        self.hide()


class UP(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm_UPDATE.ui', self)
        self.up_btn.clicked.connect(self.dd)

    def dd(self):
        con = sqlite3.connect("coffees.db")
        cur = con.cursor()
        if self.lineEdit.text() != '':
            cur.execute(f"UPDATE coffee SET Name = '{self.lineEdit.text()}' WHERE ID = {int(self.lineEdit_7.text())}")
        if self.lineEdit_2.text() != '':
            cur.execute(
                f"UPDATE coffee SET degree_of_roasting = '{self.lineEdit_2.text()}'"
                f" WHERE ID = {int(self.lineEdit_7.text())}")
        if self.lineEdit_3.text() != '':
            cur.execute(
                f"UPDATE coffee SET ground = '{self.lineEdit_3.text()}' WHERE ID = {int(self.lineEdit_7.text())}")
        if self.lineEdit_4.text() != '':
            cur.execute(
                f"UPDATE coffee SET taste = '{self.lineEdit_4.text()}' WHERE ID = {int(self.lineEdit_7.text())}")
        if self.lineEdit_5.text() != '':
            cur.execute(f"UPDATE coffee SET cost = '{self.lineEdit_5.text()}' WHERE ID = {int(self.lineEdit_7.text())}")
        if self.lineEdit_6.text() != '':
            cur.execute(
                f"UPDATE coffee SET volume = '{self.lineEdit_6.text()}' WHERE ID = {int(self.lineEdit_7.text())}")
        # cur.execute(f"UPDATE coffee SET Name = '{self.lineEdit.text()}',"
        #             f" degree_of_roasting = '{self.lineEdit_2.text()}',"
        #             f" ground = '{self.lineEdit_3.text()}', taste = '{self.lineEdit_4.text()}',"
        #             f" cost = '{self.lineEdit_5.text()}', volume = '{self.lineEdit_6.text()}'"
        #             f" WHERE ID = {int(self.lineEdit_7.text())}")
        con.commit()
        con.close()
        self.up = MyWidget()
        self.up.show()
        self.hide()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        # Подключение к БД
        con = sqlite3.connect("coffees.db")
        # Создание курсора
        cur = con.cursor()
        # Выполнение запроса и получение всех результатов
        self.result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(
            ["id", "title", "degree of roasting", "ground in grains", "the description of the taste", "cost",
             "the amount of taste"])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(self.result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
        con.commit()
        con.close()
        self.pushButton.clicked.connect(self.ad)
        self.pushButton_2.clicked.connect(self.up)

    def ad(self):
        self.window = ADD()
        self.window.show()
        self.hide()

    def up(self):
        self.w = UP()
        self.w.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
