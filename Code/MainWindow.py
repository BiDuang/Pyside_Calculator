from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from decimal import *


class Dynamic_Resource():
    # 动态链接资源文件
    @staticmethod
    def readFile(dir: str):
        with open(dir, 'r') as f:
            return f.read()


class MainWindow(QWindow):

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load("./View/MainWindow.ui")

        # 禁用最大化按钮并禁止修改窗口尺寸
        self.ui.setWindowFlags(Qt.WindowType.CustomizeWindowHint |
                               Qt.WindowType.WindowMinimizeButtonHint |
                               Qt.WindowType.WindowCloseButtonHint)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())

        self.isTop = False
        self.cursor_pos = 0
        self.lastResult = "0"

        self.ui.input.setValidator(QRegularExpressionValidator(
            QRegularExpression("[a-zA-Z0-9.%+*/=(),]{255}"), self))

        self.ui.result.setValidator(QRegularExpressionValidator(
            QRegularExpression("[a-zA-Z0-9.%+*/=(),]{0}"), self))

        # 数字按钮监听事件注册
        self.ui.btn_numpad_dot.clicked.connect(self.input_dot)
        self.ui.btn_numpad_0.clicked.connect(self.input_0)
        self.ui.btn_numpad_1.clicked.connect(self.input_1)
        self.ui.btn_numpad_2.clicked.connect(self.input_2)
        self.ui.btn_numpad_3.clicked.connect(self.input_3)
        self.ui.btn_numpad_4.clicked.connect(self.input_4)
        self.ui.btn_numpad_5.clicked.connect(self.input_5)
        self.ui.btn_numpad_6.clicked.connect(self.input_6)
        self.ui.btn_numpad_7.clicked.connect(self.input_7)
        self.ui.btn_numpad_8.clicked.connect(self.input_8)
        self.ui.btn_numpad_9.clicked.connect(self.input_9)
        # 运算符按钮监听事件注册
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_cm_add.clicked.connect(self.cm_add)
        self.ui.btn_cm_sub.clicked.connect(self.cm_sub)
        self.ui.btn_cm_mult.clicked.connect(self.cm_mult)
        self.ui.btn_cm_div.clicked.connect(self.cm_div)
        # 运算功能按钮监听事件注册
        self.ui.btn_sp_bracket_l.clicked.connect(self.brackets_left)
        self.ui.btn_sp_bracket_r.clicked.connect(self.brackets_right)
        self.ui.btn_cm_mod.clicked.connect(self.cm_mod)
        self.ui.btn_backspace.clicked.connect(self.backspace)
        self.ui.btn_clear.clicked.connect(self.calculator_reset)
        # 窗口功能按钮监听事件注册
        self.ui.btn_sp_top.clicked.connect(self.windowTop)
        self.ui.btn_history.clicked.connect(self.get_history_result)
        # 输入框光标移动事件注册
        self.ui.input.cursorPositionChanged.connect(
            self.cursor_position_changed)

    def calculator_reset(self) -> None:
        self.ui.input.clear()
        self.ui.result.setText("0")

    def backspace(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.ui.input.text().__len__()-1])

    def windowTop(self) -> None:
        if(not self.isTop):
            self.ui.setWindowFlags(Qt.WindowType.CustomizeWindowHint |
                                   Qt.WindowType.WindowMinimizeButtonHint |
                                   Qt.WindowType.WindowCloseButtonHint |
                                   Qt.WindowType.WindowStaysOnTopHint)
            self.ui.btn_sp_top.setStyleSheet(Dynamic_Resource.readFile(
                "./View/res/qss/btn_windowTop_on.qss"))
        else:
            self.ui.setWindowFlags(Qt.WindowType.CustomizeWindowHint |
                                   Qt.WindowType.WindowMinimizeButtonHint |
                                   Qt.WindowType.WindowCloseButtonHint)
            self.ui.btn_sp_top.setStyleSheet(Dynamic_Resource.readFile(
                "./View/res/qss/btn_windowTop_regular.qss"))
        self.isTop = not self.isTop
        self.ui.show()

    def get_history_result(self) -> None:
        self.ui.input.setText(self.lastResult)

    def cursor_position_changed(self) -> None:
        self.cursor_pos = self.ui.input.cursorPosition()

    def brackets_left(self) -> None:
        self.ui.input.setText(self.ui.input.text()+'(')

    def brackets_right(self) -> None:
        self.ui.input.setText(self.ui.input.text()+')')

    def cm_add(self) -> None:
        self.ui.input.setText(self.ui.input.text()+'+')

    def cm_sub(self) -> None:
        self.ui.input.setText(self.ui.input.text()+'-')

    def cm_mult(self) -> None:
        self.ui.input.setText(self.ui.input.text()+'*')

    def cm_div(self) -> None:
        self.ui.input.setText(self.ui.input.text()+'/')

    def cm_mod(self) -> None:
        self.ui.input.setText(self.ui.input.text()+'%')

    def equal(self):
        if(self.ui.input.text().strip() == ""):
            self.ui.input.setText("0")
            return

        input_str = self.ui.input.text().strip()
        if(input_str[-1] == '='):
            self.ui.input.setText(
                input_str.replace('=', ''))
            input_str = self.ui.input.text().strip()

        while(input_str.__len__() > 1 and input_str[0] == '0' and input_str[1] != '.'):
            input_str = input_str.removeprefix('0')

        self.ui.input.setText(input_str)

        try:
            if(str(eval(self.ui.input.text())).__len__()-str(int(eval(self.ui.input.text()))).__len__() >= 8):
                self.ui.result.setText(
                    str(Decimal(eval(self.ui.input.text())).quantize(Decimal('.00000000'), rounding=ROUND_HALF_UP)))
            else:
                self.ui.result.setText(
                    str(eval(self.ui.input.text())))
            self.lastResult = self.ui.result.text()
            self.ui.input.setText(self.ui.input.text()+'=')
        except SyntaxError:
            self.ui.result.setText("计算式错误")
        except ZeroDivisionError:
            self.ui.result.setText("除数不能为零")
        except TypeError:
            self.ui.result.setText("计算式错误")
        except Exception as e:
            self.ui.result.setText(f"未知错误: {str(e)}")

    def input_dot(self) -> None:
        if(self.ui.input.text() == ''):
            self.ui.input.setText("0")
        self.ui.input.setText(self.ui.input.text()+'.')

    def input_0(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'0'+self.ui.input.text()[self.cursor_pos:])

    def input_1(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'1'+self.ui.input.text()[self.cursor_pos:])

    def input_2(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'2'+self.ui.input.text()[self.cursor_pos:])

    def input_3(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'3'+self.ui.input.text()[self.cursor_pos:])

    def input_4(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'4'+self.ui.input.text()[self.cursor_pos:])

    def input_5(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'5'+self.ui.input.text()[self.cursor_pos:])

    def input_6(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'6'+self.ui.input.text()[self.cursor_pos:])

    def input_7(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'7'+self.ui.input.text()[self.cursor_pos:])

    def input_8(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'8'+self.ui.input.text()[self.cursor_pos:])

    def input_9(self) -> None:
        self.ui.input.setText(self.ui.input.text()[
                              :self.cursor_pos]+'9'+self.ui.input.text()[self.cursor_pos:])
