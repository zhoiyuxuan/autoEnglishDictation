# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dicSelect.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from tools.dic2json import *

class Ui_DictDialog(object):
    def setupUi(self, DictDialog):
        DictDialog.setObjectName("DictDialog")
        DictDialog.setEnabled(True)
        DictDialog.resize(402, 296)
        self.buttonBox = QtWidgets.QDialogButtonBox(DictDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DictDialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DictDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DictDialog)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 331, 16))
        self.label_3.setObjectName("label_3")
        self.BookCBox = QtWidgets.QComboBox(DictDialog)
        self.BookCBox.setGeometry(QtCore.QRect(110, 40, 104, 41))
        self.BookCBox.setEditable(False)
        self.BookCBox.setObjectName("BookCBox")
        self.LessonCBox = QtWidgets.QComboBox(DictDialog)
        self.LessonCBox.setGeometry(QtCore.QRect(110, 110, 104, 26))
        self.LessonCBox.setObjectName("LessonCBox")

        self.retranslateUi(DictDialog)
        self.buttonBox.accepted.connect(DictDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(DictDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DictDialog)

    def retranslateUi(self, DictDialog):
        _translate = QtCore.QCoreApplication.translate
        DictDialog.setWindowTitle(_translate("DictDialog", "选择默写内容"))
        self.label.setText(_translate("DictDialog", "选择课本"))
        self.label_2.setText(_translate("DictDialog", "选择课程"))
        self.label_3.setText(_translate("DictDialog", "您选择的是："))

        #实现两多选框绑定
        self.content = wr_json(
            path_file='../data/book.json',
            type = 'read'
        )
        bookname=list(self.content.keys())
        self.BookCBox.addItems(bookname)
        currentBook = self.BookCBox.currentText()
        initbooknum = self.content[currentBook]
        lessons=[]
        for i in range(0,initbooknum):
            lessons.append(str(i+1))
        self.LessonCBox.addItems(lessons)
        self.label_3.setText('您当前选择的是: {} {}'.format(currentBook,initbooknum))

        self.BookCBox.currentIndexChanged.connect(self.handleBookChange)
        self.LessonCBox.currentIndexChanged.connect(self.handleLabel)


    def handleBookChange(self):
        self.LessonCBox.clear()
        currentBook = self.BookCBox.currentText()
        num = self.content[currentBook]
        lessons = []
        for i in range(0, num):
            lessons.append(str(i+1))
        self.LessonCBox.addItems(lessons)

    def handleLabel(self):
        currentBook = self.BookCBox.currentText()
        currentLesson = self.LessonCBox.currentText()
        self.label_3.setText('您当前选择的是: {} {}'.format(currentBook,currentLesson))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    DictDialog = QtWidgets.QDialog()
    ui = Ui_DictDialog()
    ui.setupUi(DictDialog)
    DictDialog.show()
    sys.exit(app.exec_())