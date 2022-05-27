import sys

from PyQt5.QtWidgets import (QVBoxLayout, QPushButton, QApplication, QWidget, QLabel)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from selection_compartiment import Selection_compartiment_View, Selection_compartiment_Model
from selection_medicament_supplementaire import Selection_medicament_supplementaire_View, Selection_medicament_supplementaire_Model
from programmation_compartiment_1_prise import Programmation_compartiment_Controller, Programmation_compartiment_Model

#from calendrier import calendrier_View  

class Accueil_View(QWidget):
    def __init__(self, programmation_compartiment_Controller, selection_compartiment_Model):
        super().__init__() 
        
        selection_compartiment_Model = Selection_compartiment_Model()
        self.selection_compartiment = Selection_compartiment_View(self, selection_compartiment_Model)

        selection_medicament_supplementaire_Model = Selection_medicament_supplementaire_Model()
        self.selection_medicament_supplementaire = Selection_medicament_supplementaire_View(self, selection_medicament_supplementaire_Model)
    
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

        self.ajout_medicament = QPushButton("Programmer d'autres médicaments")
        self.ajout_medicament.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.calendrier = QPushButton("Calendrier")
        self.calendrier.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.setWindowTitle("Menu")
        self.setWindowIcon(QIcon('logo2.png'))

        self.init_ui()
        self.show()

    def init_ui(self):

        box_finale = QVBoxLayout()
        box_finale.addWidget(self.logo)
        box_finale.addWidget(self.nom_plateforme)
        box_finale.addWidget(self.message_bienvenue)
        box_finale.addWidget(self.programmer)
        box_finale.addWidget(self.ajout_medicament)
        box_finale.addWidget(self.calendrier)
        box_finale.setAlignment(Qt.AlignCenter)

        self.setLayout(box_finale)

        self.programmer.clicked.connect(self.btn_programmer)
        self.ajout_medicament.clicked.connect(self.btn_medicament_supplementaire)
        self.calendrier.clicked.connect(self.btn_calendrier)

    def btn_programmer(self):
        self.hide()
        self.selection_compartiment.show()

    def btn_medicament_supplementaire(self):
        self.hide()
        self.selection_medicament_supplementaire.show()

    def btn_calendrier(self):
        self.hide()
#        self.calendrier2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Programmation_compartiment_Model()
    programmation_compartiment_Controller = Programmation_compartiment_Controller(Programmation_compartiment_Model)
    selection_compartiment_Model = Selection_compartiment_Model()
    selection_compartiment = Selection_compartiment_View(programmation_compartiment_Controller, selection_compartiment_Model)
    menu = Accueil_View(programmation_compartiment_Controller,selection_compartiment) 
    sys.exit(app.exec_())