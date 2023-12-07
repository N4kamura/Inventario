from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QTextCharFormat, QFont, QTextCursor
import sys

user = ""

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./imagenes/margoth.ui",self)

        self.pushButton_Guardar.clicked.connect(self.save)
        self.pushButton_Buscar.clicked.connect(self.find)
        self.pushButton_Cambiar.clicked.connect(self.cambiar_ventana)

    def cambiar_ventana(self):
        self.ventana = Cambiar()
        self.ventana.show()

    def save(self):
        self.textBrowser.clear()
        self.textBrowser.append(
"""Hola
Como
Estas""")

    def find(self):
        pass

class Cambiar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./imagenes/cambiar.ui",self)

class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./imagenes/inicio.ui",self)

        self.pushButton.clicked.connect(self.iniciar)
    
    def iniciar(self):
        global user
        user = self.lineEdit.text()
        self.ventana = Window()
        self.ventana.show()

def main():
    app = QApplication(sys.argv)
    window = Inicio()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()