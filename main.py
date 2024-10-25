import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.copyButton.clicked.connect(self.copy)
        self.ui.pasteButton.clicked.connect(self.paste)
        self.ui.resultEdit.setReadOnly(True)
        self.show()

    def copy(self):
        self.text = self.ui.dataEdit.text()

    def paste(self):
        self.ui.resultEdit.setText(self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())