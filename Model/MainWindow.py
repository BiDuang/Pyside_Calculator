from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from Model.About import *
from enum import Enum, unique


@unique
class Calculate_Mode(Enum):
    undefined = 0
    add = 1
    sub = 2
    mult = 3
    div = 4


class Dynamic_Resource():
    @staticmethod
    def readQSS(style: str):
        with open(style, 'r') as f:
            return f.read()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load("View\MainWindow.ui")
        self.ui.setWindowFlags(Qt.WindowType.CustomizeWindowHint |
                               Qt.WindowType.WindowMinimizeButtonHint |
                               Qt.WindowType.WindowCloseButtonHint)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())

        # 信号事件注册
        self.ui.Input_0.clicked.connect(self.input_0_clicked)
        self.ui.Input_1.clicked.connect(self.input_1_clicked)
        self.ui.Input_2.clicked.connect(self.input_2_clicked)
        self.ui.Input_3.clicked.connect(self.input_3_clicked)
        self.ui.Input_4.clicked.connect(self.input_4_clicked)
        self.ui.Input_5.clicked.connect(self.input_5_clicked)
        self.ui.Input_6.clicked.connect(self.input_6_clicked)
        self.ui.Input_7.clicked.connect(self.input_7_clicked)
        self.ui.Input_8.clicked.connect(self.input_8_clicked)
        self.ui.Input_9.clicked.connect(self.input_9_clicked)
        self.ui.Input_Neg.clicked.connect(self.input_neg_clicked)

        self.ui.Input_Reset.clicked.connect(self.input_reset_clicked)
        self.ui.Input_Bksp.clicked.connect(self.input_backspace_clicked)
        self.ui.Rt_Last_Res.clicked.connect(self.rt_last_res_clicked)

        self.ui.Input_Add.clicked.connect(self.input_add_clicked)
        self.ui.Input_Sub.clicked.connect(self.input_sub_clicked)
        self.ui.Input_Mult.clicked.connect(self.input_mult_clicked)
        self.ui.Input_Div.clicked.connect(self.input_div_clicked)
        self.ui.Input_Equ.clicked.connect(self.input_equal_clicked)
        self.ui.About.clicked.connect(self.about_clicked)

        # 快捷键事件注册
        self.kb_input_0 = QShortcut(QKeySequence("0"), self.ui)
        self.kb_input_1 = QShortcut(QKeySequence("1"), self.ui)
        self.kb_input_2 = QShortcut(QKeySequence("2"), self.ui)
        self.kb_input_3 = QShortcut(QKeySequence("3"), self.ui)
        self.kb_input_4 = QShortcut(QKeySequence("4"), self.ui)
        self.kb_input_5 = QShortcut(QKeySequence("5"), self.ui)
        self.kb_input_6 = QShortcut(QKeySequence("6"), self.ui)
        self.kb_input_7 = QShortcut(QKeySequence("7"), self.ui)
        self.kb_input_8 = QShortcut(QKeySequence("8"), self.ui)
        self.kb_input_9 = QShortcut(QKeySequence("9"), self.ui)
        self.kb_bksp = QShortcut(QKeySequence(Qt.Key_Backspace), self.ui)
        self.kb_add = QShortcut(QKeySequence(Qt.Key_Plus), self.ui)
        self.kb_min = QShortcut(QKeySequence(Qt.Key_Minus), self.ui)
        self.kb_slash = QShortcut(QKeySequence(Qt.Key_Slash), self.ui)
        self.kb_asterisk = QShortcut(QKeySequence(Qt.Key_Asterisk), self.ui)
        self.kb_enter = QShortcut(QKeySequence(Qt.Key_Enter), self.ui)
        self.kb_return = QShortcut(QKeySequence(Qt.Key_Return), self.ui)
        self.kb_clear = QShortcut(QKeySequence(Qt.Key_Escape), self.ui)
        self.kb_lst_record = QShortcut(QKeySequence("`"), self.ui)

        # 快捷键事件绑定
        self.kb_input_0.activated.connect(self.input_0_clicked)
        self.kb_input_1.activated.connect(self.input_1_clicked)
        self.kb_input_2.activated.connect(self.input_2_clicked)
        self.kb_input_3.activated.connect(self.input_3_clicked)
        self.kb_input_4.activated.connect(self.input_4_clicked)
        self.kb_input_5.activated.connect(self.input_5_clicked)
        self.kb_input_6.activated.connect(self.input_6_clicked)
        self.kb_input_7.activated.connect(self.input_7_clicked)
        self.kb_input_8.activated.connect(self.input_8_clicked)
        self.kb_input_9.activated.connect(self.input_9_clicked)
        self.kb_bksp.activated.connect(self.input_backspace_clicked)
        self.kb_add.activated.connect(self.input_add_clicked)
        self.kb_min.activated.connect(self.input_sub_clicked)
        self.kb_asterisk.activated.connect(self.input_mult_clicked)
        self.kb_slash.activated.connect(self.input_div_clicked)
        self.kb_enter.activated.connect(self.input_equal_clicked)
        self.kb_return.activated.connect(self.input_equal_clicked)

        self.kb_clear.activated.connect(self.input_reset_clicked)
        self.kb_lst_record.activated.connect(self.rt_last_res_clicked)

        self.toolong_ignored: bool = False
        self.init()

    def init(self):
        self.compute_str: str = "0"
        self.last_record = 0
        self.compute_mode = Calculate_Mode['undefined']

        self.textbox_refresh()
        self.ui.Textbox_Operand.setText("")
        self.ui.Text_Result.setText("0")

        self.ui.Rt_Last_Res.setEnabled(False)
        self.ui.Rt_Last_Res.setStyleSheet(Dynamic_Resource.readQSS(
            "View\\QSS\\rt_last_res_disable.qss"))

    def calculate_data_save(self):
        if(self.compute_str.__len__() >= 6 and not self.toolong_ignored):
            self.too_long_calculate()
            if(not self.toolong_ignored):
                return
        self.operand = int(self.compute_str)
        self.ui.Textbox_Operand.setText(str(self.operand))
        self.compute_str = "0"
        self.textbox_refresh()

    def too_long_calculate(self):
        warn = QMessageBox.question(
            self.ui, "运算警告", "你正在尝试计算此程序设计之外的数据\n\n这可能导致程序崩溃或显示异常\n\n你仍然要继续吗？",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if(warn == QMessageBox.Yes):
            self.ui.Text_Result.setStyleSheet(Dynamic_Resource.readQSS(
                "View\\QSS\\warn_result_textbox.qss"))
            self.toolong_ignored = True
            return
        else:
            self.input_reset_clicked()

    def calculate_error(self):
        self.kb_input_0.setEnabled(False)
        self.kb_input_1.setEnabled(False)
        self.kb_input_2.setEnabled(False)
        self.kb_input_3.setEnabled(False)
        self.kb_input_4.setEnabled(False)
        self.kb_input_5.setEnabled(False)
        self.kb_input_6.setEnabled(False)
        self.kb_input_7.setEnabled(False)
        self.kb_input_8.setEnabled(False)
        self.kb_input_9.setEnabled(False)
        self.kb_add.setEnabled(False)
        self.kb_min.setEnabled(False)
        self.kb_asterisk.setEnabled(False)
        self.kb_slash.setEnabled(False)
        self.kb_enter.setEnabled(False)
        self.kb_return.setEnabled(False)
        self.kb_lst_record.setEnabled(False)

        self.ui.Input_0.setEnabled(False)
        self.ui.Input_1.setEnabled(False)
        self.ui.Input_2.setEnabled(False)
        self.ui.Input_3.setEnabled(False)
        self.ui.Input_4.setEnabled(False)
        self.ui.Input_5.setEnabled(False)
        self.ui.Input_6.setEnabled(False)
        self.ui.Input_7.setEnabled(False)
        self.ui.Input_8.setEnabled(False)
        self.ui.Input_9.setEnabled(False)
        self.ui.Input_Neg.setEnabled(False)
        self.ui.Input_Add.setEnabled(False)
        self.ui.Input_Sub.setEnabled(False)
        self.ui.Input_Mult.setEnabled(False)
        self.ui.Input_Div.setEnabled(False)
        self.ui.Input_Equ.setEnabled(False)
        self.ui.Input_Bksp.setEnabled(False)
        self.ui.Text_Result.setStyleSheet(Dynamic_Resource.readQSS(
            "View\\QSS\\err_result_textbox.qss"))
        self.last_record = 0
        self.ui.Rt_Last_Res.setEnabled(False)
        self.ui.Rt_Last_Res.setStyleSheet(Dynamic_Resource.readQSS(
            "View\\QSS\\rt_last_res_disable.qss"))
        self.ui.Text_Result.setText("警告：除数不能为零")

    def textbox_refresh(self):
        if(self.compute_str != "0"):
            self.compute_str = self.compute_str.removeprefix("0")
        self.ui.Textbox_Input.setText(self.compute_str)

    def btn_style_refresh(self):
        self.ui.Input_Add.setStyleSheet(Dynamic_Resource.readQSS(
            "View\QSS\calculate_mode_btn.qss"))
        self.ui.Input_Sub.setStyleSheet(Dynamic_Resource.readQSS(
            "View\QSS\calculate_mode_btn.qss"))
        self.ui.Input_Mult.setStyleSheet(Dynamic_Resource.readQSS(
            "View\QSS\calculate_mode_btn.qss"))
        self.ui.Input_Div.setStyleSheet(Dynamic_Resource.readQSS(
            "View\QSS\calculate_mode_btn.qss"))

    def input_backspace_clicked(self):
        if(self.compute_str == '0'):
            return
        self.compute_str = self.compute_str[:self.compute_str.__len__()-1]
        if(self.compute_str == ''):
            self.compute_str = "0"
        self.textbox_refresh()

    def input_equal_clicked(self):
        if(self.compute_str.__len__() >= 6 and not self.toolong_ignored):
            self.too_long_calculate()
            if(not self.toolong_ignored):
                return

        if(self.compute_mode == Calculate_Mode['undefined']):
            self.ui.Text_Result.setText(self.compute_str)
            self.last_record = int(self.compute_str)

        if(self.compute_mode == Calculate_Mode['add']):
            self.last_record = self.operand+int(self.compute_str)
            self.ui.Text_Result.setText(str(self.last_record))
        elif(self.compute_mode == Calculate_Mode['sub']):
            self.last_record = self.operand-int(self.compute_str)
            self.ui.Text_Result.setText(str(self.last_record))
        elif(self.compute_mode == Calculate_Mode['mult']):
            self.last_record = self.operand*int(self.compute_str)
            self.ui.Text_Result.setText(str(self.last_record))
        elif(self.compute_mode == Calculate_Mode['div']):
            if(int(self.compute_str) == 0):
                self.calculate_error()
                return
            if(self.operand % int(self.compute_str) != 0):
                self.ui.Text_Result.setStyleSheet(Dynamic_Resource.readQSS(
                    "View\\QSS\\warn_result_textbox.qss"))
            self.last_record = int(self.operand/int(self.compute_str))
            self.ui.Text_Result.setText(str(self.last_record))

        self.ui.Rt_Last_Res.setStyleSheet(Dynamic_Resource.readQSS(
            "View\\QSS\\rt_last_res_enable.qss"))
        self.ui.Rt_Last_Res.setEnabled(True)

    def rt_last_res_clicked(self):
        self.compute_str = str(self.last_record)
        self.btn_style_refresh()
        self.compute_mode = Calculate_Mode['undefined']
        if(not self.toolong_ignored):
            self.ui.Text_Result.setStyleSheet(Dynamic_Resource.readQSS(
                "View\\QSS\\normal_result_textbox.qss"))
        self.ui.Text_Result.setText("0")
        self.ui.Textbox_Operand.setText("")
        self.textbox_refresh()

    def input_reset_clicked(self):
        self.kb_input_0.setEnabled(True)
        self.kb_input_1.setEnabled(True)
        self.kb_input_2.setEnabled(True)
        self.kb_input_3.setEnabled(True)
        self.kb_input_4.setEnabled(True)
        self.kb_input_5.setEnabled(True)
        self.kb_input_6.setEnabled(True)
        self.kb_input_7.setEnabled(True)
        self.kb_input_8.setEnabled(True)
        self.kb_input_9.setEnabled(True)
        self.kb_add.setEnabled(True)
        self.kb_min.setEnabled(True)
        self.kb_asterisk.setEnabled(True)
        self.kb_slash.setEnabled(True)
        self.kb_enter.setEnabled(True)
        self.kb_return.setEnabled(True)
        self.kb_lst_record.setEnabled(True)

        self.ui.Input_0.setEnabled(True)
        self.ui.Input_1.setEnabled(True)
        self.ui.Input_2.setEnabled(True)
        self.ui.Input_3.setEnabled(True)
        self.ui.Input_4.setEnabled(True)
        self.ui.Input_5.setEnabled(True)
        self.ui.Input_6.setEnabled(True)
        self.ui.Input_7.setEnabled(True)
        self.ui.Input_8.setEnabled(True)
        self.ui.Input_9.setEnabled(True)
        self.ui.Input_Neg.setEnabled(True)
        self.ui.Input_Add.setEnabled(True)
        self.ui.Input_Sub.setEnabled(True)
        self.ui.Input_Mult.setEnabled(True)
        self.ui.Input_Div.setEnabled(True)
        self.ui.Input_Equ.setEnabled(True)
        self.ui.Input_Bksp.setEnabled(True)
        if(not self.toolong_ignored):
            self.ui.Text_Result.setStyleSheet(Dynamic_Resource.readQSS(
                "View\\QSS\\normal_result_textbox.qss"))
        else:
            self.ui.Text_Result.setStyleSheet(Dynamic_Resource.readQSS(
                "View\\QSS\\warn_result_textbox.qss"))
        self.init()
        self.btn_style_refresh()

    def input_add_clicked(self):
        self.compute_mode = Calculate_Mode['add']
        self.btn_style_refresh()
        self.ui.Input_Add.setStyleSheet(Dynamic_Resource.readQSS(
            "View\\QSS\\selected_calculate_mode_btn.qss"))
        self.calculate_data_save()

    def input_sub_clicked(self):
        self.compute_mode = Calculate_Mode['sub']
        self.btn_style_refresh()
        self.ui.Input_Sub.setStyleSheet(Dynamic_Resource.readQSS(
            "View\\QSS\\selected_calculate_mode_btn.qss"))
        self.calculate_data_save()

    def input_mult_clicked(self):
        self.compute_mode = Calculate_Mode['mult']
        self.btn_style_refresh()
        self.ui.Input_Mult.setStyleSheet(Dynamic_Resource.readQSS(
            "View\QSS\selected_calculate_mode_btn.qss"))
        self.calculate_data_save()

    def input_div_clicked(self):
        self.compute_mode = Calculate_Mode['div']
        self.btn_style_refresh()
        self.ui.Input_Div.setStyleSheet(Dynamic_Resource.readQSS(
            "View\\QSS\\selected_calculate_mode_btn.qss"))
        self.calculate_data_save()

    def input_neg_clicked(self):
        if(self.compute_str == '0'):
            return

        if(self.compute_str.startswith('-')):
            self.compute_str = self.compute_str.removeprefix('-')
        else:
            self.compute_str = '-' + self.compute_str

        self.textbox_refresh()

    def input_0_clicked(self):
        if(self.compute_str != "0"):
            self.compute_str += '0'
        else:
            pass
        self.textbox_refresh()

    def input_1_clicked(self):
        self.compute_str += '1'
        self.textbox_refresh()

    def input_2_clicked(self):
        self.compute_str += '2'
        self.textbox_refresh()

    def input_3_clicked(self):
        self.compute_str += '3'
        self.textbox_refresh()

    def input_4_clicked(self):
        self.compute_str += '4'
        self.textbox_refresh()

    def input_5_clicked(self):
        self.compute_str += '5'
        self.textbox_refresh()

    def input_6_clicked(self):
        self.compute_str += '6'
        self.textbox_refresh()

    def input_7_clicked(self):
        self.compute_str += '7'
        self.textbox_refresh()

    def input_8_clicked(self):
        self.compute_str += '8'
        self.textbox_refresh()

    def input_9_clicked(self):
        self.compute_str += '9'
        self.textbox_refresh()

    def about_clicked(self):

        self.about_popup = About()
        self.about_popup.ui.show()
