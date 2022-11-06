from View.src.logo import *
from Model import MainWindow
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

app = QApplication([])
BootMask = QUiLoader().load("./View/Boot.ui")
BootMask.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint |
                        Qt.WindowType.FramelessWindowHint)
BootMask.show()
delayTime = 1
timer = QtCore.QElapsedTimer()
timer.start()
while (timer.elapsed() < (delayTime * 1000)):
    app.processEvents()
    BootMask.progressBar.setValue((timer.elapsed()/delayTime * 1000)/10000)
BootMask.close()
window = MainWindow.MainWindow()
window.ui.show()
app.exec()
