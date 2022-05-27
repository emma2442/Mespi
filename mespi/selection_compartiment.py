import sqlite3

from PyQt5.QtWidgets import (QFormLayout, QPushButton, QWidget, QLabel, QSpacerItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from programmation_compartiment_1_prise import Programmation_compartiment_View, Programmation_compartiment_Controller, Programmation_compartiment_Model
from programmation_compartiment_2_prises import Programmation_compartiment_View_2, Programmation_compartiment_2_prises_Controller, Programmation_compartiment_2_prises_Model
from programmation_compartiment_3_prises import Programmation_compartiment_View_3, Programmation_compartiment_3_prises_Controller, Programmation_compartiment_3_prises_Model
from programmation_compartiment_4_prises import Programmation_compartiment_View_4, Programmation_compartiment_4_prises_Controller, Programmation_compartiment_4_prises_Model

class Selection_compartiment_View(QWidget):
    def __init__(self, fenetre_accueil, selection_compartiment_Model):
        super().__init__()

        self.fenetre_accueil = fenetre_accueil
        self.myModel = selection_compartiment_Model

        model_1_prise = Programmation_compartiment_Model()
        programmation_compartiment_Controller_1_prise = Programmation_compartiment_Controller(model_1_prise)
        self.compartiment_1_prise = Programmation_compartiment_View(self, programmation_compartiment_Controller_1_prise)

        model_2_prises = Programmation_compartiment_2_prises_Model()
        programmation_compartiment_Controller_2_prises = Programmation_compartiment_2_prises_Controller(model_2_prises)
        self.compartiment_2_prises = Programmation_compartiment_View_2(self.compartiment_1_prise, self, programmation_compartiment_Controller_2_prises)
        
        programmation_compartiment_3_prises_Model = Programmation_compartiment_3_prises_Model()
        programmation_compartiment_3_prises_Controller = Programmation_compartiment_3_prises_Controller(programmation_compartiment_3_prises_Model)
        self.compartiment_3_prises = Programmation_compartiment_View_3(self.compartiment_2_prises, self, programmation_compartiment_3_prises_Controller)
        
        programmation_compartiment_4_prises_Model = Programmation_compartiment_4_prises_Model()
        programmation_compartiment_4_prises_Controller = Programmation_compartiment_4_prises_Controller(programmation_compartiment_4_prises_Model)
        self.compartiment_4_prises = Programmation_compartiment_View_4(self.compartiment_3_prises, self, programmation_compartiment_4_prises_Controller)

        self.resize(300,500)
        self.setStyleSheet("background-color: #B2DEE6")
        self.verticalSpacer = QSpacerItem(5, 5) 

        self.label = QLabel("Selectionnez le compartiment")
        self.label.setAlignment(Qt.AlignCenter)

        self.compartiment_1 = QPushButton("1")
        self.compartiment_1.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_1.setMinimumWidth(30)

        self.compartiment_2 = QPushButton("2")
        self.compartiment_2.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_2.setMinimumWidth(30)

        self.compartiment_3 = QPushButton("3")
        self.compartiment_3.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_3.setMinimumWidth(30)

        self.compartiment_4 = QPushButton("4")
        self.compartiment_4.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_4.setMinimumWidth(30)

        self.compartiment_5 = QPushButton("5")
        self.compartiment_5.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_5.setMinimumWidth(30)

        self.compartiment_6 = QPushButton("6")
        self.compartiment_6.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_6.setMinimumWidth(30)

        self.compartiment_7 = QPushButton("7")
        self.compartiment_7.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_7.setMinimumWidth(30)

        self.compartiment_8 = QPushButton("8")
        self.compartiment_8.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.compartiment_8.setMinimumWidth(30)

        self.lbl_compartiment_1 = QLabel("Aucun médicament renseigné")
        self.lbl_compartiment_2 = QLabel("Aucun médicament renseigné")
        self.lbl_compartiment_3 = QLabel("Aucun médicament renseigné")
        self.lbl_compartiment_4 = QLabel("Aucun médicament renseigné")
        self.lbl_compartiment_5 = QLabel("Aucun médicament renseigné")
        self.lbl_compartiment_6 = QLabel("Aucun médicament renseigné")
        self.lbl_compartiment_7 = QLabel("Aucun médicament renseigné")
        self.lbl_compartiment_8 = QLabel("Aucun médicament renseigné")

        self.retour = QPushButton("Retour")
        self.retour.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.retour.clicked.connect(self.btn_retour)

        self.setWindowTitle("selection compartiment")
        self.setWindowIcon(QIcon('logo2.png'))

        self.init_ui()

        self.remplir_nom()

    def init_ui(self):

        box_finale = QFormLayout()
        box_finale.addRow(self.label)
        box_finale.addItem(self.verticalSpacer)
        box_finale.addRow(self.compartiment_1, self.lbl_compartiment_1)
        box_finale.addRow(self.compartiment_2, self.lbl_compartiment_2)
        box_finale.addRow(self.compartiment_3, self.lbl_compartiment_3)
        box_finale.addRow(self.compartiment_4, self.lbl_compartiment_4)
        box_finale.addRow(self.compartiment_5, self.lbl_compartiment_5)
        box_finale.addRow(self.compartiment_6, self.lbl_compartiment_6)
        box_finale.addRow(self.compartiment_7, self.lbl_compartiment_7)
        box_finale.addRow(self.compartiment_8, self.lbl_compartiment_8)
        box_finale.addItem(self.verticalSpacer)
        box_finale.addRow(self.retour)

        box_finale.setAlignment(Qt.AlignCenter)

        self.setLayout(box_finale)

        self.compartiment_1.clicked.connect(self.btn_compartiment_1)
        self.compartiment_2.clicked.connect(self.btn_compartiment_2)
        self.compartiment_3.clicked.connect(self.btn_compartiment_3)
        self.compartiment_4.clicked.connect(self.btn_compartiment_4)
        self.compartiment_5.clicked.connect(self.btn_compartiment_5)
        self.compartiment_6.clicked.connect(self.btn_compartiment_6)
        self.compartiment_7.clicked.connect(self.btn_compartiment_7)
        self.compartiment_8.clicked.connect(self.btn_compartiment_8)


    def btn_compartiment_1(self):
        self.close()
        id_compartiment = "Compartiment 1"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)


    def btn_compartiment_2(self):
        self.close()
        id_compartiment = "Compartiment 2"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)

    def btn_compartiment_3(self):
        self.close()
        id_compartiment = "Compartiment 3"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)

    def btn_compartiment_4(self):
        self.close()
        id_compartiment = "Compartiment 4"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)

    def btn_compartiment_5(self):
        self.close()
        id_compartiment = "Compartiment 5"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)

    def btn_compartiment_6(self):
        self.close()
        id_compartiment = "Compartiment 6"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)

    def btn_compartiment_7(self):
        self.close()
        id_compartiment = "Compartiment 7"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)

    def btn_compartiment_8(self):
        self.close()
        id_compartiment = "Compartiment 8"
        a = self.myModel.trouver_nb_prise(id_compartiment)
        if a == 1 :
            self.compartiment_1_prise.show()
            self.compartiment_1_prise.compartiment_selectionne(id_compartiment)
        if a == 2 :
            self.compartiment_2_prises.show()
            self.compartiment_2_prises.compartiment_selectionne(id_compartiment)
        if a == 3 :
            self.compartiment_3_prises.show()
            self.compartiment_3_prises.compartiment_selectionne(id_compartiment)
        if a == 4 :
            self.compartiment_4_prises.show()
            self.compartiment_4_prises.compartiment_selectionne(id_compartiment)

    def btn_retour(self):
        self.close()
        self.fenetre_accueil.show()

    def remplir_nom(self):
        nom_1 = self.myModel.remplir_nom_m("Compartiment 1")
        try :
            self.lbl_compartiment_1.setText(nom_1[0])
        except : self.lbl_compartiment_1.setText("Aucun médicament renseigné")

        nom_2 = self.myModel.remplir_nom_m("Compartiment 2")
        try :
            self.lbl_compartiment_2.setText(nom_2[0])
        except : self.lbl_compartiment_2.setText("Aucun médicament renseigné")

        nom_3 = self.myModel.remplir_nom_m("Compartiment 3")
        try :
            self.lbl_compartiment_3.setText(nom_3[0])
        except : self.lbl_compartiment_3.setText("Aucun médicament renseigné")

        nom_4 = self.myModel.remplir_nom_m("Compartiment 4")
        try :
            self.lbl_compartiment_4.setText(nom_4[0])
        except : self.lbl_compartiment_4.setText("Aucun médicament renseigné")

        nom_5 = self.myModel.remplir_nom_m("Compartiment 5")
        try :
            self.lbl_compartiment_5.setText(nom_5[0])
        except : self.lbl_compartiment_5.setText("Aucun médicament renseigné")

        nom_6 = self.myModel.remplir_nom_m("Compartiment 6")
        try :
            self.lbl_compartiment_6.setText(nom_6[0])
        except : self.lbl_compartiment_6.setText("Aucun médicament renseigné")

        nom_7 = self.myModel.remplir_nom_m("Compartiment 7")
        try :
            self.lbl_compartiment_7.setText(nom_7[0])
        except : self.lbl_compartiment_7.setText("Aucun médicament renseigné")

        nom_8 = self.myModel.remplir_nom_m("Compartiment 8")
        try :
            self.lbl_compartiment_8.setText(nom_8[0])
        except : self.lbl_compartiment_8.setText("Aucun médicament renseigné")
    
class Selection_compartiment_Model:

    def remplir_nom_m(self, id_compartiment):
        conn = sqlite3.connect('compartiments.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT medicament FROM compartiments WHERE id_compartiment=?""", (id_compartiment,))
        nom_compartiment = cursor.fetchone()    
        conn.close()
        return nom_compartiment

    def trouver_nb_prise(self, id_compartiment):
        conn = sqlite3.connect('compartiments.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT medicament, lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche,
                        prise_1, prise_2, prise_3, prise_4 FROM compartiments WHERE id_compartiment=?""", (id_compartiment,))
        data_compartiment = cursor.fetchone()
        conn.close()

        try : 
            if data_compartiment[11] == None :
                if data_compartiment[10] == None :
                    if data_compartiment[9] == None :
                        a = 1
                    else :
                        a = 2
                else :
                    a = 3
            else :
                a = 4
        except :
            a = 1

        return a
