from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class About(QMainWindow):

    __author__ = "BiDuang"
    __version__ = "Rev - 2.2.16"

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load("./View/About.ui")
        self.ui.setWindowFlags(
            Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        self.ui.version.setText(self.__version__)
