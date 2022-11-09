from Code import MainWindow
from PySide6.QtWidgets import *
from View.res.qrc import main

app = QApplication([])
window = MainWindow.MainWindow()
window.ui.show()
app.exec()
