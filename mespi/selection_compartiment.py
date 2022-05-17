import sys

from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QWidget, QLabel, QLineEdit, QCheckBox,
                                QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib.pyplot import box

class Programmation_compartiment_View(QWidget):
    def __init__(self):
        super().__init__()

#        self.dossier = Dossier(self, dossierController)
#        self.importer2 = Importer(self, importerController)     
  
        self.resize(300,500)
        self.setStyleSheet("background-color: #B2DEE6")

        self.verticalSpacer = QSpacerItem(10, 10) 


        self.label_medicament = QLabel("Médicament :")
        self.label_medicament.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 5px ; color : white")
        self.nom_medicament = QLineEdit()
        self.nom_medicament.setStyleSheet("background-color : #C0DEE6 ; color : black")
        self.nom_medicament.setPlaceholderText("nom")

        self.label_reccurence = QLabel("Récurrence :")
        self.label_reccurence.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 5px ; color : white")
        
        self.checkbox_lundi = QCheckBox()
        self.label_L = QLabel("L")
        self.label_L.setAlignment(Qt.AlignCenter)
        self.checkbox_mardi = QCheckBox()
        self.label_M = QLabel("M")
        self.label_M.setAlignment(Qt.AlignCenter)
        self.checkbox_mercredi = QCheckBox()
        self.label_M2 = QLabel("M")
        self.label_M2.setAlignment(Qt.AlignCenter)
        self.checkbox_jeudi = QCheckBox()
        self.label_J = QLabel("J")
        self.label_J.setAlignment(Qt.AlignCenter)
        self.checkbox_vendredi = QCheckBox()
        self.label_V = QLabel("V")
        self.label_V.setAlignment(Qt.AlignCenter)
        self.checkbox_samedi = QCheckBox()
        self.label_S = QLabel("S")
        self.label_S.setAlignment(Qt.AlignCenter)
        self.checkbox_dimanche = QCheckBox()
        self.label_D = QLabel("D")
        self.label_D.setAlignment(Qt.AlignCenter)

        self.label_prise_1 = QLabel("Prise n°1 :")
        self.label_prise_1.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 5px ; color : white")
        self.prise_1 = QLineEdit()
        self.prise_1.setPlaceholderText("xx")
        self.prise_1.setMaximumWidth(25)
        self.prise_1.setStyleSheet("background-color : #C0DEE6 ; color : black")
        self.label_h = QLabel("h")

        self.ajout_prise = QPushButton("+")
        self.ajout_prise.setStyleSheet("background-color : #0B848C ; border-radius: 15% ; padding: 10px ; color : white")
        self.ajout_prise.setMaximumWidth(35)

        self.setWindowTitle("programmation compartiment")
        self.setWindowIcon(QIcon('logo2.png'))

        self.init_ui()

    def init_ui(self):

        box_medicament = QHBoxLayout()
        box_medicament.addWidget(self.label_medicament)
        box_medicament.addSpacing(10)
        box_medicament.addWidget(self.nom_medicament)

        box_lundi = QVBoxLayout()
        box_lundi.addWidget(self.checkbox_lundi)
        box_lundi.addWidget(self.label_L)
#        box_lundi.setAlignment(Qt.AlignHCenter)

        box_mardi = QVBoxLayout()
        box_mardi.addWidget(self.checkbox_mardi)
        box_mardi.addWidget(self.label_M)
#        box_mardi.setAlignment(Qt.AlignHCenter)

        box_mercredi = QVBoxLayout()
        box_mercredi.addWidget(self.checkbox_mercredi)
        box_mercredi.addWidget(self.label_M2)
#        box_mercredi.setAlignment(Qt.AlignHCenter)

        box_jeudi = QVBoxLayout()
        box_jeudi.addWidget(self.checkbox_jeudi)
        box_jeudi.addWidget(self.label_J)
#        box_jeudi.setAlignment(Qt.AlignHCenter)

        box_vendredi = QVBoxLayout()
        box_vendredi.addWidget(self.checkbox_vendredi)
        box_vendredi.addWidget(self.label_V)
#        box_vendredi.setAlignment(Qt.AlignHCenter)

        box_samedi = QVBoxLayout()
        box_samedi.addWidget(self.checkbox_samedi)
        box_samedi.addWidget(self.label_S)

        box_dimanche = QVBoxLayout()
        box_dimanche.addWidget(self.checkbox_dimanche)
        box_dimanche.addWidget(self.label_D)
#        box_dimanche.setAlignment(Qt.AlignHCenter)

        box_jours = QHBoxLayout()
        box_jours.addLayout(box_lundi)
        box_jours.addLayout(box_mardi)
        box_jours.addLayout(box_mercredi)
        box_jours.addLayout(box_jeudi)
        box_jours.addLayout(box_vendredi)
        box_jours.addLayout(box_samedi)
        box_jours.addLayout(box_dimanche)

        box_recurrence = QVBoxLayout()
        box_recurrence.addWidget(self.label_reccurence, 0, Qt.AlignLeft)
        box_recurrence.addItem(self.verticalSpacer)
        box_recurrence.addLayout(box_jours)
#        box_recurrence.addWidget(QLabel(" "))

        box_prise_1 = QHBoxLayout()
        box_prise_1.addWidget(self.label_prise_1)
        box_prise_1.addWidget(self.prise_1, 0, Qt.AlignLeft)
        box_prise_1.addWidget(self.label_h, 0, Qt.AlignLeft)
#        box_prise_1.addItem(self.verticalSpacer)
        box_prise_1.setAlignment(Qt.AlignLeft)

        box_ajout = QHBoxLayout()
        box_ajout.addWidget(self.ajout_prise)

        box_finale = QVBoxLayout()
        box_finale.addLayout(box_medicament)
        box_finale.addSpacing(10)
        box_finale.addLayout(box_recurrence)
        box_finale.addSpacing(10)
        box_finale.addLayout(box_prise_1)
        box_finale.addSpacing(20)
        box_finale.addLayout(box_ajout)
        box_finale.setAlignment(Qt.AlignCenter)

        self.setLayout(box_finale)

        self.ajout_prise.clicked.connect(self.btn_ajout_prise)


    def btn_ajout_prise(self):
        self.hide()
        self.programmation_medicament_prise_2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
