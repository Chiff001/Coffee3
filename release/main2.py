import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class SecondForm(QMainWindow):
    def __init__(self, db):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.connection = sqlite3.connect(db)
        self.cur = self.connection.cursor()
        self.pushButton.clicked.connect(self.push_2)

    def push_2(self):
        self.cur.execute(f'insert into coffee (Кофе, Цена) values ("{self.lineEdit.text()}", {self.lineEdit_2.text()})').fetchall()
        self.connection.commit()
        self.destroy()