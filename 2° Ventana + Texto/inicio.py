# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar, QStatusBar, QLabel
from PyQt5.QtGui import QIcon

class principal(QMainWindow): # Creo la ventana
    def __init__(self, *args):
        super().__init__(*args)
        
        # Propiedades
        
        self.setWindowTitle('Ventana Principal')
        self.setGeometry(100, 100, 500, 300)
              
        label = QLabel('This is QLabel widget')
        label.setText('Hola')
         
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = principal()
    sys.exit(app.exec_())
