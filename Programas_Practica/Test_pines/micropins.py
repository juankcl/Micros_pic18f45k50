# This Python file uses the following encoding: utf-8
import sys

# pip install pyqt5
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPlainTextEdit, QMessageBox
from PyQt5 import uic

# Cargar archivo de interfaz
qtCreatorFile = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Array con los nombres de todos los pines
pines = ["RE3", "RA0", "RA1", "RA2", "RA3", "RA4", "RA5", "RE0", "RE1", "RE2",
         "Vdd", "Vss", "RA7", "RA6", "RC0", "RC1", "RC2", "Vusb", "RD0", "RD1",
         "RB7", "RB6", "RB5", "RB4", "RB3", "RB2", "RB1", "RB0", "Vdd", "Vss",
         "RD7", "RD6", "RD5", "RD4", "RC7", "RC6", "D+", "D-", "RD3", "RD2"]


class microPins(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Conectar las señales de los botones
        self.btMostrarPines.clicked.connect(self.MostrarPines)
        self.btRespuestas.clicked.connect(self.ComprobarRespuestas)
        self.btReset.clicked.connect(self.ResetTextBox)

        # Guardar los text box en una variable llamada children
        regexLabels = QtCore.QRegExp("((txtLbl))\\w*")
        self.children = self.findChildren(QPlainTextEdit, regexLabels)
        # Guardar el estilo por default de los text box
        self.defaultStyle = self.children[0].styleSheet()

        self.show()

    def MostrarPines(self):
        # Quitar formato de los botones
        self.ResetTextBox()
        # Escribir en cada text box la respuesta correcta
        for i in range(len(self.children)):
            self.children[i].setPlainText(pines[i])

    def ResetTextBox(self):
        for child in self.children:
            child.setStyleSheet(self.defaultStyle)
            child.setPlainText("")

    def ComprobarRespuestas(self):
        incorrectas = 0
        # Comprobar las respuestas usando el array de pines
        for i in range(len(self.children)):
            # Correcto
            if self.children[i].toPlainText().upper() == pines[i].upper():
                self.children[i].setStyleSheet(
                    'background-color: rgb(42, 181, 42);\
                     color: white;')
            # Incorrecto
            else:
                incorrectas += 1
                respuetaInc = self.children[i].toPlainText()
                respuetaInc += " (" + pines[i] + ")"
                self.children[i].setPlainText(respuetaInc)
                self.children[i].setStyleSheet(
                    'background-color: rgb(188, 42, 42);\
                     color: white;')
        dialog = QMessageBox()
        dialog.setWindowTitle("Resultados")
        if incorrectas == 1:
            dialog.setText("¡Tuviste " + str(40 - incorrectas) +
                           " respuestas correctas!\n Y " + str(incorrectas) + " respuesta incorrecta.")
        elif incorrectas > 0:
            dialog.setText("¡Tuviste " + str(40 - incorrectas) +
                           " respuestas correctas!\n Y " + str(incorrectas) + " respuestas incorrectas.")
        else:
            dialog.setText("¡Todas tus respuestas son correctas!")
        dialog.exec()

if __name__ == "__main__":
    app = QApplication([])
    window = microPins()
    sys.exit(app.exec_())
