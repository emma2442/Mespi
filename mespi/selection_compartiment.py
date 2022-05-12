import sys

from PyQt5.QtWidgets import (QFormLayout, QPushButton, QApplication, QWidget, QLabel)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from programmation_compartiment import Programmation_compartiment_View

class Selection_compartiment_View(QWidget):
    def __init__(self):
        super().__init__()

        self.compartiment = Programmation_compartiment_View()
#        self.dossier = Dossier(self, dossierController)
#        self.importer2 = Importer(self, importerController)     
  
        self.resize(300,200)

        self.label = QLabel("Selectionnez le compartiment")
        self.label.setAlignment(Qt.AlignCenter)

        self.compartiment_1 = QPushButton("1")
        self.compartiment_1.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_1.setMinimumWidth(150)

        self.compartiment_2 = QPushButton("2")
        self.compartiment_2.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.compartiment_3 = QPushButton("3")
        self.compartiment_3.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.compartiment_4 = QPushButton("4")
        self.compartiment_4.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.setWindowTitle("selection compartiment")
        self.setWindowIcon(QIcon('logo2.png'))

        self.init_ui()

    def init_ui(self):

        h_box = QFormLayout()
        h_box.addRow(self.label)
        h_box.addRow(self.compartiment_1, QLabel("aucun médicament renseigné"))
        h_box.addWidget(self.compartiment_2)
        h_box.addWidget(self.compartiment_3)
        h_box.addWidget(self.compartiment_4)
        h_box.setAlignment(Qt.AlignCenter)

        self.setLayout(h_box)

        self.compartiment_1.clicked.connect(self.btn_compartiment_1)
        self.compartiment_2.clicked.connect(self.btn_compartiment_2)
        self.compartiment_3.clicked.connect(self.btn_compartiment_3)
        self.compartiment_4.clicked.connect(self.btn_compartiment_4)

    def btn_compartiment_1(self):
        self.hide()
        self.compartiment.show()

    def btn_compartiment_2(self):
        self.hide()
        self.compartiment.show()

    def btn_compartiment_3(self):
        self.hide()
        self.compartiment.show()

    def btn_compartiment_4(self):
        self.hide()
        self.compartiment.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())