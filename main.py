import sys
from cgitb import small

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

    def durze(self):
        if self.ui.big.isChecked():
            self.ui.edit.text.lower
    def male(self):
        if self.ui.small.isChecked():
            self.ui.edit.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())