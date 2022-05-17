import sys

from PyQt5.QtWidgets import (QVBoxLayout, QPushButton, QApplication, QWidget, QLabel)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from selection_compartiment import Selection_compartiment_View
#from calendrier import calendrier_View

class Accueil_View(QWidget):
    def __init__(self):
        super().__init__()

        self.selection_compartiment = Selection_compartiment_View()
#        self.calendrier = calendrier(self, calendrierController)     
  
        self.resize(300,500)
        self.setStyleSheet("background-color: #B2DEE6")

        self.logo = QLabel(self)
        self.pixmap = QPixmap('logo2.png')
        self.logo.setPixmap(self.pixmap.scaled(100,100))
        self.logo.setAlignment(Qt.AlignCenter)

        self.nom_plateforme = QLabel("e-pilulier \n \n")
        self.nom_plateforme.setAlignment(Qt.AlignCenter)
        self.nom_plateforme.setStyleSheet("color : #0B848C")
        self.message_bienvenue = QLabel("Bienvenue sur l'application du pilulier")
        self.message_bienvenue.setAlignment(Qt.AlignCenter)

        self.programmer = QPushButton("Programmer les compartiments")
        self.programmer.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.ajout_medicament = QPushButton("Ajouter un autre médicament")
        self.ajout_medicament.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.calendrier = QPushButton("Calendrier")
        self.calendrier.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon('logo2.png'))

        self.init_ui()
        self.show()

    def init_ui(self):

        h_box = QVBoxLayout()
        h_box.addWidget(self.logo)
        h_box.addWidget(self.nom_plateforme)
        h_box.addWidget(self.message_bienvenue)
        h_box.addWidget(self.programmer)
        h_box.addWidget(self.ajout_medicament)
        h_box.addWidget(self.calendrier)
        h_box.setAlignment(Qt.AlignCenter)

        self.setLayout(h_box)

        self.programmer.clicked.connect(self.btn_programmer)
        self.calendrier.clicked.connect(self.btn_calendrier)

    def btn_programmer(self):
        self.hide()
        self.selection_compartiment.show()

    def btn_calendrier(self):
        self.hide()
        self.calendrier2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Accueil_View() 
    sys.exit(app.exec_())
