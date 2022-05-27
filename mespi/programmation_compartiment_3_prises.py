import sqlite3

from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QCheckBox, QSpacerItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from programmation_compartiment_4_prises import Programmation_compartiment_View_4, Programmation_compartiment_4_prises_Controller, Programmation_compartiment_4_prises_Model

class Programmation_compartiment_View_3(QWidget):
    def __init__(self, fenetre_2_prises, fenetre_selection, controller):
        super().__init__()

        self.fenetre_selection = fenetre_selection
        self.fenetre_2_prises = fenetre_2_prises

        self.myController = controller

        programmation_compartiment_4_prises_Model = Programmation_compartiment_4_prises_Model()
        programmation_compartiment_4_prises_Controller = Programmation_compartiment_4_prises_Controller(programmation_compartiment_4_prises_Model)
        self.programmation_medicament_4_prises = Programmation_compartiment_View_4(self, fenetre_selection, programmation_compartiment_4_prises_Controller)

        self.resize(300, 500)
        self.setStyleSheet("background-color: #B2DEE6")

        self.verticalSpacer = QSpacerItem(10, 10) 
        self.label_numero_compartiment = QLabel()
        self.label_numero_compartiment.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")
        self.label_numero_compartiment.setMaximumWidth(150)

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
        self.label_prise_1.setFixedWidth(80)
        self.prise_1 = QLineEdit()
        self.prise_1.setPlaceholderText("00")
        self.prise_1.setMaximumWidth(25)
        self.prise_1.setStyleSheet("background-color : #C0DEE6 ; color : black")
        self.label_h = QLabel("h")
        
        self.label_prise_2 = QLabel("Prise n°2 :")
        self.label_prise_2.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 5px ; color : white")
        self.label_prise_2.setFixedWidth(80)
        self.prise_2 = QLineEdit()
        self.prise_2.setPlaceholderText("00")
        self.prise_2.setMaximumWidth(25)
        self.prise_2.setStyleSheet("background-color : #C0DEE6 ; color : black")
        self.label_h_2 = QLabel("h")

        self.label_prise_3 = QLabel("Prise n°3 :")
        self.label_prise_3.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 5px ; color : white")
        self.label_prise_3.setFixedWidth(80)
        self.prise_3 = QLineEdit()
        self.prise_3.setPlaceholderText("00")
        self.prise_3.setMaximumWidth(25)
        self.prise_3.setStyleSheet("background-color : #C0DEE6 ; color : black")
        self.label_h_3 = QLabel("h")

        self.supp_prise = QPushButton("x")
        self.supp_prise.setStyleSheet("color : #878787 ; border-style : None ; background-color : #B2DEE6 ; max-width: 3em")
        self.ajout_prise = QPushButton("+")
        self.ajout_prise.setStyleSheet("color : #0B848C ; font-size: 18px ; border-style : None ; background-color : #B2DEE6 ; max-width: 3em")
        self.ajout_prise.setMaximumWidth(35)

        self.retour = QPushButton("Retour")
        self.retour.setStyleSheet("background-color : #0B848C ; border-radius: 10% ; padding: 10px ; color : white")

        self.supp_prise.clicked.connect(self.btn_supp_prise)
        self.retour.clicked.connect(self.btn_retour)

        self.setWindowTitle("programmation compartiment")
        self.setWindowIcon(QIcon('logo2.png'))

        self.init_ui()

    def init_ui(self):

        box_numero_compartiment = QVBoxLayout()
        box_numero_compartiment.addWidget(self.label_numero_compartiment)
        box_numero_compartiment.setAlignment(Qt.AlignCenter)

        box_medicament = QHBoxLayout()
        box_medicament.addWidget(self.label_medicament)
        box_medicament.addSpacing(10)
        box_medicament.addWidget(self.nom_medicament)

        box_lundi = QVBoxLayout()
        box_lundi.addWidget(self.checkbox_lundi)
        box_lundi.addWidget(self.label_L)

        box_mardi = QVBoxLayout()
        box_mardi.addWidget(self.checkbox_mardi)
        box_mardi.addWidget(self.label_M)

        box_mercredi = QVBoxLayout()
        box_mercredi.addWidget(self.checkbox_mercredi)
        box_mercredi.addWidget(self.label_M2)

        box_jeudi = QVBoxLayout()
        box_jeudi.addWidget(self.checkbox_jeudi)
        box_jeudi.addWidget(self.label_J)

        box_vendredi = QVBoxLayout()
        box_vendredi.addWidget(self.checkbox_vendredi)
        box_vendredi.addWidget(self.label_V)

        box_samedi = QVBoxLayout()
        box_samedi.addWidget(self.checkbox_samedi)
        box_samedi.addWidget(self.label_S)

        box_dimanche = QVBoxLayout()
        box_dimanche.addWidget(self.checkbox_dimanche)
        box_dimanche.addWidget(self.label_D)

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

        box_prise_1 = QHBoxLayout()
        box_prise_1.addWidget(self.label_prise_1)
        box_prise_1.addWidget(self.prise_1, 0, Qt.AlignLeft)
        box_prise_1.addWidget(self.label_h, 0, Qt.AlignLeft)
        box_prise_1.setAlignment(Qt.AlignLeft)

        box_prise_2 = QHBoxLayout()
        box_prise_2.addWidget(self.label_prise_2)
        box_prise_2.addWidget(self.prise_2, 0, Qt.AlignLeft)
        box_prise_2.addWidget(self.label_h_2, 0, Qt.AlignLeft)
        box_prise_2.setAlignment(Qt.AlignLeft)

        box_prise_3 = QHBoxLayout()
        box_prise_3.addWidget(self.label_prise_3)
        box_prise_3.addWidget(self.prise_3, 0, Qt.AlignLeft)
        box_prise_3.addWidget(self.label_h_3, 0, Qt.AlignLeft)
        box_prise_3.addSpacing(90)
        box_prise_3.addWidget(self.supp_prise)
        box_prise_3.setAlignment(Qt.AlignLeft)

        box_ajout = QVBoxLayout()
        box_ajout.addWidget(self.ajout_prise)
        box_ajout.setAlignment(Qt.AlignAbsolute)

        box_retour = QVBoxLayout()
        box_retour.addWidget(self.retour)
        box_retour.setAlignment(Qt.AlignHCenter)

        box_finale = QVBoxLayout()
        box_finale.addLayout(box_numero_compartiment)
        box_finale.addSpacing(40)
        box_finale.addLayout(box_medicament)
        box_finale.addSpacing(10)
        box_finale.addLayout(box_recurrence)
        box_finale.addSpacing(10)
        box_finale.addLayout(box_prise_1)
        box_finale.addSpacing(5)
        box_finale.addLayout(box_prise_2)
        box_finale.addLayout(box_prise_3)
        box_finale.addSpacing(20)
        box_finale.addLayout(box_ajout)
        box_finale.addLayout(box_retour)
        box_finale.setAlignment(Qt.AlignCenter)

        self.setLayout(box_finale)

        self.ajout_prise.clicked.connect(self.btn_ajout_prise)

    def btn_ajout_prise(self):
        self.hide()
        self.programmation_medicament_4_prises.show()
        self.myController.enregistrer(self.label_numero_compartiment.text(), self.nom_medicament.text(), 
        self.checkbox_lundi.isChecked(), self.checkbox_mardi.isChecked(), self.checkbox_mercredi.isChecked(),
        self.checkbox_jeudi.isChecked(), self.checkbox_vendredi.isChecked(), self.checkbox_samedi.isChecked(),
        self.checkbox_dimanche.isChecked(), self.prise_1.text(), self.prise_2.text(), self.prise_3.text())
        self.programmation_medicament_4_prises.compartiment_selectionne(self.label_numero_compartiment.text())

    def btn_supp_prise(self):
        self.myController.enregistrer(self.label_numero_compartiment.text(), self.nom_medicament.text(), 
        self.checkbox_lundi.isChecked(), self.checkbox_mardi.isChecked(), self.checkbox_mercredi.isChecked(),
        self.checkbox_jeudi.isChecked(), self.checkbox_vendredi.isChecked(), self.checkbox_samedi.isChecked(),
        self.checkbox_dimanche.isChecked(), self.prise_1.text(), self.prise_2.text(), self.prise_3.text())
        self.myController.supp_prise()
        self.fenetre_2_prises.show()
        self.fenetre_2_prises.compartiment_selectionne(self.label_numero_compartiment.text())
        self.hide()

    def btn_retour(self):
        self.hide()
        self.fenetre_selection.show()
        self.myController.enregistrer(self.label_numero_compartiment.text(), self.nom_medicament.text(), 
        self.checkbox_lundi.isChecked(), self.checkbox_mardi.isChecked(), self.checkbox_mercredi.isChecked(),
        self.checkbox_jeudi.isChecked(), self.checkbox_vendredi.isChecked(), self.checkbox_samedi.isChecked(),
        self.checkbox_dimanche.isChecked(), self.prise_1.text(), self.prise_2.text(), self.prise_3.text())

    def compartiment_selectionne(self, lbl_numero_compartiment):
        self.label_numero_compartiment.setText(lbl_numero_compartiment)
        data_compartiment = self.myController.recupere_data_compartiment(lbl_numero_compartiment)
        self.remplir(data_compartiment)

    def remplir(self, data_compartiment):
        try : 
                self.nom_medicament.setText(data_compartiment[0])
                self.prise_1.setText(str(data_compartiment[8]))
                self.prise_2.setText(str(data_compartiment[9]))
                if data_compartiment[10] != None :
                    self.prise_3.setText(str(data_compartiment[10]))
                self.checkbox_lundi.setChecked(data_compartiment[1])
                self.checkbox_mardi.setChecked(data_compartiment[2])
                self.checkbox_mercredi.setChecked(data_compartiment[3])
                self.checkbox_jeudi.setChecked(data_compartiment[4])
                self.checkbox_vendredi.setChecked(data_compartiment[5])
                self.checkbox_samedi.setChecked(data_compartiment[6])
                self.checkbox_dimanche.setChecked(data_compartiment[7])
        except : 
                self.nom_medicament.clear()
                self.prise_1.clear()
                self.prise_2.clear()
                self.prise_3.clear()
                self.checkbox_lundi.setChecked(0)
                self.checkbox_mardi.setChecked(0)
                self.checkbox_mercredi.setChecked(0)
                self.checkbox_jeudi.setChecked(0)
                self.checkbox_vendredi.setChecked(0)
                self.checkbox_samedi.setChecked(0)
                self.checkbox_dimanche.setChecked(0)


class Programmation_compartiment_3_prises_Controller:
    def __init__(self, model):
        self.myModel = model

    def recupere_data_compartiment(self, id_compartiment):
        return self.myModel.recupere_data_compartiment_m(id_compartiment)

    def enregistrer(self, label_numero_compartiment, nom_medicament, lundi, mardi, mercredi, jeudi,
                        vendredi, samedi, dimanche, prise_1, prise_2, prise_3):
        self.myModel.enregistrer_m(label_numero_compartiment, nom_medicament, lundi, mardi, mercredi, jeudi,
                                vendredi, samedi, dimanche, prise_1, prise_2, prise_3)

    def supp_prise(self):
        self.myModel.supp_prise_m()

class Programmation_compartiment_3_prises_Model:
        def __init__(self):

                conn = sqlite3.connect('compartiments.db')
                cursor = conn.cursor()
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS compartiments(
                id_compartiment TEXT PRIMARY KEY,
                medicament TEXT,
                lundi INTEGER,
                mardi INTEGER,
                mercredi INTEGER,
                jeudi INTEGER,
                vendredi INTEGER,
                samedi INTEGER,
                dimanche INTEGER,
                prise_1 INTEGER,
                prise_2 INTEGER,
                prise_3 INTEGER,
                prise_4 INTEGER
                )
                """)
                conn.commit()
                conn.close()
        
        def recupere_data_compartiment_m(self, id_compartiment):
                conn = sqlite3.connect('compartiments.db')
                cursor = conn.cursor()
                cursor.execute("""SELECT medicament, lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche, 
                prise_1, prise_2, prise_3 FROM compartiments WHERE id_compartiment=?""", (id_compartiment,))
                data_compartiment = cursor.fetchone()
                conn.close()
#                print("dans recupere de 3 prises")
#                print(data_compartiment)
                return data_compartiment

        def enregistrer_m(self, id_compartiment, nom_medicament, lundi, mardi, mercredi, jeudi,
                                vendredi, samedi, dimanche, prise_1, prise_2, prise_3):

                conn = sqlite3.connect('compartiments.db')
                cursor = conn.cursor()
                data = {"id_compartiment" :id_compartiment, "medicament" :nom_medicament, "lundi" :lundi, 
                "mardi" :mardi, "mercredi" :mercredi, "jeudi" :jeudi, "vendredi" :vendredi, "samedi" :samedi,
                "dimanche" :dimanche, "prise_1" :prise_1, "prise_2" :prise_2, "prise_3" :prise_3}
                cursor.execute("""
                INSERT OR REPLACE INTO compartiments(id_compartiment, medicament, lundi, mardi, mercredi, jeudi, vendredi, samedi,
                dimanche, prise_1, prise_2, prise_3) VALUES(:id_compartiment, :medicament, :lundi, :mardi, :mercredi, :jeudi, :vendredi,
                :samedi, :dimanche, :prise_1, :prise_2, :prise_3)""", data)
                conn.commit()
                conn.close()
#                print("enregistré 3 prises")
#                print(data)
        
        def supp_prise_m(self):
                conn = sqlite3.connect('compartiments.db')
                cursor = conn.cursor()
                prise_3 = None
                data = {"prise_3" :prise_3}
                cursor.execute("""REPLACE INTO compartiments(prise_3) VALUES(:prise_3)""", data,)
                conn.commit()
                conn.close()
