from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import uic
from uiTest.dicSelect import *



class Login:
    '''
    登录界面,widget窗口
    '''
    def __init__(self):
        self.ui = uic.loadUi('../uiTest/login.ui')
        self.ui.loginButton.clicked.connect(self.handleCalc)
        self.ui.pwdText.returnPressed.connect(self.handleCalc)
        self.ui.usrText.returnPressed.connect(self.handleCalc)

    #登录按键 or enter键
    def handleCalc(self):
        usr = self.ui.usrText.text()
        pwd = self.ui.pwdText.text()
        print(usr,pwd)
        if usr == '' and pwd =='':
            self.mainWindow = MainWindow()
            self.mainWindow.ui.show()
            self.ui.close()
        else:
            QMessageBox.about(self.ui,'提示','密码输入错误\n\n请重新输入密码')
            self.ui.pwdText.clear()
            self.ui.usrText.clear()

    #注册按键


class MainWindow:
    '''
    主界面,mainwindow窗口
    '''
    def __init__(self):
        self.ui = uic.loadUi('../uiTest/mainWindow.ui')
        #初始化天气信息
        self.ui.weatherLabel.setText('未初始化天气')

        self.ui.DictationButton.clicked.connect(self.handleDictation)

    def handleDictation(self):
        self.dicSelectDialog=dicSelectDialog()
        self.dicSelectDialog.ui.show()

class dicSelectDialog:

    def __init__(self):
        self.ui = uic.loadUi('../uiTest/dicSelect.ui')

        self.ui.BookCBox




















app = QApplication([])
login = Login()
login.ui.show()
app.exec_()