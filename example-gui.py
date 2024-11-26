
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot



class UserInterface(QtWidgets.QMainWindow):
    pass

    def __init__(self):
        # roep de __init__() aan van de parent class
        super().__init__()

        # elk QMainWindow moet een central widget hebben
        # hierbinnen maak je een layout en hang je andere widgets
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # voeg geneste layouts en widgets toe
        vbox = QtWidgets.QVBoxLayout(central_widget)
        self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.textedit)
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox)
        qbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(qbox)


        clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(clear_button)
        add_text_button = QtWidgets.QPushButton("Add text")
        hbox.addWidget(add_text_button)
        hello_world_button = QtWidgets.QPushButton("Hello, world")
        hbox.addWidget(hello_world_button)
        quit_button = QtWidgets.QPushButton("Quit")
        qbox.addWidget(quit_button)

        # Slots and signals
        clear_button.clicked.connect(self.textedit.clear)
        add_text_button.clicked.connect(self.add_text_button_clicked)
        hello_world_button.clicked.connect(self.hello_world)
        quit_button.clicked.connect(self.close)

    @Slot()
    def add_text_button_clicked(self):
        self.textedit.append("You clicked me.")
    
    def hello_world(self):
        self.textedit.append("Hello, world")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  
