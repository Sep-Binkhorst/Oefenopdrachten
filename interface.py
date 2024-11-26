from ui_simple_app import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtCore import Slot

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.AddText.clicked.connect(self.ui.textedit.clear)
        self.ui.Clear.clicked.connect(self.add_button_clicked)

        self.show()

    @Slot()
    def add_button_clicked(self):
        self.ui.textedit.append("You clicked me.")