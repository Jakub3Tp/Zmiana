import sys
from cgitb import small

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.change.clicked.connect(self.button_clicked)
        self.ui.edit.textChanged.connect(self.button_clicked)
        self.show()

    def button_clicked(self):
        if self.ui.big.isChecked():
            self.ui.edit.setText(self.ui.edit.text().upper())

        if self.ui.reverse.isChecked():
            self.ui.edit.setText(self.ui.edit.text()[::-1])

        if self.ui.small.isChecked():
            self.ui.edit.setText(self.ui.edit.text().lower())

        self.ui.result.setText(self.ui.edit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())