from Code import MainWindow
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from View.res.qrc import About
from View.res.qrc import main

app = QApplication([])
window = MainWindow.MainWindow()
window.ui.show()
app.exec()
